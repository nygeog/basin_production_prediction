import pandas as pd


def aggregate_viirs_by_basin_month(viirs_int_basins, eia_data):
    viirs_int_basins['date_mscan_yyyymm'] = viirs_int_basins[
        'date_mscan'
    ].dt.to_period('M')

    viirs_gby = viirs_int_basins.groupby(
        ["index_right", "date_mscan_yyyymm"],
    ).agg(
        count_obs=pd.NamedAgg(column='id', aggfunc='count'),
        temp_bb_mean=pd.NamedAgg(column='temp_bb', aggfunc='mean'),
        temp_bb_med=pd.NamedAgg(column='temp_bb', aggfunc='median'),
        temp_bb_sum=pd.NamedAgg(column='temp_bb', aggfunc='sum'),
        temp_bb_min=pd.NamedAgg(column='temp_bb', aggfunc='min'),
        temp_bb_max=pd.NamedAgg(column='temp_bb', aggfunc='max'),
    )

    viirs_gby = viirs_gby.reset_index()

    eia_data['month_yyyymm'] = eia_data['month'].dt.to_period('M')

    eia_data = eia_data[[
        'region',
        'month_yyyymm',
        'oil_bbl_d_total_production',
        'rig_count',
    ]]

    eia_agg_viirs = pd.merge(
        eia_data,
        viirs_gby,
        left_on=['region', 'month_yyyymm'],
        right_on=['index_right', 'date_mscan_yyyymm'],
        how='outer',
    )

    return eia_agg_viirs
