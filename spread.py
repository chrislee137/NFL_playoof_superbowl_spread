import pandas as pd
import psycopg2 as pg
import csv
import numpy as py
import matplotlib.pyplot as plt 
import seaborn as sns

spread = pd.read_csv("spreadspoke_scores.csv")

spread.head()