# coding: utf-8



import obspy
import pandas as pd
from obspy.taup import taup_create
import numpy as np
import matplotlib.pyplot as plt
import geographiclib



taup_create.build_taup_model("/raid2/jam247/JM_Tutorials/GMT_Tutorials/BSM_Poster/askja_vmodel.tvel", output_folder = '/raid2/jam247/JM_Tutorials/GMT_Tutorials/BSM_Poster')

vmod = obspy.taup.tau.TauPyModel('/raid2/jam247/JM_Tutorials/GMT_Tutorials/BSM_Poster/askja_vmodel.npz')


def calculate_incident_angle(event, model):
    """
    Calculates the incident angle of the ray for a given event using the TauP
    toolkit wrapper provided by ObsPy. This is done using geographic
    coordinates, rather than epicentral distance angles, with the local
    velocity structure loaded into a TauP model.

    Parameters
    ----------
    event : pandas.Series object
        Contains event and station information.
    model : obspy.taup.tau.TauPModel object
        Velocity structure to be used.

    Returns
    -------
    incident_angle : float
        Angle-of-incidence of the ray with the surface.
    takeoff_angle : float
        Direction ray shoots from source, measured in degrees from vertical.
    path : list of lists
        Path taken by the ray between source and receiver.
        Columns: [rayparam, time, distance (degrees), depth, lat, lon]
    arrival : obspy.taup.tau.Arrival object
        Full arrival object for the given event.

    """

    arrival = model.get_ray_paths_geo(event["depthkm"]+0.5,
                                      event["evla"], event["evlo"],
                                      event["slat"], event["slon"],
                                      phase_list=["S"], resample=True)

    try:
        arrival[0]
    except IndexError:
        print("Cannot calculate S arrival for this event, trying s...")
        arrival = model.get_ray_paths_geo(event["depthkm"]+0.5,
                                          event["evla"], event["evlo"],
                                          event["slat"], event["slon"],
                                          phase_list=["s"], resample=True)

    #print(f"Straight-line angle-of-incidence: {event['25anginc']:5.1f}°")
    print(f"          Ray angle-of-incidence: {arrival[0].incident_angle:5.1f}°")

    incident_angle = arrival[0].incident_angle
    takeoff_angle = arrival[0].takeoff_angle
    path = arrival[0].path

    return incident_angle, takeoff_angle, path, arrival[0]
        


def append_inc_ang(dataf, model):
    """
    Function to apply 'calculate_incidence_angle()' to a dataframe of events with the correct column headers
    
    Parameters
    ----------
    dataf : pandas.DataFrame object
        Contains a dataframe containing event and station information.
    model : obspy.taup.tau.TauPModel object
        Velocity structure to be used.
    Returns
    -------
    Dataframe object which is the 'dataf' dataframe but with anginc (incidence_angle) and takeoff_ang (take-off angle) appended to each event 
    
    """
 

    frames = []
    
    for _,row in data.iterrows():
        angin,tak,x,y = calculate_incident_angle(row,vmod)
        new_frame = [angin,tak, row['1event']]
        frames.append(new_frame)

    result = pd.DataFrame(frames, columns = ('anginc', 'tak', '1event'))
    
    #pd.merge(data,result, on='1event')
    return pd.merge(data, result, on='1event')


























