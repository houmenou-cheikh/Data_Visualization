import numpy as np
import pandas as pd
import plotly.express as px

""" fig1 = go.Figure(go.Scattergeo(locations = data['CODE'],
   hovertext= data['TC'], mode='text',=data['TC'],
    text = data['COUNTRY']))
###################################################################################################   
fig1.update_geos(
    resolution=110,)

fig1.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})

#####################################################################################"
fig1.add_trace(go.Choropleth(
    locations=data['COUNTRY'], # Spatial coordinates
    z = data['TD'], # Data to be color-coded
    locationmode = "country names",
    colorscale = 'Reds',
    colorbar_title = "TD",
))

fig1.update_layout(
    title_text = 'Évaluation du nombres de décés liés au covid19 ',
    
) """
##################################### recup données et nettoyage ##################################
data = pd.read_csv("dataCovid.csv") 
data_1 = pd.read_csv("raw_data.csv") 
data[["TC","TD","POP", "GDPCAP", "STI"]] = data_1[["total_cases","total_deaths","population", "gdp_per_capita","stringency_index"]]
data["DATE"] = pd.to_datetime(data['DATE'])
data = data.fillna(0)
#data = data.dropna()

#print(data.head())
#print(data.groupby('COUNTRY').last().nlargest(10, columns = 'TC'))  ##10 pays(COUNTRY) les plus touchés par covid19(TC)

#bb = data.groupby(["DATE", "COUNTRY"])["TC",'TD'].mean()
cc = data[data["COUNTRY"] == "France"].groupby(pd.Grouper(key='DATE', freq='M'))[['TC','TD','COUNTRY','POP']].last() ## 

#air_quality = pd.concat([aa, cc], axis=0)
#print(air_quality )

data["DATE_2"] = pd.to_datetime(data['DATE'])
aa = pd.DataFrame()
for pays in data["COUNTRY"].unique():
    a = data[data["COUNTRY"] == pays].groupby(pd.Grouper(key='DATE', freq='M')).last() ## 
    aa= pd.concat([aa, a], axis=0)

print(aa)
data_2 = data.groupby("CODE").last()
#print(data_2)
