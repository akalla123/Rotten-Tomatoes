# -*- coding: utf-8 -*-
"""Scraping_scifi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wsFuOKeoTjqtnoMWbcg49jsVyymAcp1D
"""

import pandas as pd

action = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/action_numeric.csv")
animation = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/animation_numeric.csv")
art_foreign = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/art_foreign_numeric.csv")
classics = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/classics_numeric.csv")
comedy = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/comedy_numeric.csv")
documentary = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/documentary_numeric.csv")
drama = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/drama_numeric.csv")
horror = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/horror_numeric.csv")
kids_family = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/kids_family_numeric.csv")
mystery = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/mystery_numeric.csv")
romance = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/romance_numeric.csv")
scifi = pd.read_csv("/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/scifi_numeric.csv")

frames=[action,animation,art_foreign,classics,comedy,documentary,drama,horror,kids_family,mystery,romance,scifi]

all_movie=pd.concat(frames,ignore_index=True,axis=0)

import os
path= r'/Users/jaynanda/Desktop/Assignments/660/Project/Numeric Data/'
all_movie.to_csv(os.path.join(path, r'all_numeric_movie.csv'), index=False)