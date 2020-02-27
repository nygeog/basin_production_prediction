import pandas as pd
import us
from tools.tools import open_excel_workbook, excel_sheet_names
import os


def eia_parse_county(eia_cnty_xls):
    eia_cnty = pd.read_excel(
        eia_cnty_xls,
        sheet_name='RegionCounties',
    )

    eia_cnty.columns = [c.lower() for c in eia_cnty.columns]

    # eia data for some reason has the incorrect state fips codes, remap here
    eia_cnty['stateid'] = eia_cnty['state'].map(remap_state_fips)

    eia_cnty['geoid'] = eia_cnty[
        'stateid'
    ].astype(str).str.zfill(2) + eia_cnty[
        'countyid'
    ].astype(str).str.zfill(3)

    return eia_cnty[['geoid', 'region']]


def remap_state_fips(state_abbrev):
    s = us.states.lookup(state_abbrev)
    return s.fips


def eia_parse_data(eia_xls):
    print(" parse eia data")
    xls_sheets = excel_sheet_names(
        open_excel_workbook(eia_xls)
    )

    out_dir = os.path.dirname(eia_xls)

    df_list = []

    for sheet in xls_sheets:
        if sheet != "RegionCounties":
            print(f"    for {sheet}")
            df = pd.read_excel(eia_xls, sheet_name=sheet, skiprows=[0])

            df.columns = [
                'month',
                'rig_count',
                'oil_bbl_d_production_per_rig',
                'oil_bbl_d_legacy_production_change',
                'oil_bbl_d_total_production',
                'natgas_mcf_d_production_per_rig',
                'natgas_mcf_d_legacy_production_change',
                'natgas_mcf_d_total_production',
            ]

            df['region'] = sheet

            df.to_csv(
                f"{out_dir }/{sheet.lower().replace(' ', '_')}.csv",
                index=False,
            )

            df_list.append(df)

    eia_data = pd.concat(df_list, sort=True)

    eia_data.to_csv(
        f"{out_dir}/all_eia_data.csv",
        index=False,
    )

    return eia_data
