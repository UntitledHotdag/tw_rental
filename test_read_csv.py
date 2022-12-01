import csv

def geostring_to_geofloat(str):
  s=str
  s=s[1:-1]
  return s


with open("./2022Q3-deduplicated.csv", 'r',encoding="utf-8") as file:
  rows = csv.reader(file)
  
  open_for_lease = []
  unknow_lease=[]
  rent_out=[]
  head=[]
  for row in rows:
    if row[0]=="重複物件數":
      head.append(row)
    if row[6]=="17" or row[6]=="11":
      if row[9]=="0":
        open_for_lease.append(row)
      elif row[9]=="1":
        unknow_lease.append(row)
      elif row[9]=="2":
        print(row[8])
        row[8]=geostring_to_geofloat(row[8])
        rent_out.append(row)
        print(row[8])
        
        break


  print(len(open_for_lease))
  print(len(unknow_lease))
  print(len(rent_out)) 

"""
with open('test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head[0])
    for rows in rent_out:
      writer.writerow(rows)
"""


