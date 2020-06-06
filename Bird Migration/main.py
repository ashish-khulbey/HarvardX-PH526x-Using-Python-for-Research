import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
# !apt-get -qq install python-cartopy python3-cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

birddata = pd.read_csv("bird_tracking.csv")
# birddata.info()
# birddata.head()

# plt.figure(figsize=(7,7))
bird_names = pd.unique(birddata.bird_name)

for bird_name in bird_names:
  ix = birddata.bird_name == bird_name
  x, y = birddata.longitude[ix], birddata.latitude[ix]
  # plt.plot(x, y, label=bird_name)
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.legend(loc="lower right")


ix = birddata.bird_name=="Eric"
speed = birddata.speed_2d[ix]
# plt.hist(speed)
# np.isnan(speed).any()
# np.sum(np.isnan(speed))
ind = np.isnan(speed)
# plt.hist(speed[~ind], bins=np.linspace(0,30,20), density=True)


# birddata.speed_2d.plot(kind="hist", range=[0, 30])


date_str = birddata.date_time[0]
# datetime.datetime.strptime(date_str[:-3], "%Y-%-m-%d %H:%M:%S")

timestamps = []
for k in range(len(birddata)):
  timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

data = birddata[birddata.bird_name == "Sanne"]
print(data)
data = birddata[birddata.bird_name == "Eric"]

times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time)/ datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for i,t in enumerate(elapsed_days):
  if t < next_day:
    inds.append(i)
  else:
    daily_mean_speed.append(np.mean(data.speed_2d[inds]))
    next_day += 1
    inds = []

# plt.plot(daily_mean_speed)
# plt.xlabel("Day")
# plt.ylabel("Mean speed (m/s)")

proj = ccrs.Mercator()


plt.figure()
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
for name in bird_names:
  ix = birddata["bird_name"] == name
  x,y = birddata.longitude[ix], birddata.latitude[ix]
  ax.plot(x,y,'.',transform=ccrs.Geodetic(),label=name)
