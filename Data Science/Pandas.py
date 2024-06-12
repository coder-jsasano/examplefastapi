import pandas as pd
#print(pd.__version__) #show version of pip
#--------------------------------------------------------------------------------------------
#Series = enable to create list and decide index
A = pd.Series([2,3,4,5], index=['a','b','c','d'])
#print(A.values)
#print(type(A.values)) # Type = numpy array
#print(type(A)) #Type = panda Series
#print(A.index)
#print(A['a'])
#print(A['a':'c'])

grades_dict = {'A':4, 'B':3.5, 'C':3, 'D':2.5}
grades = pd.Series(grades_dict)

marks_dict = {'A':85, 'B':75, 'C':65, 'D':55}
marks = pd.Series(marks_dict)

#print(grades)
#print(marks)

#print(marks['A'])
#print(marks[0:2])
#--------------------------------------------------------------------------------------------
#DataFrame
D = pd.DataFrame({'Marks': marks, 'Grades': grades})
#print(D)
#print(D.T) 
#print(D.values)
#print(D.values[2,0]) #row=2,colum=0 : 65.0
#print(D.columns) # Marks, Grades
D['ScaleMarks'] = (D['Marks']/90)*100
#print(D)
del D['ScaleMarks']
#print(D)

G = D[D['Marks']>70] #Show only marks more than 70
#print(G)
#--------------------------------------------------------------------------------------------
#NaN = Missing values, None
A = pd.DataFrame([{'a':1, 'b':4},{'b':-3, 'c':9}])
#print(A)
#print(A.fillna(0))  #Fill a specified value in every NaN value 
#print(A.dropna())  #Drop every row where there's at least one NaN value 
#--------------------------------------------------------------------------------------------
#Indexing = .loc[:] :explicit index, .iloc[:]:inplicit index
A = pd.Series(['a','b','c'], index=[1,3,5])
#print(A[1])
#print(A[1:3]) #start from 0 and the last number don't be included
#print(A.loc[1:3]) #start from 1 and the last number don't be included
#print(A.iloc[1:3]) #start from 0 and the last number don't be included

#print(D.iloc[2,:]) #access to a whole specified row
#print(D.iloc[::-1,:])
#--------------------------------------------------------------------------------------------
#csv files
import numpy as np
from sklearn.impute import SimpleImputer
from IPython.display import display

try:
    df = pd.read_csv('C:/Users/junpe/Python code/Tutorials/Data Science/WHO-COVID-19-global-data.csv')
    #print('File has been read successfully!')
    
    #Remove unneccesary category
    df.drop(['WHO_region','Cumulative_cases','Country_code','New_deaths'], axis=1, inplace=True)
    #Rename columns 
    df.rename(columns={'Date_reported':'Date','New_cases':'Confirmed','Cumulative_deaths':'Deaths'}, inplace=True)
    

    #Change original date data into pandas' data  
    df['Date'] = pd.to_datetime(df['Date'])
    

    df = df.fillna(0)
    #display(df.head())
    

    df2 = df.groupby('Country')[['Confirmed','Deaths']].sum().reset_index() #Show total cases and deaths with each country
    #df2 = df.groupby(['Country','Date'])[['Confirmed','Deaths']].sum().reset_index() 
    #display(df2.head(10))

    df3 = df2[df2['Confirmed']>100] #show the data with more than 100 Confirmed
    #print(df3)


    #print(df.describe())
    #display(df.head())

except Exception as e:
    print('An error occured:',e)
    

#print(df)




