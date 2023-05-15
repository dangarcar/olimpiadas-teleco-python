import sqlite3
import sys
import json
import http.server
import socketserver

conn = sqlite3.connect(sys.argv[1])
conn.row_factory = sqlite3.Row
cur = conn.cursor()
res = cur.execute('SELECT * FROM Data').fetchall()
conn.commit()
conn.close()

obj = {
    "type": "FeatureCollection",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "features": []
}


for i in res:
    x = {
        "type" : "Feature",
        "properties": {},
        "geometry": {
            "type": "Point",
            "coordinates": [0]
        }
    }

    for k, v in dict(i).items():
        if(k == "Lat" or k == "Lon"):
            x["geometry"]["coordinates"].insert(0, v)
        else:
            x["properties"][k] = v
    
    obj["features"].append(x)

with open('data.json', 'w') as f:
    json.dump(obj, f, ensure_ascii=False)

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()