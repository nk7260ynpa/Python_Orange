import json,datetime

fp=open("earthquake.json","r")
earthquakes=json.load(fp)

print("過去七天發生全球發生的重大地震資訊")
for eq in earthquakes["features"]:
    print("地點:{}".format(eq["properties"]["place"]))
    print("震度:{}".format(eq["properties"]["mag"]))
    et=float(eq["properties"]["time"])/1000.0
    d=datetime.datetime.fromtimestamp(et).strftime("%Y-%m-%d %H:%M:%S")
    print("時間:{}".format(d))