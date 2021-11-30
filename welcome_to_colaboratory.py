
from google.colab import drive
drive.mount('/content/drive') #to mount google drive

import pandas as pd
import matplotlib.pyplot as plt
import re
test = pd.read_csv('/content/drive/MyDrive/test.csv')   #to read and show data from csv
test

test.columns

import numpy as np

test.replace(to_replace=np.nan, value >= 0.5)

test.loc[test['f0'] >= 0.5, 'f0'] = 1  #one column data replaced following the given condition
print(test)
