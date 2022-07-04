# -*- coding: utf-8 -*-



import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
import pygmt 
import math



def map_plotter(pat):
    #sort the data into a useable list
    all_res_path = [filename for filename in glob.glob(f'{pat}**/*.fb1**.res')]

    frames = []

    for file_path in all_res_path:
        df = pd.read_csv(f'{file_path}')
        frames.append(df)

    result = pd.concat(frames) #ignore_index here when worked
    stations = pd.read_csv("/home/tebw2/STATION_FILES/QMigrate/ASKJA_stns_QM_2007-2020_ALL.txt")
    station_elevations = stations[['Name','Elevation']]

    result_elevations = pd.merge(result,station_elevations, left_on='stat', right_on='Name')




    #filter resulyts by high grades ('ACl)
    good_results = result_elevations[result_elevations['gradeABCNR']=='ACl'].copy()





    #add station-event midpoint columns to dataframe
    stlo = good_results['slon']
    evlo = good_results['evlo']
    slat = good_results['slat']
    evla = good_results['evla']
    fast_or = good_results['fast']



    good_results['midpoint_lon'] = ((stlo - evlo)/2)+evlo
    good_results['midpoint_lat'] = ((slat - evla)/2)+evla
    good_results['E_fast'] = np.sin(np.deg2rad(fast_or))
    good_results['N_fast'] = np.cos(np.deg2rad(fast_or))

    #add the eastward and northwards fast vectors to the dataframe
    #good_results['E_fast'] = math.cos(fast_or)



    #specify earthuake coordinates
    quake_longitude = good_results['evlo']
    quake_latitude = good_results['evla']

    #specify station-event midpoint coordinates
    mid_lon = good_results['midpoint_lon']
    mid_lat = good_results['midpoint_lat']

    #specify east and north vectors of fast_axes
    E_fast = good_results['E_fast']
    N_fast = good_results['N_fast']


    #create dataframe of midpoint fast_axes orientations
    fast_axes_data = good_results[['midpoint_lon', 'midpoint_lat', 'E_fast', 'N_fast']]



    #import the standard grid and colour table from GMT files
    grid = '/raid2/jam247/JM_Tutorials/GMT_Tutorials/gmt_data/IcelandDEM_20m.grd'
    gridI = '/raid2/jam247/JM_Tutorials/GMT_Tutorials/gmt_data/IcelandDEM_20mI.grd'
    cpt = '/raid2/jam247/JM_Tutorials/GMT_Tutorials/gmt_data/grey_poss.cpt'





    #create the figure
    fig = pygmt.Figure()
    fig.basemap(
    region = [-17.9,-15.5,64.7,65.5],
    projection = 'M15c',
    frame = ["x2df1d", "ya1df0.5d", "SWne"]
    )
    fig.coast(land="#666666", lakes = "skyblue", water="skyblue", resolution= 'h', area_thresh= "10/0/2 ")
    fig.coast(shorelines="0.5p,black")
    fig.grdimage(grid=grid, shading = gridI, cmap = cpt, dpi = 200)
    #fig.plot(x = quake_longitude, y = quake_latitude, style = "c0.3c", color = "green", pen = "black", label= "Earthquakes")
    fig.plot(x = stations['Longitude'], y = stations['Latitude'], style = "c0.1c", color = "blue", label ="Stations")
    #fig.plot(x = mid_lon, y= mid_lat, style = "c0.2c", color = 'red', label= "MidPoints")
    fig.velo(data = fast_axes_data, spec = 'e0.6/1/1', pen = "0.3p,red", vector ='+h0')
    fig.text( x = stations['Longitude'], y = stations['Latitude'], text = stations['Name'], yshift = "0.3c", font = "7p")


    fig.show()
