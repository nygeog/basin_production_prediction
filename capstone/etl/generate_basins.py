import pandas as pd


# this only applies to generating basins in the us
def generate_us_basins(census, eia_cnty, basins_output_dir):
    print('generating us basins')
    basins_geo_all = pd.merge(
        left=census,
        right=eia_cnty,
        on='geoid',
        how='inner',
    )

    basins_gdf_list = []

    for region in basins_geo_all['region'].unique():
        print(f"    {region.lower()}")

        region_gdf = basins_geo_all[basins_geo_all['region'] == region]
        basin_gdf = region_gdf.dissolve(by='region', aggfunc='sum')

        basin_filename = region.lower().replace(' ', '_')
        basin_gdf.to_file(
            f"{basins_output_dir}/{basin_filename}.shp",
            driver='ESRI Shapefile',
        )

        basins_gdf_list.append([region, basin_filename, basin_gdf])

    basins_geo_all.to_file(
        f"{basins_output_dir}/all_us_basins.shp",
        driver='ESRI Shapefile',
    )

    return basins_gdf_list, basins_geo_all
