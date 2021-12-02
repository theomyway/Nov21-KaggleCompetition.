#MOUNTING FILE ON COLAB FROM DRIVE
from google.colab import drive
drive.mount('/content/drive')

import pandas as panda
import numpy as num
import random

#LOADING TEST CSV AND PRINTING DATA
h=panda.read_csv('/content/drive/MyDrive/test.csv')
h.head()

#CREATING NEW COLUMN AND GENERATING NEW VALUES IN THEM
test = panda.read_csv('/content/drive/MyDrive/test.csv')
test['Random Number'] = num.random.uniform(0,1, test.shape[0])
print(test)


#GENERATING 1 AND 0 IN NEW COLUMN BAESED ON RANDOM NUMBER COLUMN
for row in test['Random Number']:
    if row >= 0.5:
      test['target'] = 1
    else :
      test['target'] = 0

print(test)

#COPYING THE NEW 2 COLUMNS SO WE CAN MAKE IT CONVERT TO CSV LATER
sample = test[['id','target']].copy()
print(sample)

#CONVERTING TO CSV
sample.to_csv('sample.csv',index=False)
