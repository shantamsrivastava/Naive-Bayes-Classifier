#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[42]:


import pandas as pd
import numpy as np
import import_ipynb
import Data
import warnings
warnings.filterwarnings('ignore')


# ## Data Handling

# In[43]:


df = pd.read_csv('Dataset.csv')
df1 = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df1.head()


# In[44]:


d = Data.data_fix(df)
train,test = Data.split(d)


# In[45]:



train = train.applymap(lambda x: x.strip() if isinstance(x, str) else x)
test = test.applymap(lambda x: x.strip() if isinstance(x, str) else x)


# ## Prior Probabilty 

# In[46]:


def prior(dataf):
    rich = 0
    poor = 0
    for i in range(len(dataf)):
        if(dataf.iloc[i,14] == '>50K'):
            rich = rich + 1
        else:
            poor = poor + 1

    rich_prior_prob = rich / (rich + poor)
    poor_prior_prob = poor / (rich + poor)
    return rich_prior_prob, poor_prior_prob


# In[47]:


prior(train)


# ## Conditional Probability of Each Feature given the Class

# In[48]:


rich = pd.DataFrame()
poor = pd.DataFrame()
for i in range(len(train)):
    if(train.iloc[i,14] == '>50K'):
        rich = rich.append(train.iloc[i],ignore_index = True)
    else:
        poor = poor.append(train.iloc[i],ignore_index = True)


# In[49]:


"""

This Entire Code Block is for individuals with an income higher than 50k

"""
age0, age1, age2, age3, age4 = 1,1,1,1,1
for i in range(len(rich)):
    if(rich.iloc[i,0] <= 20.0):
        age0 = age0 + 1
    elif(rich.iloc[i,0] <= 30.0 and rich.iloc[i,0] > 20):
        age1 = age1 + 1
    elif(rich.iloc[i,0] <= 40.0 and rich.iloc[i,0] > 30):
        age2 = age2 + 1
    elif(rich.iloc[i,0] <= 50.0 and rich.iloc[i,0] > 40):
        age3 = age3 + 1
    elif(rich.iloc[i,0] > 50):
        age4 = age4 + 1

sum = age0 + age1 + age2 + age3 + age4
r0_prob0 = age0 / sum
r0_prob1 = age1 / sum
r0_prob2 = age2 / sum
r0_prob3 = age3 / sum
r0_prob4 = age4 / sum

print("Conditional Probabilty of Age <= 20 given the income is greater than 50k is: ", r0_prob0)
print("Conditional Probabilty of 20 < Age <= 30 given the income is greater than 50k is: ", r0_prob1)
print("Conditional Probabilty of 30 < Age <= 40 given the income is greater than 50k is: ", r0_prob2)
print("Conditional Probabilty of 40 < Age <= 50 given the income is greater than 50k is: ", r0_prob3)
print("Conditional Probabilty of Age > 50 given the income is greater than 50k is: ", r0_prob4)     


# In[50]:


"""

This Entire Code Block is for individuals with an income less than or equal to 50k

"""
age0, age1, age2, age3, age4 = 1,1,1,1,1
for i in range(len(poor)):
    if(poor.iloc[i,0] <= 20.0):
        age0 = age0 + 1
    elif(poor.iloc[i,0] <= 30.0 and poor.iloc[i,0] > 20):
        age1 = age1 + 1
    elif(poor.iloc[i,0] <= 40.0 and poor.iloc[i,0] > 30):
        age2 = age2 + 1
    elif(poor.iloc[i,0] <= 50.0 and poor.iloc[i,0] > 40):
        age3 = age3 + 1
    elif(poor.iloc[i,0] > 50):
        age4 = age4 + 1

summ = age0 + age1 + age2 + age3 + age4
p0_prob0 = age0 / summ
p0_prob1 = age1 / summ
p0_prob2 = age2 / summ
p0_prob3 = age3 / summ
p0_prob4 = age4 / summ

print("Conditional Probabilty of Age <= 20 given the income is less than or equal to 50k is: ", p0_prob0)
print("Conditional Probabilty of 20 < Age <= 30 given the income is less than or equal to 50k is: ", p0_prob1)
print("Conditional Probabilty of 30 < Age <= 40 given the income is less than or equal to 50k is: ", p0_prob2)
print("Conditional Probabilty of 40 < Age <= 50 given the income is less than or equal to 50k is: ", p0_prob3)
print("Conditional Probabilty of Age > 50 given the income is less than or equal to 50k is: ", p0_prob4) 


# In[51]:


for i in range(5):
    print(f"{globals()['p0_prob' + str(i)]} ")


# In[52]:


# Define the variables with some values
a1 = 10
a2 = 20
a3 = 30

# Using f-strings
for i in range(1, 4):
    print(f"a{i} = {globals()['a'+str(i)]}")

# Using format() method
for i in range(1, 4):
    print("a{} = {}".format(i, globals()['a'+str(i)]))

# Using %-formatting
for i in range(1, 4):
    print("a%d = %d" % (i, globals()['a'+str(i)]))


# In[53]:


vari = [1,1,1,1,1,1,1,1]

for i in range(len(rich)):
    if(rich.iloc[i,1] == 'Private'):
        vari[0] = vari[0] + 1
    elif(rich.iloc[i,1] == 'Self-emp-not-inc'):
        vari[1] = vari[1] + 1
    elif(rich.iloc[i,1] == 'Self-emp-inc'):
        vari[2] = vari[2] + 1
    elif(rich.iloc[i,1] == 'Federal-gov'):
        vari[3] = vari[3] + 1
    elif(rich.iloc[i,1] == 'Local-gov'):
        vari[4] = vari[4] + 1
    elif(rich.iloc[i,1] == 'State-gov'):
        vari[5] = vari[5] + 1
    elif(rich.iloc[i,1] == 'Without-pay'):
        vari[6] = vari[6] + 1
    elif(rich.iloc[i,1] == 'Never-worked'):
        vari[7] = vari[7] + 1

x = 0
for i in range(len(vari)):
    x = x + vari[i]

r1_prob0 = vari[0]/x
r1_prob1 = vari[1]/x
r1_prob2 = vari[2]/x
r1_prob3 = vari[3]/x
r1_prob4 = vari[4]/x
r1_prob5 = vari[5]/x
r1_prob6 = vari[6]/x
r1_prob7 = vari[7]/x

print("Conditional Probabilty of Workclass = Private given the income is greater than 50k is: ", r1_prob0)
print("Conditional Probabilty of Workclass = Self-emp-not-inc given the income is greater than 50k is: ", r1_prob1)
print("Conditional Probabilty of Workclass = Self-emp-inc given the income is greater than 50k is: ", r1_prob2)
print("Conditional Probabilty of Workclass = Federal-gov given the income is greater than 50k is: ", r1_prob3)
print("Conditional Probabilty of Workclass = Local-gov given the income is greater than 50k is: ", r1_prob4)  
print("Conditional Probabilty of Workclass = State-gov given the income is greater than 50k is: ", r1_prob5)
print("Conditional Probabilty of Workclass = Without-pay given the income is greater than 50k is: ", r1_prob6)
print("Conditional Probabilty of Workclass = Never-worked given the income is greater than 50k is: ", r1_prob7)


# In[54]:


job_counts = poor.iloc[:, 1].value_counts()
job = job_counts.tolist()
job_names_list = job_counts.index.tolist()

x = 0
for i in range(len(job)):
    x = x + job[i]

job = [x + 1 for x in job]

p1_prob0 = job[0]/x
p1_prob1 = job[1]/x
p1_prob2 = job[5]/x
p1_prob3 = job[4]/x
p1_prob4 = job[2]/x
p1_prob5 = job[3]/x
p1_prob6 = job[6]/x
p1_prob7 = 1/x

print("Conditional Probabilty of Workclass = Private given the income is less than or equal to 50k is: ", p1_prob0)
print("Conditional Probabilty of Workclass = Self-emp-not-inc given the income is less than or equal to 50k is: ", p1_prob1)
print("Conditional Probabilty of Workclass = Self-emp-inc given the income is less than or equal to 50k is: ", p1_prob2)
print("Conditional Probabilty of Workclass = Federal-gov given the income is less than or equal to 50k is: ", p1_prob3)
print("Conditional Probabilty of Workclass = Local-gov given the income is less than or equal to 50k is: ", p1_prob4)  
print("Conditional Probabilty of Workclass = State-gov given the income is less than or equal to 50k is: ", p1_prob5)
print("Conditional Probabilty of Workclass = Without-pay given the income is less than or equal to 50k is: ", p1_prob6)
print("Conditional Probabilty of Workclass = Never-worked given the income is less than or equal to 50k is: ", p1_prob7)


# In[55]:


edu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

edu = [x + 1 for x in edu]

for i in range(len(rich)):
    if(rich.iloc[i,3] == 'Bachelors'):
        edu[0] = edu[0] + 1
    elif(rich.iloc[i,3] == 'Some-college'):
        edu[1] = edu[1] + 1
    elif(rich.iloc[i,3] == '11th'):
        edu[2] = edu[2] + 1
    elif(rich.iloc[i,3] == 'HS-grad'):
        edu[3] = edu[3] + 1
    elif(rich.iloc[i,3] == 'Prof-school'):
        edu[4] = edu[4] + 1
    elif(rich.iloc[i,3] == 'Assoc-acdm'):
        edu[5] = edu[5] + 1
    elif(rich.iloc[i,3] == 'Assoc-voc'):
        edu[6] = edu[6] + 1
    elif(rich.iloc[i,3] == '9th'):
        edu[7] = edu[7] + 1
    elif(rich.iloc[i,3] == '7th-8th'):
        edu[8] = edu[8] + 1
    elif(rich.iloc[i,3] == '12th'):
        edu[9] = edu[9] + 1
    elif(rich.iloc[i,3] == 'Masters'):
        edu[10] = edu[10] + 1
    elif(rich.iloc[i,3] == '1st-4th'):
        edu[11] = edu[11] + 1
    elif(rich.iloc[i,3] == '10th'):
        edu[12] = edu[12] + 1
    elif(rich.iloc[i,3] == 'Doctorate'):
        edu[13] = edu[13] + 1
    elif(rich.iloc[i,3] == '5th-6th'):
        edu[14] = edu[14] + 1
    elif(rich.iloc[i,3] == 'Preschool'):
        edu[15] = edu[15] + 1

x = 0
for i in range(len(edu)):
    x = x + edu[i]

r3_prob0 = edu[0]/x
r3_prob1 = edu[1]/x
r3_prob2 = edu[2]/x
r3_prob3 = edu[3]/x
r3_prob4 = edu[4]/x
r3_prob5 = edu[5]/x
r3_prob6 = edu[6]/x
r3_prob7 = edu[7]/x
r3_prob8 = edu[8]/x
r3_prob9 = edu[9]/x
r3_prob10 = edu[10]/x
r3_prob11 = edu[11]/x
r3_prob12 = edu[12]/x
r3_prob13 = edu[13]/x
r3_prob14 = edu[14]/x
r3_prob15 = edu[15]/x

print("Conditional Probabilty of Education = Bachelors given the income is greater than 50k is: ", r3_prob0)
print("Conditional Probabilty of Education = Some-college given the income is greater than 50k is: ", r3_prob1)
print("Conditional Probabilty of Education = 11th given the income is greater than 50k is: ", r3_prob2)
print("Conditional Probabilty of Education = HS-grad given the income is greater than 50k is: ", r3_prob3)
print("Conditional Probabilty of Education = Prof-school given the income is greater than 50k is: ", r3_prob4)
print("Conditional Probabilty of Education = Assoc-acdm given the income is greater than 50k is: ", r3_prob5)
print("Conditional Probabilty of Education = Assoc-voc given the income is greater than 50k is: ", r3_prob6)
print("Conditional Probabilty of Education = 9th given the income is greater than 50k is: ", r3_prob7)
print("Conditional Probabilty of Education = 7th-8th given the income is greater than 50k is: ", r3_prob8)
print("Conditional Probabilty of Education = 12th given the income is greater than 50k is: ", r3_prob9)
print("Conditional Probabilty of Education = Masters given the income is greater than 50k is: ", r3_prob10)
print("Conditional Probabilty of Education = 1st-4th given the income is greater than 50k is: ", r3_prob11)
print("Conditional Probabilty of Education = 10th given the income is greater than 50k is: ", r3_prob12)
print("Conditional Probabilty of Education = Doctorate given the income is greater than 50k is: ", r3_prob13)
print("Conditional Probabilty of Education = 5th-6th given the income is greater than 50k is: ", r3_prob14)
print("Conditional Probabilty of Education = Preschool given the income is greater than 50k is: ", r3_prob15)


# In[56]:


edu_counts = poor.iloc[:,3].value_counts()
education = edu_counts.tolist()
edu_names_list = edu_counts.index.tolist()

x = 0
for i in range(len(education)):
    x = x + education[i]

education = [x + 1 for x in education]

p3_prob0 = education[2]/x
p3_prob1 = education[1]/x
p3_prob2 = education[3]/x
p3_prob3 = education[0]/x
p3_prob4 = education[12]/x
p3_prob5 = education[6]/x
p3_prob6 = education[4]/x
p3_prob7 = education[9]/x
p3_prob8 = education[8]/x
p3_prob9 = education[10]/x
p3_prob10 = education[7]/x
p3_prob11 = education[13]/x
p3_prob12 = education[5]/x
p3_prob13 = education[14]/x
p3_prob14 = education[11]/x
p3_prob15 = education[15]/x

print("Conditional Probabilty of Education = Bachelors given the income is less than or equal to 50k is: ", p3_prob0)
print("Conditional Probabilty of Education = Some-college given the income is less than or equal to 50k is: ", p3_prob1)
print("Conditional Probabilty of Education = 11th given the income is less than or equal to 50k is: ", p3_prob2)
print("Conditional Probabilty of Education = HS-grad given the income is less than or equal to 50k is: ", p3_prob3)
print("Conditional Probabilty of Education = Prof-school given the income is less than or equal to 50k is: ", p3_prob4)
print("Conditional Probabilty of Education = Assoc-acdm given the income is less than or equal to 50k is: ", p3_prob5)
print("Conditional Probabilty of Education = Assoc-voc given the income is less than or equal to 50k is: ", p3_prob6)
print("Conditional Probabilty of Education = 9th given the income is less than or equal to 50k is: ", p3_prob7)
print("Conditional Probabilty of Education = 7th-8th given the income is less than or equal to 50k is: ", p3_prob8)
print("Conditional Probabilty of Education = 12th given the income is less than or equal to 50k is: ", p3_prob9)
print("Conditional Probabilty of Education = Masters given the income is less than or equal to 50k is: ", p3_prob10)
print("Conditional Probabilty of Education = 1st-4th given the income is less than or equal to 50k is: ", p3_prob11)
print("Conditional Probabilty of Education = 10th given the income is less than or equal to 50k is: ", p3_prob12)
print("Conditional Probabilty of Education = Doctorate given the income is less than or equal to 50k is: ", p3_prob13)
print("Conditional Probabilty of Education = 5th-6th given the income is less than or equal to 50k is: ", p3_prob14)
print("Conditional Probabilty of Education = Preschool given the income is less than or equal to 50k is: ", p3_prob15)


# In[57]:


e0, e1, e2, e3 = 1,1,1,1
for i in range(len(rich)):
    if(rich.iloc[i,4] <= 4):
        e0 = e0 + 1
    elif(rich.iloc[i,4] <= 8 and rich.iloc[i,4] > 4):
        e1 = e1 + 1
    elif(rich.iloc[i,4] <= 12 and rich.iloc[i,4] > 8):
        e2 = e2 + 1
    elif(rich.iloc[i,4] > 12):
        e3 = e3 + 1

sum = e0 + e1 + e2 + e3 
r4_prob0 = e0 / sum
r4_prob1 = e1 / sum
r4_prob2 = e2 / sum
r4_prob3 = e3 / sum


print("Conditional Probabilty of edu <= 4 given the income is greater than 50k is: ", r4_prob0)
print("Conditional Probabilty of 4 < edu <= 8 given the income is greater than 50k is: ", r4_prob1)
print("Conditional Probabilty of 8 < edu <= 12 given the income is greater than 50k is: ", r4_prob2)
print("Conditional Probabilty of edu > 12 given the income is greater than 50k is: ", r4_prob3)


# In[58]:


e0, e1, e2, e3 = 1,1,1,1
for i in range(len(poor)):
    if(poor.iloc[i,4] <= 4):
        e0 = e0 + 1
    elif(poor.iloc[i,4] <= 8 and poor.iloc[i,4] > 4):
        e1 = e1 + 1
    elif(poor.iloc[i,4] <= 12 and poor.iloc[i,4] > 8):
        e2 = e2 + 1
    elif(poor.iloc[i,4] > 12):
        e3 = e3 + 1

sum = e0 + e1 + e2 + e3 
p4_prob0 = e0 / sum
p4_prob1 = e1 / sum
p4_prob2 = e2 / sum
p4_prob3 = e3 / sum


print("Conditional Probabilty of edu <= 4 given the income is less than or equal to 50k is: ", p4_prob0)
print("Conditional Probabilty of 4 < edu <= 8 given the income is less than or equal to 50k is: ", p4_prob1)
print("Conditional Probabilty of 8 < edu <= 12 given the income is less than or equal to 50k is: ", p4_prob2)
print("Conditional Probabilty of edu > 12 given the income is less than or equal to 50k is: ", p4_prob3)


# In[59]:


rel = [0,0,0,0,0,0,0]

rel = [x + 1 for x in rel]

for i in range(len(rich)):
    if(rich.iloc[i,5] == 'Married-civ-spouse'):
        rel[0] = rel[0] + 1
    elif(rich.iloc[i,5] == 'Divorced'):
        rel[1] = rel[1] + 1
    elif(rich.iloc[i,5] == 'Never-married'):
        rel[2] = rel[2] + 1
    elif(rich.iloc[i,5] == 'Separated'):
        rel[3] = rel[3] + 1
    elif(rich.iloc[i,5] == 'Widowed'):
        rel[4] = rel[4] + 1
    elif(rich.iloc[i,5] == 'Married-spouse-absent'):
        rel[5] = rel[5] + 1
    elif(rich.iloc[i,5] == 'Married-AF-spouse'):
        rel[6] = rel[6] + 1

x = 0
for i in range(len(rel)):
    x = x + rel[i]

r5_prob0 = rel[0]/x
r5_prob1 = rel[1]/x
r5_prob2 = rel[2]/x
r5_prob3 = rel[3]/x
r5_prob4 = rel[4]/x
r5_prob5 = rel[5]/x
r5_prob6 = rel[6]/x


print("Conditional Probabilty of Marital-Status = Married-civ-spouse given the income is greater than 50k is: ", r5_prob0)
print("Conditional Probabilty of Marital-Status = Divorced given the income is greater than 50k is: ", r5_prob1)
print("Conditional Probabilty of Marital-Status = Never-married given the income is greater than 50k is: ", r5_prob2)
print("Conditional Probabilty of Marital-Status = Separated given the income is greater than 50k is: ", r5_prob3)
print("Conditional Probabilty of Marital-Status = Widowed given the income is greater than 50k is: ", r5_prob4)  
print("Conditional Probabilty of Marital-Status = Married-spouse-absent given the income is greater than 50k is: ", r5_prob5)
print("Conditional Probabilty of Marital-Status = Married-AF-spouse given the income is greater than 50k is: ", r5_prob6)


# In[60]:


marriage_counts = poor.iloc[:,5].value_counts()
marr = marriage_counts.tolist()
marriage_names_list = marriage_counts.index.tolist()

x = 0
for i in range(len(marr)):
    x = x + marr[i]

marr = [x + 1 for x in marr]

p5_prob0 = marr[1]/x
p5_prob1 = marr[2]/x
p5_prob2 = marr[0]/x
p5_prob3 = marr[3]/x
p5_prob4 = marr[4]/x
p5_prob5 = marr[5]/x
p5_prob6 = marr[6]/x

print("Conditional Probabilty of Marital-Status = Married-civ-spouse given the income is less than or equal to 50k is: ", p5_prob0)
print("Conditional Probabilty of Marital-Status = Divorced given the income is less than or equal to 50k is: ", p5_prob1)
print("Conditional Probabilty of Marital-Status = Never-married given the income is less than or equal to 50k is: ", p5_prob2)
print("Conditional Probabilty of Marital-Status = Separated given the income is less than or equal to 50k is: ", p5_prob3)
print("Conditional Probabilty of Marital-Status = Widowed given the income is less than or equal to 50k is: ", p5_prob4)
print("Conditional Probabilty of Marital-Status = Married-spouse-absent given the income is less than or equal to 50k is: ", p5_prob5)
print("Conditional Probabilty of Marital-Status = Married-AF-spouse given the income is less than or equal to 50k is: ", p5_prob6)


# In[61]:


occ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

occ = [x + 1 for x in occ]

for i in range(len(rich)):
    if(rich.iloc[i,6] == 'Tech-support'):
        occ[0] = occ[0] + 1
    elif(rich.iloc[i,6] == 'Craft-repair'):
        occ[1] = occ[1] + 1
    elif(rich.iloc[i,6] == 'Other-service'):
        occ[2] = occ[2] + 1
    elif(rich.iloc[i,6] == 'Sales'):
        occ[3] = occ[3] + 1
    elif(rich.iloc[i,6] == 'Exec-managerial'):
        occ[4] = occ[4] + 1
    elif(rich.iloc[i,6] == 'Prof-specialty'):
        occ[5] = occ[5] + 1
    elif(rich.iloc[i,6] == 'Handlers-cleaners'):
        occ[6] = occ[6] + 1
    elif(rich.iloc[i,6] == 'Machine-op-inspct'):
        occ[7] = occ[7] + 1
    elif(rich.iloc[i,6] == 'Adm-clerical'):
        occ[8] = occ[8] + 1
    elif(rich.iloc[i,6] == 'Farming-fishing'):
        occ[9] = occ[9] + 1
    elif(rich.iloc[i,6] == 'Transport-moving'):
        occ[10] = occ[10] + 1
    elif(rich.iloc[i,6] == 'Priv-house-serv'):
        occ[11] = occ[11] + 1
    elif(rich.iloc[i,6] == 'Protective-serv'):
        occ[12] = occ[12] + 1
    elif(rich.iloc[i,6] == 'Armed-Forces'):
        occ[13] = occ[13] + 1

x = 0
for i in range(len(occ)):
    x = x + occ[i]

r6_prob0 = occ[0]/x
r6_prob1 = occ[1]/x
r6_prob2 = occ[2]/x
r6_prob3 = occ[3]/x
r6_prob4 = occ[4]/x
r6_prob5 = occ[5]/x
r6_prob6 = occ[6]/x
r6_prob7 = occ[7]/x
r6_prob8 = occ[8]/x
r6_prob9 = occ[9]/x
r6_prob10 = occ[10]/x
r6_prob11 = occ[11]/x
r6_prob12 = occ[12]/x
r6_prob13 = occ[13]/x


# In[62]:


occ_counts = poor.iloc[:,6].value_counts()
occu = occ_counts.tolist()
occ_names_list = occ_counts.index.tolist()

x = 0
for i in range(len(occu)):
    x = x + occu[i]

occu = [x + 1 for x in occu]

p6_prob0 = occu[10]/x
p6_prob1 = occu[1]/x
p6_prob2 = occu[2]/x
p6_prob3 = occu[3]/x
p6_prob4 = occu[5]/x
p6_prob5 = occu[4]/x
p6_prob6 = occu[8]/x
p6_prob7 = occu[6]/x
p6_prob8 = occu[0]/x
p6_prob9 = occu[9]/x
p6_prob10 = occu[7]/x
p6_prob11 = occu[12]/x
p6_prob12 = occu[11]/x
p6_prob13 = occu[13]/x


# In[63]:


rel = [0,0,0,0,0,0] 

rel = [x + 1 for x in rel]

for i in range(len(rich)):
    if(rich.iloc[i,7] == 'Wife'):
        rel[0] = rel[0] + 1
    elif(rich.iloc[i,7] == 'Own-child'):
        rel[1] = rel[1] + 1
    elif(rich.iloc[i,7] == 'Husband'):
        rel[2] = rel[2] + 1
    elif(rich.iloc[i,7] == 'Not-in-family'):
        rel[3] = rel[3] + 1
    elif(rich.iloc[i,7] == 'Other-relative'):
        rel[4] = rel[4] + 1
    elif(rich.iloc[i,7] == 'Unmarried'):
        rel[5] = rel[5] + 1

x = 0
for i in range(len(rel)):
    x = x + rel[i]

r7_prob0 = rel[0]/x
r7_prob1 = rel[1]/x
r7_prob2 = rel[2]/x
r7_prob3 = rel[3]/x
r7_prob4 = rel[4]/x
r7_prob5 = rel[5]/x


# In[64]:


rel_counts = poor.iloc[:,7].value_counts()
relations = rel_counts.tolist()
rel_names_list = rel_counts.index.tolist()

x = 0
for i in range(len(relations)):
    x = x + relations[i]

relations = [x + 1 for x in relations]

p7_prob0 = relations[5]/x
p7_prob1 = relations[2]/x
p7_prob2 = relations[1]/x
p7_prob3 = relations[0]/x
p7_prob4 = relations[4]/x
p7_prob5 = relations[3]/x


# In[65]:


race = [0,0,0,0,0]

race = [x + 1 for x in race]

for i in range(len(rich)):
    if(rich.iloc[i,8] == 'White'):
        race[0] = race[0] + 1
    elif(rich.iloc[i,8] == 'Asian-Pac-Islander'):
        race[1] = race[1] + 1
    elif(rich.iloc[i,8] == 'Amer-Indian-Eskimo'):
        race[2] = race[2] + 1
    elif(rich.iloc[i,8] == 'Other'):
        race[3] = race[3] + 1
    elif(rich.iloc[i,8] == 'Black'):
        race[4] = race[4] + 1

x = 0
for i in range(len(race)):
    x = x + race[i]

r8_prob0 = race[0]/x
r8_prob1 = race[1]/x
r8_prob2 = race[2]/x
r8_prob3 = race[3]/x
r8_prob4 = race[4]/x

r8_prob0, r8_prob1, r8_prob2, r8_prob3, r8_prob4


# In[66]:


race_counts = poor.iloc[:,8].value_counts()
prace = race_counts.tolist()
race_names_list = race_counts.index.tolist()

x = 0
for i in range(len(prace)):
    x = x + prace[i]

prace = [x + 1 for x in prace]

p8_prob0 = prace[0]/x
p8_prob1 = prace[2]/x
p8_prob2 = prace[3]/x
p8_prob3 = prace[4]/x
p8_prob4 = prace[1]/x

p8_prob0, p8_prob1, p8_prob2, p8_prob3, p8_prob4


# In[67]:


sex  = [1,1]

for i in range(len(rich)):
    if(rich.iloc[i,9] == 'Male'):
        sex[0] = sex[0] + 1
    elif(rich.iloc[i,9] == 'Female'):
        sex[1] = sex[1] + 1

x = 0
for i in range(len(sex)):
    x = x + sex[i]

r9_prob0 = sex[0]/x
r9_prob1 = sex[1]/x

r9_prob0, r1_prob1


# In[68]:


sex_counts = poor.iloc[:,9].value_counts()
psex = sex_counts.tolist()
sex_names_list = sex_counts.index.tolist()

x = 0
for i in range(len(psex)):
    x = x + psex[i]

psex = [x + 1 for x in psex]

p9_prob0 = psex[0]/x
p9_prob1 = psex[1]/x

p9_prob0, p9_prob1


# In[69]:


gain  = [1,1]

for i in range(len(rich)):
    if(rich.iloc[i,10] == 0):
        gain[0] = gain[0] + 1
    elif(rich.iloc[i,10] != 0):
        gain[1] = gain[1] + 1

x = 0
for i in range(len(gain)):
    x = x + gain[i]

r10_prob0 = gain[0]/x
r10_prob1 = gain[1]/x

r10_prob0, r10_prob1


# In[70]:


pgain  = [1,1]

for i in range(len(poor)):
    if(poor.iloc[i,10] == 0):
        pgain[0] = pgain[0] + 1
    elif(poor.iloc[i,10] != 0):
        pgain[1] = pgain[1] + 1

x = 0
for i in range(len(pgain)):
    x = x + pgain[i]

p10_prob0 = pgain[0]/x
p10_prob1 = pgain[1]/x

p10_prob0, p10_prob1


# In[71]:


loss  = [1,1]

for i in range(len(rich)):
    if(rich.iloc[i,11] == 0):
        loss[0] = loss[0] + 1
    elif(rich.iloc[i,11] != 0):
        loss[1] = loss[1] + 1

x = 0
for i in range(len(loss)):
    x = x + loss[i]

r11_prob0 = loss[0]/x
r11_prob1 = loss[1]/x

r11_prob0, r11_prob1


# In[72]:


ploss  = [1,1]

for i in range(len(poor)):
    if(poor.iloc[i,11] == 0):
        ploss[0] = ploss[0] + 1
    elif(poor.iloc[i,11] != 0):
        ploss[1] = ploss[1] + 1

x = 0
for i in range(len(ploss)):
    x = x + ploss[i]

p11_prob0 = ploss[0]/x
p11_prob1 = ploss[1]/x

p11_prob0, p11_prob1


# In[73]:


work0, work1, work2, work3, work4 = 1,1,1,1,1
for i in range(len(rich)):
    if(rich.iloc[i,12] <= 20.0):
        work0 = work0 + 1
    elif(rich.iloc[i,12] <= 40.0 and rich.iloc[i,12] > 20):
        work1 = work1 + 1
    elif(rich.iloc[i,12] <= 60.0 and rich.iloc[i,12] > 40):
        work2 = work2 + 1
    elif(rich.iloc[i,12] <= 80.0 and rich.iloc[i,12] > 60):
        work3 = work3 + 1
    elif(rich.iloc[i,12] > 80):
        work4 = work4 + 1

sum = work0 + work1 + work2 + work3 + work4
r12_prob0 = work0 / sum
r12_prob1 = work1 / sum
r12_prob2 = work2 / sum
r12_prob3 = work3 / sum
r12_prob4 = work4 / sum

print("Conditional Probabilty of working hours <= 20 given the income is greater than 50k is: ", r12_prob0)
print("Conditional Probabilty of 20 < working hours <= 40 given the income is greater than 50k is: ", r12_prob1)
print("Conditional Probabilty of 40 < working hours <= 60 given the income is greater than 50k is: ", r12_prob2)
print("Conditional Probabilty of 60 < working hours <= 80 given the income is greater than 50k is: ", r12_prob3)
print("Conditional Probabilty of working hours > 80 given the income is greater than 50k is: ", r12_prob4)


# In[74]:


work0, work1, work2, work3, work4 = 1,1,1,1,1
for i in range(len(poor)):
    if(poor.iloc[i,12] <= 20.0):
        work0 = work0 + 1
    elif(poor.iloc[i,12] <= 40.0 and poor.iloc[i,12] > 20):
        work1 = work1 + 1
    elif(poor.iloc[i,12] <= 60.0 and poor.iloc[i,12] > 40):
        work2 = work2 + 1
    elif(poor.iloc[i,12] <= 80.0 and poor.iloc[i,12] > 60):
        work3 = work3 + 1
    elif(poor.iloc[i,12] > 80):
        work4 = work4 + 1

sum = work0 + work1 + work2 + work3 + work4
p12_prob0 = work0 / sum
p12_prob1 = work1 / sum
p12_prob2 = work2 / sum
p12_prob3 = work3 / sum
p12_prob4 = work4 / sum

print("Conditional Probabilty of working hours <= 20 given the income is less than or equal to 50k is: ", p12_prob0)
print("Conditional Probabilty of 20 < working hours <= 40 given the income is less than or equal to 50k is: ", p12_prob1)
print("Conditional Probabilty of 40 < working hours <= 60 given the income is less than or equal to 50k is: ", p12_prob2)
print("Conditional Probabilty of 60 < working hours <= 80 given the income is less than or equal to 50k is: ", p12_prob3)
print("Conditional Probabilty of working hours > 80 given the income is less than or equal to 50k is: ", p12_prob4)


# In[75]:



country_counts = rich.iloc[:, 13].value_counts()
country_counts_list = country_counts.tolist()
country_counts_list = [x + 1 for x in country_counts_list]
country_names_list = country_counts.index.tolist()


country_names = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)',
                 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy',
                 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic',
                 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland',
                 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']


total_count = 0
for count in country_counts_list:
    total_count += count


rcountry_probabilities_list = []

for name in country_names:
    if name in country_names_list:

        index = country_names_list.index(name)
    
        count = country_counts_list[index]
    
        probability = count / total_count
        rcountry_probabilities_list.append(probability)
    else:

        rcountry_probabilities_list.append(0)


print("Country counts:", country_counts_list)
print("Country probabilities:", rcountry_probabilities_list)


# In[76]:



country_counts = poor.iloc[:, 13].value_counts()
pcountry_counts_list = country_counts.tolist()
pcountry_counts_list = [x + 1 for x in pcountry_counts_list]
country_names_list = country_counts.index.tolist()


country_names = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)',
                 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy',
                 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic',
                 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland',
                 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']


total_count = 0
for count in pcountry_counts_list:
    total_count += count


pcountry_probabilities_list = []


for name in country_names:
    if name in country_names_list:
 
        index = country_names_list.index(name)
      
        count = pcountry_counts_list[index]
     
        probability = count / total_count
        pcountry_probabilities_list.append(probability)
    else:
 
        pcountry_probabilities_list.append(0)


print("Country counts:", pcountry_counts_list)
print("Country probabilities:", pcountry_probabilities_list)


# In[77]:


ans = test['Salary'].tolist()
r_p = prior(test)


# In[78]:


ques = []
count = 0
for i in range(len(test)):
    response = []
    if(test.iloc[i,0] <= 20.0):
        response.append(0)
    elif(test.iloc[i,0] <= 30.0 and test.iloc[i,0] > 20):
        response.append(1)
    elif(test.iloc[i,0] <= 40.0 and test.iloc[i,0] > 30):
        response.append(2)
    elif(test.iloc[i,0] <= 50.0 and test.iloc[i,0] > 40):
        response.append(3)
    elif(test.iloc[i,0] > 50):
        response.append(4)

    if(test.iloc[i,1] == 'Private'):
        response.append(0)
    elif(test.iloc[i,1] == 'Self-emp-not-inc'):
        response.append(1)
    elif(test.iloc[i,1] == 'Self-emp-inc'):
        response.append(2)
    elif(test.iloc[i,1] == 'Federal-gov'):
        response.append(3)
    elif(test.iloc[i,1] == 'Local-gov'):
        response.append(4)
    elif(test.iloc[i,1] == 'State-gov'):
        response.append(5)
    elif(test.iloc[i,1] == 'Without-pay'):
        response.append(6)
    elif(test.iloc[i,1] == 'Never-worked'):
        response.append(7)

    response.append(1)

    if(test.iloc[i,3] == 'Bachelors'):
        response.append(0)
    elif(test.iloc[i,3] == 'Some-college'):
        response.append(1)
    elif(test.iloc[i,3] == '11th'):
        response.append(2)
    elif(test.iloc[i,3] == 'HS-grad'):
        response.append(3)
    elif(test.iloc[i,3] == 'Prof-school'):
        response.append(4)
    elif(test.iloc[i,3] == 'Assoc-acdm'):
        response.append(5)
    elif(test.iloc[i,3] == 'Assoc-voc'):
        response.append(6)
    elif(test.iloc[i,3] == '9th'):
        response.append(7)
    elif(test.iloc[i,3] == '7th-8th'):
        response.append(8)
    elif(test.iloc[i,3] == '12th'):
        response.append(9)
    elif(test.iloc[i,3] == 'Masters'):
        response.append(10)
    elif(test.iloc[i,3] == '1st-4th'):
        response.append(11)
    elif(test.iloc[i,3] == '10th'):
        response.append(12)
    elif(test.iloc[i,3] == 'Doctorate'):
        response.append(13)
    elif(test.iloc[i,3] == '5th-6th'):
        response.append(14)
    elif(test.iloc[i,3] == 'Preschool'):
        response.append(15)

    if(test.iloc[i,4] <= 4):
        response.append(0)
    elif(test.iloc[i,4] <= 8 and test.iloc[i,4] > 4):
        response.append(1)
    elif(test.iloc[i,4] <= 12 and test.iloc[i,4] > 8):
        response.append(2)
    elif(test.iloc[i,4] > 12):
        response.append(3)

    if(test.iloc[i,5] == 'Married-civ-spouse'):
        response.append(0)
    elif(test.iloc[i,5] == 'Divorced'):
        response.append(1)
    elif(test.iloc[i,5] == 'Never-married'):
        response.append(2)
    elif(test.iloc[i,5] == 'Separated'):
        response.append(3)
    elif(test.iloc[i,5] == 'Widowed'):
        response.append(4)
    elif(test.iloc[i,5] == 'Married-spouse-absent'):
        response.append(5)
    elif(test.iloc[i,5] == 'Married-AF-spouse'):
        response.append(6)

    if(test.iloc[i,6] == 'Tech-support'):
        response.append(0)
    elif(test.iloc[i,6] == 'Craft-repair'):
        response.append(1)
    elif(test.iloc[i,6] == 'Other-service'):
        response.append(2)
    elif(test.iloc[i,6] == 'Sales'):
        response.append(3)
    elif(test.iloc[i,6] == 'Exec-managerial'):
        response.append(4)
    elif(test.iloc[i,6] == 'Prof-specialty'):
        response.append(5)
    elif(test.iloc[i,6] == 'Handlers-cleaners'):
        response.append(6)
    elif(test.iloc[i,6] == 'Machine-op-inspct'):
        response.append(7)
    elif(test.iloc[i,6] == 'Adm-clerical'):
        response.append(8)
    elif(test.iloc[i,6] == 'Farming-fishing'):
        response.append(9)
    elif(test.iloc[i,6] == 'Transport-moving'):
        response.append(10)
    elif(test.iloc[i,6] == 'Priv-house-serv'):
        response.append(11)
    elif(test.iloc[i,6] == 'Protective-serv'):
        response.append(12)
    elif(test.iloc[i,6] == 'Armed-Forces'):
        response.append(13)

    if(test.iloc[i,7] == 'Wife'):
        response.append(0)
    elif(test.iloc[i,7] == 'Own-child'):
        response.append(1)
    elif(test.iloc[i,7] == 'Husband'):
        response.append(2)
    elif(test.iloc[i,7] == 'Not-in-family'):
        response.append(3)
    elif(test.iloc[i,7] == 'Other-relative'):
        response.append(4)
    elif(test.iloc[i,7] == 'Unmarried'):
        response.append(5)
    
    if(test.iloc[i,8] == 'White'):
        response.append(0)
    elif(test.iloc[i,8] == 'Asian-Pac-Islander'):
        response.append(1)
    elif(test.iloc[i,8] == 'Amer-Indian-Eskimo'):
        response.append(2)
    elif(test.iloc[i,8] == 'Other'):
        response.append(3)
    elif(test.iloc[i,8] == 'Black'):
        response.append(4)

    if(test.iloc[i,9] == 'Male'):
        response.append(0)
    elif(test.iloc[i,9] == 'Female'):
        response.append(1)

    if(test.iloc[i,10] == 0):
        response.append(0)
    elif(test.iloc[i,10] != 0):
        response.append(1)
    
    if(test.iloc[i,11] == 0):
        response.append(0)
    elif(test.iloc[i,11] != 0):
        response.append(1)

    if(test.iloc[i,12] <= 20.0):
        response.append(0)
    elif(test.iloc[i,12] <= 40.0 and test.iloc[i,12] > 20):
        response.append(1)
    elif(test.iloc[i,12] <= 60.0 and test.iloc[i,12] > 40):
        response.append(2)
    elif(test.iloc[i,12] <= 80.0 and test.iloc[i,12] > 60):
        response.append(3)
    elif(test.iloc[i,12] > 80):
        response.append(4)

    for j in range(len(country_names_list) - 2):
        if(test.iloc[i,13] == country_names_list[j]):
            response.append(j)

    

    part1 = 1
    part2 = 1
    for k in range(len(test.columns) - 2):
        if k == 2:
            continue
            
        part1 *= globals()[f"r{k}_prob{response[k]}"]

    a = response[-1]
    part1 = part1 * rcountry_probabilities_list[a]
  
    part2 = part2 * pcountry_probabilities_list[a]

    for l in range(len(test.columns) - 2):
        if l == 2:
            continue
        
        part2 *= globals()[f"p{l}_prob{response[l]}"]


    if(part1 == 0 and part2 == 0):
        final_prob = 0
    else:
        final_prob = part1 * r_p[0] / ((part1 * r_p[0]) + (part2 * r_p[1]))
    
    if(final_prob >= 0.5):
        ques.append('>50K')
    else:
        ques.append('<=50K')

    if(ques[i] == ans[i]):
        count = count + 1
 


# In[79]:


accuracy = count/len(test)
print(accuracy)


# >50k is a positive
# <=50k is a negative

# In[86]:


true_p = 0
true_n = 0
false_p = 0
false_n = 0
for i in range(len(ques)):
    if(ques[i] == '>50K' and ans[i] == '>50K'):
        true_p = true_p + 1
    elif(ques[i] == '>50K' and ans[i] == '<=50K'):
        false_p = false_p + 1
    elif(ques[i] == '<=50K' and ans[i] == '<=50K'):
        true_n = true_n + 1
    elif(ques[i] == '<=50K' and ans[i] == '>50K'):
        false_n = false_n + 1

recall = true_p / (true_p + false_n)
precision = true_p / (true_p + false_p)
f1_score = 2 * recall * precision / (precision + recall)

print("Recall:", recall)
print("Precision:", precision)
print("F1 Score:", f1_score)


# ## Laplace Smoothing

# 
