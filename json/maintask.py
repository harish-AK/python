candidates = [{"Name":"Ajay","Age":23,"Designation":"IAS","Gender":"Male","Subjects":{"Maths":45,"English":42,"Social":37,"Science": 43},"Interview":56},
                {"Name":"Surya","Age":25,"Designation":"IAS","Gender":"Female","Subjects":{"Maths":47,"English":49,"Social":40,"Science": 41},"Interview":59},
                {"Name":"Surya","Age":27,"Designation":"IPS","Gender":"Female","Subjects":{"Maths":42,"English":48,"Social":38,"Science": 39},"Interview":54},
                {"Name":"Surya","Age":24,"Designation":"IAS","Gender":"Male","Subjects":{"Maths":49,"English":40,"Social":34,"Science": 40},"Interview":52},
                {"Name":"Suresh","Age":23,"Designation":"IPS","Gender":"Male","Subjects":{"Maths":44,"English":45,"Social":47,"Science": 44},"Interview":53}]

import pandas as pd
df=pd.DataFrame(candidates)
# print mark of each candidate with mark

print("Name with subjects ",df[['Name','Subjects']])

# print mark of only IPS candidates

ias = df[['Name','Subjects']].where(df['Designation']=='IAS')
print("IAS marks ",ias)

# print mark of female ips surya

female=df[['Name','Subjects']].where(df['Gender']=='Female')
print("female surya ",female)

# print only suresh mark in interview

suresh=df[df['Name']=='Suresh']
mark = suresh['Interview'].iloc[0]

print("suresh in interview ",mark)

# print interview marks of each candidate
inter=df[['Name','Interview']]
print("Interview of each candidates ",inter)

#  for a range of 1 to 100 find numbers divisible by 3 and 2
for i in range(1,100):
    if(i%2==0 and i%3==0):
        print(i)
# for a range of 10 print squares
for i in range(1,10):
    print(i*i)
# change suresh age to 26
df.loc[df['Name'] == 'Suresh', 'Age'] = 26
print(df)



samples = ["Prakash",20,"maths", "39","plays","CRICKET"]

# find length of above list
print(len(samples))
# find the index of cricket
print(samples.index('CRICKET'))
# find the type of elements in list
print(type(samples))
# add bowler in to the list
samples.append('bowler')
print(samples)
# delete 20 and 39
samples.remove("39")
print(samples)
samples.remove(20)
print("finak list ",samples)