#Functions to create rose plot from numpy array of strikes




def sub_zero_convert(array):

    """
    Function to convert array from -90>90 range to 0>180 range
    
    
    
    """
    new_array = []
    for i in array:
        if i <0:
            new_array.append(i+180)
        else:
            new_array.append(i)

    return new_array



def rose_plotter(strikes, station_name):

    """
    Function to plot a rose diagram of a given array of strike data 

    Parameters


    strikes: numpy ndarray, the strike data which must be in a one dimensional numpy array
    
    
    
    """
    strikes = sub_zero_convert(strikes)


    
    bin_edges = np.arange(0, 371, 10)
    number_of_strikes, bin_edges = np.histogram(strikes, bin_edges)
    half = np.sum(np.split(number_of_strikes[:-1], 2), 0)
    two_halves = np.concatenate([half, half])

    fig = plt.figure(figsize=(16,8))



    ax = fig.add_subplot(122, projection='polar')

    ax.bar(np.deg2rad(np.arange(5, 365, 10)), np.sqrt(two_halves), 
        width=np.deg2rad(10), bottom=0.0, color='red', edgecolor='k')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
    #ax.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')
    ax.set_title(f'{station_name} Fast Axes', y=1.10, fontsize=15)

    
