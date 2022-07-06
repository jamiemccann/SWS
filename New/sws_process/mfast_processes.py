# -*- coding: utf-8 -*-

import os
import glob

def run_all_stations(dir_path):
    """
    Function which runs do_station_mfm in on all stations directories within a specified directory.
    This function will only work if the directories are in the required structure. This structure is
    Station > Event-station component files

    dir_path: str, full path to the top level directory in which the station directories are contained
    """
    for station in sorted(glob.glob(f"{dir_path}/*")):
        os.system(f"/raid2/jam247/mfast/sample_data/do_station_mfm {station}")
