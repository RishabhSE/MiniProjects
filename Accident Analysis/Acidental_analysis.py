# Importing Pakages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# when you want graphs in a separate window 

# %matplotlib inline
# when you want an inline plot
# *******************************************************************
# *******************************************************************

## Importing Files
Accident = pd.read_csv("C:/LOCAL_R/Rishabh##/Machine Learning/data SET/dft-accident-data/Accidents0515.csv",sep = ',') 
#Casualties = pd.read_csv("C:/LOCAL_R/Rishabh##/Machine Learning/data SET/accident dataset/Casualties0515.csv") 
#Vehicles0515 = pd.read_csv("C:\LOCAL_R\Rishabh##\Machine Learning\data SET\accident dataset\Vehicles0515.csv",sep = 't') 

# *******************************************************************
# *******************************************************************

# ## Understanding the Data

Accident.head()
# To find the dimensions of the Dataset
Accident.shape
# Find the datatype of variables
Accident.dtypes
# Summary of the Dataset
describe=pd.DataFrame(Accident.describe())
# Null Values in the Dataset
null_values = pd.DataFrame(Accident.isnull().sum()/Accident.shape[0])

# *******************************************************************
# *******************************************************************

## Univariate Analysis
# Analysing target variable
Accident['Accident_Severity'].value_counts(normalize = True).plot.bar()

# ****************************************************************
# Independent Variable (Categorical)
plt.figure(1)
plt.subplot(221)
Accident['Pedestrian_Crossing-Human_Control'].value_counts(normalize = True).plot.bar(figsize=(20,10),title = 'Pedestrian_Crossing-Human_Control')
#plt.show()
plt.subplot(222)
Accident['Pedestrian_Crossing-Physical_Facilities'].value_counts(normalize = True).plot.bar(title = 'Pedestrian_Crossing-Physical_Facilities')
#plt.show()
plt.subplot(223)
Accident['Day_of_Week'].value_counts(normalize = True).plot.bar(title = 'Day_of_week')
#plt.show()
plt.subplot(224)
Accident['Light_Conditions'].value_counts(normalize = True).plot.bar(title = 'Light_Conditions')
plt.show()
# ****************************************************************
plt.figure(2)
plt.subplot(221)
Accident['Weather_Conditions'].value_counts(normalize = True).plot.bar(figsize=(20,10),title = 'Weather_Conditions')
#plt.show()
plt.subplot(222)
Accident['Road_Surface_Conditions'].value_counts(normalize = True).plot.bar(title = 'Road_Surface_Conditions')
#plt.show()
plt.subplot(223)
Accident['Special_Conditions_at_Site'].value_counts(normalize = True).plot.bar(title = 'Special_Conditions_at_Site')
#plt.show()
plt.subplot(224)
Accident['Carriageway_Hazards'].value_counts(normalize = True).plot.bar(title = 'Carriageway_Hazards')
plt.show()
# ****************************************************************
plt.figure(3)
plt.subplot(221)
Accident['Urban_or_Rural_Area'].value_counts(normalize = True).plot.bar(figsize=(20,10),title = 'Urban_or_Rural_Area')
#plt.show()
plt.subplot(222)
Accident['Did_Police_Officer_Attend_Scene_of_Accident'].value_counts(normalize = True).plot.bar(title = 'Did_Police_Officer_Attend_Scene_of_Accident')
plt.show()

# *******************************************************************
# *******************************************************************
# Independent Variable (Continuous)

plt.figure(1) 
plt.subplot(221) 
sns.distplot(Accident['Police_Force'],hist=False,color="b", kde_kws={"shade": True}); 
plt.subplot(222) 
Accident['Police_Force'].plot.box( patch_artist=True,figsize=(16,5)) 

plt.subplot(223) 
sns.distplot(Accident['Number_of_Vehicles'],hist=False,color="b", kde_kws={"shade": True}); 
plt.subplot(224) 
Accident['Number_of_Vehicles'].plot.box( patch_artist=True,figsize=(16,5)) 
plt.show()

plt.figure(2) 
plt.subplot(221) 
sns.distplot(Accident['Number_of_Casualties'],hist=False,color="b", kde_kws={"shade": True}); 
plt.subplot(222) 
Accident['Number_of_Casualties'].plot.box( patch_artist=True,figsize=(16,5)) 

plt.subplot(223) 
sns.distplot(Accident['Local_Authority_(District)'],hist=False,color="b", kde_kws={"shade": True}); 
plt.subplot(224) 
Accident['Local_Authority_(District)'].plot.box( patch_artist=True,figsize=(16,5)) 
plt.show()

plt.figure(3) 
plt.subplot(221) 
sns.distplot(Accident['2nd_Road_Number'],hist=False,color="b", kde_kws={"shade": True}); 
plt.subplot(222) 
Accident['2nd_Road_Number'].plot.box( patch_artist=True,figsize=(16,5)) 
plt.show()


# *******************************************************************
# *******************************************************************

# Bi-Variate Analysis

# Categorical Independent Variable vs Target Variable

Day_of_Week = pd.crosstab(Accident['Day_of_Week'],Accident['Accident_Severity'])
# Percentage wise
for i in range(7):
    Day_of_Week.iloc[i] = Day_of_Week.iloc[i,:] / Day_of_Week.iloc[i].sum()

Day_of_Week.plot(kind="bar", stacked=True, figsize=(4,4))


# *******************************************************************
# *******************************************************************
 # Correlation Matrix
matrix = Accident.corr() 
f, ax = plt.subplots(figsize=(9, 6)) 
sns.heatmap(matrix, vmax=.8, square=True, cmap="BuPu");

# *******************************************************************
# *******************************************************************

# Missing Value Treatment

# Count of Missing Values
Accident.isnull().sum()

# Dropping rows containing any missing values
Accident = Accident.dropna()

# Since in this dataset missing values represent -1 values
pd.value_counts(Accident['Junction_Control'].values) # 641392
# Dropping
Accident = Accident[ Accident.Junction_Control != -1 ]

pd.value_counts(Accident['Weather_Conditions'].values)
# Imputing
Accident.Weather_Conditions[Accident.Weather_Conditions == -1] = 1

# *******************************************************************
# *******************************************************************

# Model Building

# Dropping Unecessary Columns
Accident = Accident.drop([],axis = 1)

# Seperating Dependent & Independent Variable
Y = Accident.Accident_Severity
X = Accident.drop('Accident_Severity',1)

# Dummy Variables
X=pd.get_dummies(X) 
 
# Splitting Dataset
from sklearn.model_selection import train_test_split
x_train, x_cv, y_train, y_cv = train_test_split(X,y, test_size =0.3)

























