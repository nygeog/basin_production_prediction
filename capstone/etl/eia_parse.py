import pandas as pd
import us


def eia_parse_county(eia_cnty_xls):
    eia_cnty = pd.read_excel(
        eia_cnty_xls,
        sheet_name='RegionCounties',
    )

    eia_cnty.columns = [c.lower() for c in eia_cnty.columns]

    # eia data for some reason has the incorrect state fips codes, remap here
    eia_cnty['stateid'] = eia_cnty['state'].map(remap_state_fips)

    return eia_cnty


def remap_state_fips(state_abbrev):
    s = us.states.lookup(state_abbrev)
    return s.fips
