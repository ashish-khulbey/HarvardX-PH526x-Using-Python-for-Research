import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering

whiskey = pd.read_csv("whiskies.txt")
whiskey["Region"] = pd.read_csv("regions.txt")
whiskey.iloc[5:10, 0:5]
flavours = whiskey.iloc[:, 2:14]
corr_flavours = pd.DataFrame.corr(flavours)
corr_flavours


plt.figure(figsize=(10,10))
plt.pcolor(corr_flavours) # pseudo color
plt.colorbar()

corr_whiskey = pd.DataFrame.corr(flavours.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whiskey) # pseudo color
plt.axis("tight")
plt.colorbar()


model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whiskey)
model.rows_
np.sum(model.rows_, axis=1)
np.sum(model.rows_, axis=0)
model.row_labels_

data = pd.Series([1,2,3,4])
data = data.iloc[[3,0,1,2]]
data = data.reset_index(drop=True)
data[0]
