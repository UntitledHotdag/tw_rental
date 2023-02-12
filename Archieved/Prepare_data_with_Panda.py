import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('original_data_set/2022_Rental_data_Taipe_and_New_Taipei.csv', dtype={'月租金': int})

#========For using IQR method cleaning outliers===============
#For caculating Q1,Q3 and IQR 
'''
Q1 = df['月租金'].quantile(0.25)
Q3 = df['月租金'].quantile(0.75)
IQR = Q3 - Q1
upper_limit=(Q1 - 1.5 * IQR)
lower_limit=(Q3 + 1.5 * IQR)
condition = ((df['月租金'] > lower_limit ) & (df['月租金'] < upper_limit))
'''

#========For using STD method cleaning outliers===============
#For caculating Q1,Q3 and IQR 
upper_limit=int(df['月租金'].mean()+df['月租金'].std()*3)
lower_limit=int(df['月租金'].mean()-df['月租金'].std()*3)
condition = ((df['月租金'] >lower_limit ) & (df['月租金'] < upper_limit))


#========Filtering with upper and lower condition

#check what is the upper and lower limit
#print(lower_limit,upper_limit)

#put data within lower_limit and upper_limit into filtered_df
filtered_df = df[condition]
outliers_df=df[~condition]
print(len(filtered_df.index))
filtered_df = filtered_df[df['約略地點範圍'] != '-']
print(len(filtered_df.index))




#print('or_lenght:',len(filtered_df.index))

new = filtered_df['約略地點範圍'].str.split(", ",n = 4, expand = True)

new[0]=new[0].map(lambda x: str(x)[1:])
new[3]=new[3].map(lambda x: str(x)[:-1])


#print(len(new.index))
#print(new)
#new.dropna()
#print(len(new.index))

#print(np.where(pd.isnull(new)))
#print(new[0][9345])
#print(new[0][9346])
#print(new[0][9347])

new=new.astype(float)
filtered_df['經度']=(new[0]+new[2])/2
filtered_df['緯度']=(new[1]+new[3])/2
#print('output:',len(filtered_df.index))


print(filtered_df)
#print(filtered_df.columns)
filtered_df.to_csv('output_data_set/data_with_in_upper_and_lower_bondary.csv', index=False)
#print("偏態(Skewness): {:.2f}".format(filtered_df['月租金'].skew()))
#print("峰度(Kurtosis): {:.2f}".format(filtered_df['月租金'].kurt()))

#sns.distplot(outliers_df['月租金'])
#plt.show()

#print(filtered_df)
