# -*- coding: utf-8 -*-

# -- Sheet --

#import packages
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('Arsenal xG Vs Formations.csv')

df

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.image as mpimg

# set the background color to white for all plots
plt.rcParams['figure.facecolor'] = 'white'

# sample data
x = ['4-3-3', '4-2-3-1', '3-4-2-1', '3-1-4-2', '4-1-4-1', '5-4-1']
y = [55.45, 19.56, 1.83, 0.75, 0.21, 0.03]

# create a larger figure
fig = plt.figure(figsize=(10, 10), facecolor='white')

# create a figure and axis object
fig, ax = plt.subplots()

# create the scatter plot
ax.scatter(x, y)

# set the plot title and axis labels with Menlo font
font = {'family': 'Menlo', 'size': 12}
title = ax.set_title('Arsenal xG Vs Formations [2022/2023] ', fontdict=font,fontsize=12,weight='bold', y=1.0)
title.set_color('red')  # set the color of the title to red
ax.set_xlabel('Formation', fontdict=font,fontsize=10,weight='bold')
ax.set_ylabel('xG', fontdict=font, fontsize=10,weight='bold')

# set the x-axis tick locations and labels
ax.set_xticks(range(len(x)))
ax.set_xticklabels(x)

# set the y-axis ticklocations and labels
ax.set_ylim([0, 60])
ax.set_yticks(range(0, 61, 10))
ax.set_yticklabels(range(0, 61, 10))

# add labels to each point
for i, j in zip(x, y):
    ax.text(i, j+1, str(j), horizontalalignment='left', fontsize=10)

# add lines between the points
ax.plot(x, y, color='black')

# Add a grid to the chart
ax.grid(which='major', color='gray', linestyle='--', linewidth=0.4)

# add credit
fig.text(0.5, -0.2, 'Created by (@SeifAjax04). Source of data via: [Understat.com].', color="#000000",
        transform=ax.transAxes, ha='center', fontsize=8)
fig.text(0.5, -0.3, 'seifkhaled.me', color="#000000",
        transform=ax.transAxes, ha='center', fontsize=8)

# save the plot as a PNG image in Datlore workspace
plt.savefig('ARSxG.png', dpi=300)

# show the plot
plt.show()

!pip install matplotlib==3.4.3
!wget "https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Menlo.zip"
!unzip Menlo.zip -d /usr/share/fonts/truetype/

