#matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)
plt.plot(x,y)
plt.scatter(x[::15],y[::15], color = 'red') #show scatter points
#plt.show()

plt.plot(x,y,color='b')
plt.plot(x,np.cos(x),color='g')
#plt.show()
#-------------------------------------------------------------------------------------------------------------
import pandas as pd
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
    countries = df3['Country'].unique()
    #print(len(countries))

#    for idx in range(0,len(countries)):
#        C = df3[df3['Country'] == countries[idx]]
#        plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
#        plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
#        plt.title(countries[idx])
#        plt.xlabel('Days since the first suspect')
#        plt.ylabel('Number of cases')
#        plt.legend()
        #plt.show()

    df4 = df.groupby('Date')[['Confirmed','Deaths']].sum()

    C = df4
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title('World')
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()




    #print(df.describe())
    #display(df.head())

except Exception as e:
    print('An error occured:',e)


