#---------
# PART ONE
#---------
#TODO: import pandas
import pandas as pd

#TODO: read data from csv file into a variable name `data`
#TODO: pass na_values = ['*', '**', '***', ****', '*****', '******']
data = pd.read_csv(r'DATA300/week_4/6153237444115dat.csv', na_values = ['*', '**', '***', '****', '*****', '******'])
#NOTE: How many rows are there in the data?
print(len(data)) # there are a total of 11,694 rows
#NOTE: What are the column names?
print(data.columns)
column_names = ['USAF', 'WBAN', 'YR--MODAHRMN', 'DIR', 'SPD', 'GUS', 'CLG', 'SKC', 'L',
       'M', 'H', 'VSB', 'MW', 'MW.1', 'MW.2', 'MW.3', 'AW', 'AW.1', 'AW.2',
       'AW.3', 'W', 'TEMP', 'DEWP', 'SLP', 'ALT', 'STP', 'MAX', 'MIN', 'PCP01',
       'PCP06', 'PCP24', 'PCPXX', 'SD'
]
#NOTE: what are the data types of the COlumns?
print(data.dtypes)
data_types = {
    'USAF' : 'int64', 
    'WBAN' : 'int64', 
    'SPD' : 'float64', 
    'GUS' : 'float64', 
    'CLG' : 'float64', 
    'SKC' : 'object', 
    'L' : 'float64', 
    'M' : 'float64', 
    'H' : 'float64', 
    'VSB' : 'float64', 
    'MW' : 'float64', 
    'MW.1' :'float64', 
    'MW.2' : 'float64', 
    'MW.3' : 'float64', 
    'AW' : 'float64', 
    'AW.1' : 'float64', 
    'AW.2' : 'float64', 
    'AW.3' : 'float64', 
    'W' : 'float64', 
    'TEMP' : 'float64', 
    'DEWP' : 'float64', 
    'SLP' : 'float64', 
    'ALT' : 'float64', 
    'STP' : 'float64', 
    'MAX' : 'float64', 
    'MIN' : 'float64', 
    'PCP01' : 'float64', 
    'PCP06' : 'float64', 
    'PCP24' : 'float64', 
    'PCPXX' : 'float64', 
    'SD' : 'float64', 
}
#NOTE: What is the mean Fahrenheit temperature in the data?
print(f"Temperature Mean {data['TEMP'].mean():0.2f}°F")# mean 52.25
#NOTE: What is the standard deviation of the Maximum temperature? (MAX column)
print(f"Temperature Max Standard Deviation {data['MAX'].std():0.2f}°F")# max std 10.31
#NOTE: How many unique stations exists in the data? (USAF column)
print(len(data["USAF"].unique()))# there are 2 unique stations in the data

#---------
# PART TWO
#---------

selected = data[['USAF','YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']].dropna()
# convert to celsius using apply and lambda functions. Round to 1 decimal place
selected["TEMP"] =  selected["TEMP"].apply(lambda temp: round((temp-32)/1.8, 1))
print(selected)

#-----------
# PART THREE
#-----------

# NOTE: divide the selection into two separate subtests for different stations
# and save those DataFrames into disk

# Filter data for code 29980 "kumpula"
kumpula = selected[(selected["USAF"].isin([29980]))]
# save to csv file separated by `,` and 1 decimal point in the floating point numbers
kumpula.to_csv('DATA300/week_4/Kumpula_temps_May_Aug_2017.csv', sep=',',float_format='%.1f')
# Filter data for code 28450 "rovaniemi"
rovaniemi = selected[(selected["USAF"].isin([28450]))]
# save to csv file separated by `,` and 1 decimal point in the floating point numbers
rovaniemi.to_csv('DATA300/week_4/Rovaniemi_temps_May_Aug_2017.csv', sep=',',float_format='%.1f')

#--------------
# PART FOUR (A)
#--------------

#NOTE find median temperature at Kumpula in celsius
print(f'Median temperature in kumpula {kumpula["TEMP"].median():.1f} °C')
#NOTE find median temperature at Rovaniemi in celsius
print(f'Median temperature in Rovaniemi {rovaniemi["TEMP"].median():.1f} °C')

#--------------
# PART FOUR (B)
#--------------

kumpula_may = kumpula.loc[(kumpula['YR--MODAHRMN'] >= 201705010000) & (kumpula['YR--MODAHRMN'] < 201706010000)]
kumpula_june = kumpula.loc[(kumpula['YR--MODAHRMN'] >= 201706010000) & (kumpula['YR--MODAHRMN'] < 201707010000)]
rovaniemi_may = rovaniemi.loc[(rovaniemi['YR--MODAHRMN'] >= 201705010000) & (rovaniemi['YR--MODAHRMN'] < 201706010000)]
rovaniemi_june = rovaniemi.loc[(rovaniemi['YR--MODAHRMN'] >= 201706010000) & (rovaniemi['YR--MODAHRMN'] < 201707010000)]

# print mean, min and max temperatures for May and June
print(
    f"Kumpula Stats For May:\t\
    mean: {kumpula_may['TEMP'].mean():.1f}\t\
    min: {kumpula_may['TEMP'].min():.1f}\t\
    max: {kumpula_may['TEMP'].max():.1f}"
)
print(
    f"Rovaniemi Stats For May:\t\
    mean: {rovaniemi_may['TEMP'].mean():.1f}\t\
    min: {rovaniemi_may['TEMP'].min():.1f}\t\
    max: {rovaniemi_may['TEMP'].max():.1f}"
)
print(
    f"Kumpula Stats For June:\t\
    mean: {kumpula_june['TEMP'].mean():.1f}\t\
    min: {kumpula_june['TEMP'].min():.1f}\t\
    max: {kumpula_june['TEMP'].max():.1f}"
)
print(
    f"Rovaniemi Stats For June:\t\
    mean: {rovaniemi_june['TEMP'].mean():.1f}\t\
    min: {rovaniemi_june['TEMP'].min():.1f}\t\
    max: {rovaniemi_june['TEMP'].max():.1f}"
)