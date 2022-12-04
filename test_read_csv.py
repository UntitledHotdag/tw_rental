import csv

def geostring_to_geofloat(str):
  s=str
  s=s[1:-1].split(", ")
  a=[]
  #print(s)
  if len(s)==4:
    a.append((float(s[0])+float(s[2]))/2)
    a.append((float(s[1])+float(s[3]))/2)
    #(25.000)
    return a
  return str

def read_scraped_csv(reference,container_list):

  with open(reference, 'r',encoding="utf-8") as file:
    rows = csv.reader(file)
    for row in rows:
      if row[6]=="17" or row[6]=="11":
        if row[9]=="2":
          if row[23]=="1" or row[23]=="2" or row[23]=="3": 
            row[8]=geostring_to_geofloat(row[8])
            if type(row[8]) == list:
              row=row[8]+row 
              container_list.append(row)
      elif row[0]=="重複物件數":
        row.insert(0,'lo')
        row.insert(0,'la')
        container_list.append(row)

def write_to_csv(destination,list):
  with open(destination, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    for rows in list:
      writer.writerow(rows)



test=[]

read_scraped_csv("./original_data_set/2022Q1-deduplicated.csv",test)
read_scraped_csv("./original_data_set/2022Q2-deduplicated.csv",test)
read_scraped_csv("./original_data_set/2022Q3-deduplicated.csv",test)
#print(test[0])
#print(test[3])
print(len(test))
write_to_csv("./output_data_set/2022_filtered_city_and_house_type_and_sale_condition.csv",test)

'''
with open("./2022Q3-deduplicated.csv", 'r',encoding="utf-8") as file:
  rows = csv.reader(file)
  
  open_for_lease = []
  unknow_lease=[]
  rent_out=[]
  head=[]
  count=0
  group=0
  el=0
  for row in rows:
    #print(count)
    if row[0]=="重複物件數":
      row.insert(0,'la')
      row.insert(0,'li')
      head.append(row)
    if row[6]=="17" or row[6]=="11":
      if row[9]=="0":
        #row[8]=geostring_to_geofloat(row[8])
        open_for_lease.append(row)
      elif row[9]=="1":
        #row[8]=geostring_to_geofloat(row[8])
        unknow_lease.append(row)
      elif row[9]=="2":
        row[8]=geostring_to_geofloat(row[8])
        print(row[8])
        if type(row[8]) == list:
         row=row[8]+row 
         rent_out.append(row)
        
        
        
        if row[23]=="1" or row[23]=="2" or row[23]=="3":
          count=count+1
        elif row[23]=="0":
          group=group+1
        else :
          el=el+1
        '''

'''   
print("個人使用房間") 
print(count)
print("團體使用房間")
print(group)
print("其他")
print(el)

        

with open('test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head[0])
    for rows in rent_out:
      writer.writerow(rows)

'''