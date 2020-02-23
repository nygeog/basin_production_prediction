from datetime import datetime
import os
import json


def get_current_time(time_format):
    if time_format == 'yyyymmdd_hhmm':
        return datetime.now().strftime('%Y%m%d_%H%M')
    elif time_format == 'yyyymmdd':
        return datetime.now().strftime('%Y%m%d')
    elif time_format == 'yyyy':
        return datetime.now().strftime('%Y')
    elif time_format == 'mmddyyyy':
        return datetime.now().strftime("%m/%d/%Y")
    elif time_format == 'yy':
        return str(int(datetime.now().strftime('%Y')) - 2000)
    else:
        return 'invalid time_format'


def create_directory(directory_folder):
    if not os.path.exists(directory_folder):
        os.makedirs(directory_folder)


def read_json(json_file):
    with open(json_file) as f:
        return json.load(f)
