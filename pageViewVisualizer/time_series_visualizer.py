import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime as dt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", infer_datetime_format=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
#df = df.set_index('date')


def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    plt.plot(df['date'], df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar['date'].dt.month_name()
    df_bar['year'] = df['date'].dt.year

    df_bar_means = df_bar.groupby(['year', 'month']).mean()
    df_bar_means = df_bar_means.reset_index()

    # Draw bar plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    g = sns.catplot(x='year', y='value', hue='month', hue_order=months, kind="bar", data=df_bar_means)
    
    g.set(xlabel='Years', ylabel='Average Page Views')
    g._legend.remove()
    plt.legend(title='Months')


    fig = g.fig


    #fig = plt.figure()
    #plt.bar(data=df_bar_means, x=df_bar_means['year'], height=df_bar_means['value'], rot=0)
   
    #plt.xlabel('Years')
    #plt.ylabel('Average Page Views')
    #plt.legend(title='Months')
   
  



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(1, 2, figsize=(13,5))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], order=Months)

    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
