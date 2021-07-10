import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df_plot = df[['Year', 'CSIRO Adjusted Sea Level']].copy()
    plt.xticks(range(1850, 2075))
    plt.rcParams["figure.figsize"] = (10,5)

    # Create scatter plot
    df_plot.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    bestFit = np.arange(1880,2051,1).tolist()
    df_bestFit = pd.DataFrame(bestFit, columns=['Year'])
    m, b = np.polyfit(df['Year'], df['CSIRO Adjusted Sea Level'], 1)
    plt.plot(df_bestFit['Year'], m*df_bestFit['Year'] + b)

    # Create second line of best fit
    bestFit = np.arange(2000,2051,1).tolist()
    df_bestFit = pd.DataFrame(bestFit, columns=['Year'])

    df_new = df_plot.copy()
    df_new.drop(df[df['Year'] < 2000].index, inplace = True)
    
    n, c = np.polyfit(df_new['Year'], df_new['CSIRO Adjusted Sea Level'], 1)
    plt.plot(df_bestFit['Year'], n*df_bestFit['Year'] + c)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
 
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()