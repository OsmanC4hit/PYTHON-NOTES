import sqlite3
veri=sqlite3.connect("/Users/osman/Desktop/değişkenler/yeni.db")
imlec=ogr.cursor()
imlec.execute("""SELECT *FROM ogr""")
ogr=imlec.fetchall()
for x in ogr:
    print(x)
