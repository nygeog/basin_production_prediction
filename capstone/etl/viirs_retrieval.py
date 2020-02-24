from datetime import date
import pandas as pd
import urllib.request
from urllib.error import HTTPError, URLError
import gzip
import shutil


def viirs_retrieval(workspace_directory, start_date, end_date):
    url = "https://eogdata.mines.edu/wwwdata/viirs_products/vnf/v30/"

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
        print(d)
        dl_date = d.strftime("%Y%m%d")
        f = f"VNF_npp_d{dl_date}_noaa_v30-ez.csv.gz"

        print(f"{url}/{f}")

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
