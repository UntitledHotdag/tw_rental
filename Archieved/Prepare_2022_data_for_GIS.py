import csv
import numpy as np

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
  #1 Open CSV file
  with open(reference, 'r',encoding="utf-8") as file:
    rows = csv.reader(file)
    #iterate through rows to find interested data 
    for row in rows:
      #if the location is in Taipie or new Taipei city
      if row[6]=="17" or row[6]=="11":
      #if the property is rented out  
        if row[9]=="2":
          #if the property is either 套房、雅房、獨立套房
          if row[23]=="1" or row[23]=="2" or row[23]=="3":
            container_list.append(row)

            #row[8]=geostring_to_geofloat(row[8])
            #if type(row[8]) == list:
              #row=row[8]+row 
              #container_list.append(row)
      elif row[0]=="重複物件數":
        #row.insert(0,'lo')
        #row.insert(0,'la')
        container_list.append(row)

def write_to_csv(destination,list):
  with open(destination, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    for rows in list:
      writer.writerow(rows)



test=[]
#Reading data
read_scraped_csv("./original_data_set/2022_Rental_data.csv",test)
'''
#decide IQR bund
#print(len([int(y[14]) for y in test]))
q75, q25 = np.percentile([int(y[14]) for y in test], [75 ,25])
iqr = q75 - q25
print(iqr)
upperbond = q75+(1.5*iqr)
lowerbond = q25-(1.5*iqr)

outlier_up=0
outlier_down=0
outliers=[]
for i in test:
  if int(i[14])>upperbond:
    outlier_up+=1
    outliers.append(i)
  elif int(i[14])<lowerbond:
    outlier_down+=1

print('upper_bond:',upperbond,'lower_bond:',lowerbond)
print('Outlier_down:',outlier_down,'Outlier_up:',outlier_up)


#print(type(test[1][14]))
#print(np.mean([int(y[14]) for y in test]))

print(len(test))
print(outliers[10])
'''
write_to_csv("./original_data_set/2022_Rental_data_Taipe_and_New_Taipei.csv",test)
