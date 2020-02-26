import geopandas as gpd


def point_in_polygon(point_gdf, poly_gdf):
    return gpd.sjoin(
        point_gdf,
        poly_gdf,
        how="inner",
        op='intersects',  # warning CRS of frames do not match
    )
