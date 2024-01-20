from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pandas as pd
import datetime

client = Client("IRIS")
end_time = UTCDateTime(datetime.datetime.now())
start_time = end_time - 30 * 24 * 60 * 60  # 30 kun

latitude = 41.0  # Misol uchun
longitude = 64.0 # Misol uchun
maxradius = 10.0 # Radius gradda

# Zilzilalar haqida ma'lumotlarni so'rash
events = client.get_events(starttime=start_time, endtime=end_time,
                           latitude=latitude, longitude=longitude,
                           maxradius=maxradius, minmagnitude=0)

# Ma'lumotlarni pandas DataFrame'ga aylantirish
data = []
for event in events:
    for magnitude in event.magnitudes:
        row = {
            "Time": event.origins[0].time,
            "Latitude": event.origins[0].latitude,
            "Longitude": event.origins[0].longitude,
            "Depth": event.origins[0].depth,
            "Magnitude": magnitude.mag,
            "Magnitude Type": magnitude.magnitude_type
        }
        data.append(row)

df = pd.DataFrame(data)

# CSV fayl sifatida saqlash
df.to_csv("orta_osiyo_zilzila_ma'lumotlar.csv", index=False)

events = client.get_events(starttime=start_time, endtime=end_time,
                           latitude=latitude, longitude=longitude,
                           maxradius=maxradius, minmagnitude=0)

# Ma'lumotlarni QuakeML formatida saqlash
events.write("orta_osiyo_zilzilalar_quakeml.xml", format="QUAKEML")

