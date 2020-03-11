from code.etl.viirs_parse import viirs_parse
from tools.geoprocessing import point_in_polygon
import pandas as pd
import os
import glob
from pathlib import Path


def viirs_join_basins(wd, all_basins, viirs_files, suffix):
    wdt = "processing/intersect"  # intersect intermediate data folder
    print(f"selecting viirs for basins {suffix}")

    for viirs_file in viirs_files:
        vdate = os.path.basename(viirs_file)[9:17]  # viirs date
        if vdate[4:8] == '0101':
            print(f"    {vdate}")

        if not Path(
            f"{wd}/{wdt}/basins_int_viirs_{vdate}_{suffix}.csv"
        ).is_file():
            print(f"    {os.path.basename(viirs_file)}")

            viirs_gdf = viirs_parse(viirs_file)

            viirs_int_basin = point_in_polygon(
                viirs_gdf,  # set to same crs as census
                all_basins,
            )

            viirs_int_basin.to_csv(
                f"{wd}/{wdt}/basins_int_viirs_{vdate}_{suffix}.csv",
                index=False,
            )


def compile_basin_data(wd, suffix):
    wdt = "processing/intersect"  # intersect intermediate data folder

    basin_int_viirs_list = glob.glob(
        f"{wd}/{wdt}/basins_int_viirs_*_{suffix}.csv",
    )
    basin_int_viirs_list.sort()  # sort

    basin_viirs_dfs = []  # basin viirs empty list

    for f in basin_int_viirs_list:
        vdate = os.path.basename(f)[17:25]   # viirs date
        if vdate[4:8] == '0101':
            print(f"    {vdate}")

        df = pd.read_csv(f)
        basin_viirs_dfs.append(df)

    df = pd.concat(basin_viirs_dfs, sort=True)

    df.to_csv(
        f"{wd}/processing/basins_int_viirs_{suffix}.csv",
        index=False,
    )

    return df
