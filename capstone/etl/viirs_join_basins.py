from capstone.etl.viirs_parse import viirs_parse
from tools.geoprocessing import point_in_polygon
import pandas as pd
import os
import glob


def viirs_join_basins(wd, basins, viirs_files, suffix):
    wdt = "processing/intersect"  # intersect intermediate data folder

    for basin in basins:
        basin_name, basin_fname, basin_gdf = basin[0], basin[1], basin[2]

        print(f"selecting viirs for {basin_fname}")

        basin_int_viirs_list = []

        for viirs_file in viirs_files:
            print(f"    {os.path.basename(viirs_file)}")

            viirs_gdf = viirs_parse(viirs_file)

            viirs_int_basin = point_in_polygon(
                viirs_gdf,  # set to same crs as census
                basin_gdf,
            )

            basin_int_viirs_list.append(viirs_int_basin)

            viirs_date = os.path.basename(viirs_file)[9:17]

            viirs_int_basin.to_csv(
                f"{wd}/{wdt}/{basin_fname}_int_viirs_{viirs_date}_{suffix}.csv",
                index=False,
            )


def compile_basin_data(wd, basins, suffix):
    wdt = "processing/intersect"  # intersect intermediate data folder

    all_int_viirs_list = []

    for basin in basins:
        basin_name, basin_fname, basin_gdf = basin[0], basin[1], basin[2]

        basin_int_viirs_list = glob.glob(
            f"{wd}/{wdt}/{basin_fname}_int_viirs_*_{suffix}.csv",
        )
        basin_int_viirs_list.sort()  # sort

        basin_viirs_dfs = []  # basin viirs empty list

        for f in basin_int_viirs_list:
            df = pd.read_csv(f)
            basin_viirs_dfs.append(df)

        basin_viirs = pd.concat(basin_int_viirs_list, sort=True)

        # basin_viirs.to_file(
        #     f"{wd}/{basin_fname}_int_viirs_{suffix}.gpkg",
        #     driver="GPKG",
        # )

        basin_viirs.to_csv(
            f"{wd}/processing/{basin_fname}_int_viirs_{suffix}.csv",
            index=False,
        )

        all_int_viirs_list.append(basin_viirs)

    gdf = pd.concat(all_int_viirs_list, sort=True)

    # gdf.to_file(
    #     f"{wd}/processing/all_int_viirs_{suffix}.gpkg",
    #     driver="GPKG",  # 'ESRI Shapefile',
    # )

    gdf.to_csv(
        f"{wd}/processing/all_int_viirs_{suffix}.csv",
        index=False,
    )

    return gdf
