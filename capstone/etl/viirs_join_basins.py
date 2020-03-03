from capstone.etl.viirs_parse import viirs_parse
from tools.geoprocessing import point_in_polygon
import pandas as pd
import geopandas as gpd
import os
import glob
from pathlib import Path


def viirs_join_basins(wd, basins, viirs_files, suffix):
    wdt = "processing/intersect"  # intersect intermediate data folder

    for basin in basins:
        basin_name, basin_fname, basin_gdf = basin[0], basin[1], basin[2]

        print(f"selecting viirs for {basin_fname} {suffix}")

        for viirs_file in viirs_files:
            vdate = os.path.basename(viirs_file)[9:17]  # viirs date

            if not Path(
                f"{wd}/{wdt}/{basin_fname}_int_viirs_{vdate}_{suffix}.gpkg"
            ).is_file():
                print(f"    {os.path.basename(viirs_file)}")

                viirs_gdf = viirs_parse(viirs_file)

                viirs_int_basin = point_in_polygon(
                    viirs_gdf,  # set to same crs as census
                    basin_gdf,
                )

                viirs_int_basin.to_csv(
                    f"{wd}/{wdt}/{basin_fname}_int_viirs_{vdate}_{suffix}.csv",
                    index=False,
                )

                if len(viirs_int_basin) == 0:  # geopackage can't be written
                    break                      # if empty

                viirs_int_basin.to_file(
                    f"{wd}/{wdt}/{basin_fname}_int_viirs_{vdate}_{suffix}.gpkg",
                    driver="GPKG", 
                )


def compile_basin_data(wd, basins, suffix):
    wdt = "processing/intersect"  # intersect intermediate data folder

    all_int_viirs_list = []

    for basin in basins:
        basin_name, basin_fname, basin_gdf = basin[0], basin[1], basin[2]
        print(f'{basin_name}')

        basin_int_viirs_list = glob.glob(
            f"{wd}/{wdt}/{basin_fname}_int_viirs_*_{suffix}.gpkg",
        )
        basin_int_viirs_list.sort()  # sort

        basin_viirs_gdfs = []  # basin viirs empty list

        for f in basin_int_viirs_list:
            # print(f'{f}')
            df = gpd.read_file(f)
            basin_viirs_gdfs.append(df)

        print(len(basin_viirs_gdfs), 'geodataframes', suffix)

        # if len(basin_viirs_gdfs) != 0:  # geopackage can't be written
        #     break  # if empty

        basin_viirs = pd.concat(basin_viirs_gdfs, sort=True)

        basin_viirs.to_file(
            f"{wd}/{basin_fname}_int_viirs_{suffix}.gpkg",
            driver="GPKG",
        )

        basin_viirs.to_csv(
            f"{wd}/processing/{basin_fname}_int_viirs_{suffix}.csv",
            index=False,
        )

        all_int_viirs_list.append(basin_viirs)

    gdf = pd.concat(all_int_viirs_list, sort=True)

    gdf.to_file(
        f"{wd}/processing/all_int_viirs_{suffix}.gpkg",
        driver="GPKG",
    )

    gdf.to_csv(
        f"{wd}/processing/all_int_viirs_{suffix}.csv",
        index=False,
    )

    return gdf
