#TO MOUNT THE FILES TO COLAB FROM GOOGLE DRIVE
from google.colab import drive
drive.mount('/content/drive')

#TO READ THE FILE MOUNTED AND SHOW DATA
import pandas as panda
test=panda.read_csv('/content/drive/MyDrive/test.csv')
test.head()
id = test["id"]
nDf = pd.Dataframe(id)

#INITIALIZING ARRAY TO HOLD AND TRANSFER VALUES TO DATAFRAME LATER
arr[]

#LOOP TO GENERATE 0'S AND 1'S
for row in id:
  arr.append(random,randint(0,1))
  test[target] = arr

#TO UPLOAD UPDATED FILE TO DRIVE FROM COLAB
test.to_csv('edited.csv', index=False)