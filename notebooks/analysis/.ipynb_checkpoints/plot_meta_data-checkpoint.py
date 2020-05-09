"""Functions to plot some of the GISAIS meta data.
@author: Harald Ringbauer, 2020"""

import numpy as np
import os as os
import sys as sys
import multiprocessing as mp
import pandas as pd
import socket
import matplotlib.pyplot as plt
import matplotlib.dates as dts
from datetime import date, timedelta, time, datetime

def plot_hist(df, color_dict, plot_col="region", ec="k",
              width=0.9, title="Viral Genomes per Region",
              figsize=(3,5), savepath="", fs=12, rotation=30):
    """Plot Histogram of Values in plot_col in
    dataframe df"""
    vc = df[plot_col].value_counts()
    labels = vc.index.to_list()
    colors = [color_dict[l] for l in labels]
    ax = vc.plot(kind='bar', figsize=figsize, width=width, 
                 ec=ec, color=colors)
    for i, xtick in enumerate(ax.get_xticklabels()):
        lab = xtick.get_text()
        c = color_dict[lab]
        xtick.set_color(c)
    plt.xticks(rotation=rotation, ha='right')
    
    ### Set Text Label
    label="Sequences \nper region"
    ax.text(0.5, 0.95, label, horizontalalignment='left',      
        verticalalignment='top', transform=ax.transAxes,
       fontsize=fs)
    
    ### Save the Figure
    if len(savepath)>0:
        plt.savefig(savepath, bbox_inches = 'tight', 
                    pad_inches = 0, dpi=200)
        print(f"Saved to {savepath}")
    plt.show()


def plot_hist_dates(dates, date_last=date.today(), date_first=date(year=2020, month=2, day=15),
              fs = 14, fs_l=6, figsize=(5,6), color="gray",
              show=True):
    """Plot histogram of dates"""    
    days_back = date_last - date_first
    date_bins = [date_last -  timedelta(days=i) for i in range(days_back.days, -1, -1)]
    dates = [d.to_pydatetime().date() for d in dates]
    label = f"Sequences submitted daily\n{date_bins[0]} - {date_bins[-1]}\nTotal: {len(dates)}"

    plt.figure(figsize=figsize)
    ax = plt.gca()
    ax.hist(dates, ec="k", color=color, bins=dts.date2num(date_bins))
    ax.set_xlabel("Date", fontsize=fs)
    ax.set_ylabel("Count", fontsize=fs)
    plt.xticks(rotation=45, ha='right')
    ax.text(0.02, 0.9, label, horizontalalignment='left',      
            verticalalignment='center', transform=ax.transAxes,
           fontsize=fs)
    if show:
        plt.show()
        
def plot_cumulative_dates(dates, figsize = (4,6),
                         savepath="./figures/dumpster/covid19.png", fs=8,
                         date_last = False, days_back=60, color="k",
                         scale="lin"):
    """Plot Cumulaative Dates"""
    if not date_last:
        today = date.today()
    date_bins = [today -  timedelta(days=i) for i in range(days_back, -1, -1)]
    date_bins = [np.datetime64(d) for d in date_bins]
    counts = dates.value_counts(bins=date_bins, sort=False)
    cum_counts = np.cumsum(counts.values)
    
    label = f"Available \nSARS-CoV-2 \nGenomes \n(n={cum_counts[-1]})"
    
    plt.figure(figsize=figsize)
    ax=plt.gca()
    ax.plot(date_bins[:-1], cum_counts, "o-",
           color=color)
    ax.set_xlabel("Date", fontsize=fs)
    ax.set_ylabel("Cumulative Count", fontsize=fs)
    plt.xticks(rotation=30, ha='right')
    
    ax.text(0.1, 0.95, label, horizontalalignment='left',      
       verticalalignment='top', transform=ax.transAxes,
       fontsize=fs)
    ax.set_yscale(scale)
    
    if len(savepath)>0:
        plt.savefig(savepath, bbox_inches = 'tight', pad_inches = 0, dpi=200)
        print(f"Saved to {savepath}")
    plt.show()