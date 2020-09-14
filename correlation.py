# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:40:32 2020

@author: Iris Reitsma
"""

import pandas as pd
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/reitsmairis/CS_Assignment/master/istherecorrelation.csv'
data = pd.read_csv(url, error_bad_lines=False)
display(df)

#df.plot(x =df['Year'], y='Beer consumption', kind = 'scatter')