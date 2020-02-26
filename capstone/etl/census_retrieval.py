import urllib.request
import zipfile
from pathlib import Path


def census_retrieval(workspace_directory):
    url = "https://www2.census.gov/geo/tiger/TIGER2017/COUNTY/"
    filename = "tl_2017_us_county.zip"

    if not Path(
        f"{workspace_directory}/{filename.replace('.zip', '.shp')}"
    ).is_file():
        print('getting us census county boundaries for basin delineation')

        urllib.request.urlretrieve(
            f"{url}/{filename}",
            f"{workspace_directory}/{filename}",
        )

        with zipfile.ZipFile(
            f"{workspace_directory}/{filename}",
            'r',
        ) as zip_ref:
            zip_ref.extractall(f"{workspace_directory}")

    return f"{workspace_directory}/{filename.replace('.zip', '.shp')}"
