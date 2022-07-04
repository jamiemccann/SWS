# -*- coding: utf-8 -*-

import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplstereonet





def plot_rose(pat, title):
    """
    This function will plot a rose diagram of all results graded 'ACl', within the defined path
    
    pat = Path of file within which the .res files are located containing all information about sws event-station pairs
    
    title = str, desired title of the rose diagram plot
    """
    #sort the data into a useable list
    all_res_path = [filename for filename in glob.glob(f'{pat}**/*.fb1**.res')]
    
    frames = []
    
    for file_path in all_res_path:
        df = pd.read_csv(f'{file_path}')
        frames.append(df)
    
    result = pd.concat(frames, ignore_index=True)
    
    #filter resulyts by high grades ('ACl)
    good_results = result[result['gradeABCNR']=='ACl']
    
    #take only the fast axes
    fast_axes = list(good_results['fast'])
    
    
    #corrct the fast axes so that they are betweeb 0 and 180 (strike)
    corr_fast_axes = [i+180 for i in fast_axes if i<0 ] + [ i for i in fast_axes if i>0]
    
    
    
    
    
    
    #calculate the number of strikes in each direction
    bin_edges = np.arange(0,361,10)
    number_of_strikes, bin_edges = np.histogram(corr_fast_axes, bin_edges)
    
    
    
    
    #double this to get mirror 
    middle = (len(number_of_strikes)/2)
    
    
    max180_number_of_strikes = number_of_strikes[:int(middle)]
    number_of_strikes = np.array(list(max180_number_of_strikes)*2)
    
    
    
    #create dataframe to inspect results
    df1 = pd.DataFrame(number_of_strikes)
    df2 = pd.DataFrame(np.deg2rad(np.arange(0,360,10))) #radian bins
    df3 = pd.DataFrame(np.arange(0,360,10)) #degrees bins
    
    result = pd.concat([df1, df2, df3], axis=1, join='inner')
    
    
    
    
    #create the figure
    fig = plt.figure(figsize= (16,8))
    
    
    #add the axes
    ax = fig.add_subplot(121, projection = 'polar')
    
    ax.bar(np.deg2rad(np.arange(5,365,10)), number_of_strikes, width = np.deg2rad(10), bottom = 0.0, color ='r')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
    ax.set_rgrids(np.arange(1, number_of_strikes.max() + 1, 2), angle=0, weight= 'black')
    ax.set_title(f'{title}', y=1.10, fontsize=15)
    
    fig.tight_layout()
    fig.show()
    
