# -*- coding: utf-8 -*-


import glob
import pathlib
import multiprocessing
import os




#Define the list of stations you want to run

stations = []


#Function
def run_station(station_path):
    """
    Parameters
    
    station_path: str, path to directory of a given station,whic cointains component sac files
    
    Function which runs do_station_mfm in on all stations directories within a specified directory.
    This function will only work if the directories are in the required structure. This structure is
    Station > Event-station component files
    dir_path: str, full path to the top level directory in which the station directories are contained
    """

    os.system(f"/raid2/jam247/mfast/sample_data/do_station_mfm {station_path}")


# Main
#Function to run mfast do_station_mfm in parallel using 8
if __name__ == "__main__":
    with multiprocessing.Pool(processes=8) as pool:
        argslist = stations


        pool.map(run_station, argslist)
        
        
