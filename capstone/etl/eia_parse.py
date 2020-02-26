import pandas as pd
import us


def eia_parse_county():
    eia_cnty = pd.read_excel(
        '../data/input/eia/dpr-data.xlsx',
        sheet_name='RegionCounties',
    )

    eia_cnty.columns = [c.lower() for c in eia_cnty.columns]
    eia_cnty['stateid'] = eia_cnty['state'].map(remap_state_fips)



def remap_state_fips(state_abbrev):
    s = us.states.lookup(state_abbrev)
    return s.fips
