'''
Visualization tools for plotting probability data

* bar : Creates a bar chart of data

'''

import matplotlib.pyplot as plt


def bar(x, y, title, xlabel, ylabel, file_name):
    '''
    Creates a bar chart
    
    Parameters
    ----------
    x : The names for the x axis
    
    y : The values for each x item
    
    title : The title of the plot
    
    xlabel : The lable for the x-axis
    
    ylabel : The label for the y-axis
    
    file_name : The name of the file to save
    
    Returns
    -------
    None, creates a bar chart in current directory
    '''
    # use a unique color for the input student bar
    colors = []
    for i in range(len(x)):
        if i==0:
            colors.append('rebeccapurple')
        else:
            colors.append('mediumpurple')
    
    fig = plt.figure()
    plt.bar(x, y, color=colors)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(file_name)
    
    return None
