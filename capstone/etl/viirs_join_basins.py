from capstone.etl.viirs_parse import viirs_parse
from tools.geoprocessing import point_in_polygon
import pandas as pd
import os


def viirs_join_basins(wd, basins, viirs_files, suffix):
    all_int_viirs_list = []

    for basin in basins:
        basin_name, basin_filename, basin_gdf = basin[0], basin[1], basin[2]

        print(f"selecting viirs for {basin_filename}")

        basin_int_viirs_list = []

        for viirs_file in viirs_files:
            print(f"    {os.path.basename(viirs_file)}")

            viirs_gdf = viirs_parse(viirs_file)

            viirs_int_basin = point_in_polygon(
                viirs_gdf,  # set to same crs as census
                basin_gdf,
            )

            basin_int_viirs_list.append(viirs_int_basin)

        basin_viirs = pd.concat(basin_int_viirs_list, sort=True)

        basin_viirs.to_file(
            f"{wd}/processing/{basin_filename}_int_viirs.gpkg",
            driver="GPKG",  # 'ESRI Shapefile',
        )

        basin_viirs.to_csv(
            f"{wd}/processing/{basin_filename}_int_viirs.csv",
            index=False,
        )

        all_int_viirs_list.append(basin_viirs)

    gdf = pd.concat(all_int_viirs_list, sort=True)

    gdf.to_file(
        f"{wd}/processing/all_int_viirs_{suffix}.gpkg",
        driver="GPKG",  # 'ESRI Shapefile',
    )

    gdf.to_csv(
        f"{wd}/processing/all_int_viirs_{suffix}.csv",
        index=False,
    )

    return gdf
