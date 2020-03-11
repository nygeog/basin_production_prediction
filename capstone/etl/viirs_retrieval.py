from datetime import date
import pandas as pd
import urllib.request
from urllib.error import HTTPError, URLError
import gzip
import shutil
import time
from pathlib import Path


def viirs_retrieval(
        workspace_directory,
        start_date,
        end_date,
        version='v30',
):
    print(f'retrieving viirs {version} data')
    url = f"https://eogdata.mines.edu/wwwdata/viirs_products/vnf/{version}/"

    ver_url = f'{version}-ez' if version == 'v30' else 'v21'

    start_dt = date(
        int(start_date[:4]),
        int(start_date[4:6]),
        int(start_date[6:8]),
    )

    end_dt = date(
        int(end_date[:4]),
        int(end_date[4:6]),
        int(end_date[6:8]),
    )

    for d in pd.date_range(start_dt, end_dt):
        print(f"    {d}")
        dl_date = d.strftime("%Y%m%d")
        f = f"VNF_npp_d{dl_date}_noaa_{ver_url}.csv.gz"

        if not Path(f"{workspace_directory}/{f}").is_file():
            print(f"    {url}/{f}")
            try:
                urllib.request.urlretrieve(
                    f"{url}/{f}",
                    f"{workspace_directory}/{f}",
                )

                with gzip.open(
                    f"{workspace_directory}/{f}",
                    'rb',
                ) as file_in:
                    with open(
                        f"{workspace_directory}/{f.replace('.csv.gz', '.csv')}",
                        'wb',
                    ) as file_out:
                        shutil.copyfileobj(file_in, file_out)

            except (HTTPError, URLError) as e:
                print(e.reason)
                continue

            time.sleep(0.25)  # politely wait before next request
