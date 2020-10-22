#!/usr/bin/env python
# coding: utf-8

# # Proyecto-01-python-datos-vectoriales-visualización

# In[26]:


# Importar paquetes

import folium 
print(folium.__version__)
from folium import plugins
import numpy as np
import json
import pandas as pd
import os
import csv
import branca


# In[4]:


import pandas as pd
import json
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
from folium import plugins


# In[5]:


# definir y leer archivos csv

df_positivos = pd.read_csv('datos/10_07_CSV_POSITIVOS_ULTIMA_FECHA.csv', sep=',')
df_fallecidos = pd.read_csv('datos/10_07_CSV_FALLECIDOS_ULTIMA_FECHA.csv', sep=',')
df_activos = pd.read_csv('datos/10_07_CSV_ACTIVOS_ULTIMA_FECHA.csv', sep=',')
df_recuperados = pd.read_csv('datos/10_07_CSV_RECUPERADOS_ULTIMA_FECHA.csv', sep=',')


# In[6]:


# sustituir el valor 0 por id


df_positivos.rename(columns = {'Unnamed: 0': 'id'}, inplace=True)
df_activos.rename(columns = {'Unnamed: 0': 'id'}, inplace=True)
df_recuperados.rename (columns = {'Unnamed: 0': 'id'}, inplace=True)
df_fallecidos.rename(columns = {'Unnamed: 0': 'id'}, inplace=True)


# In[27]:


df_positivos
df_fallecidos
df_activos
df_recuperados


# In[53]:


df_fallecidos


# In[7]:


df_positivos


# # Mapa : Número de dasos positivos, activos, recuperados y fallecidos por  Covid 19 por cantones en Costa Rica  para el año 2020

# In[46]:


import pandas as pd
import folium
import os


#GeoJson de cantones 

geo_cantones = r'datos/cr_limite_cantonal_ign_wgs84.geojson'

geo_cantones = os.path.join('datos/cr_limite_cantonal_ign_wgs84.geojson')

#with open(geo_cantones) as cantones_1:
    #geo_cantones = json.load(cantones_1)



#Mapa del mapa base 
mapa = folium.Map(
    location=[10, -84], 
    zoom_start=7, 
    control_scale = True,
    show =['positivos','df_positivos', 'fallecidos','activos','recuperados', 'po1', 'geo_cantones', True],
    tiles='openstreetmap')



# Agregar teselas
tiles = [ 'CartoDB dark_matter','cartodbpositron' ]
for tile in tiles: 
     folium.TileLayer(tile).add_to (mapa)
        
#Mapa del geoJson


    
#Mapa de coropletas  

# mapa de coropletas_mapa_positivos

po1=folium.Choropleth(geo_data=geo_cantones, 
    data= df_positivos, 
    columns=['cod_canton', 'positivos'],
    key_on='feature.properties.cod_canton',            
    fill_color='YlOrRd', 
    fill_opacity=0.75, 
    line_opacity=0.75,
    name ='Casos positivos',
    legend_name='Numero de casos positivos',
    highlight = True,
    bins = [0, 2500, 5000, 10000, 15000],
    overlay = True,
    show = True,             
    smooth_factor=0).add_to(mapa)
                 
         
# mapa de coropletas_mapa_fallecidos
fa2=folium.Choropleth(geo_data=geo_cantones, 
    data=df_fallecidos, columns=['cod_canton', 'fallecidos'],
    key_on='feature.properties.cod_canton',
    fill_color='YlOrRd', 
    fill_opacity=0.75, 
    line_opacity=0.75,
    name ='Número de fallecidos',
    overlay = True,
    control_scale = True,
    legend_name='Numero de fallecidos',
    bins = [0,50, 100, 150, 200, 250],            
    highlight = True,            
    smooth_factor=0).add_to(mapa)


# mapa de coropletas activos
ac3=folium.Choropleth(geo_data=geo_cantones, 
    data=df_activos, columns=['cod_canton', 'activos'],
    key_on='feature.properties.cod_canton',
    fill_color='YlOrRd', 
    fill_opacity=0.75, 
    line_opacity=0.75,
    legend_name='Numero de casos activos',
    overlay = True,                  
    name = 'Número de casos activos',
    bins = [0,500, 1000, 1500, 2000, 2500, 3000, 3500],            
    highlight = True,            
    smooth_factor=0).add_to(mapa)


# mapa de coropletas recuperados
rec4=folium.Choropleth(geo_data=geo_cantones, 
    data=df_recuperados,columns=['cod_canton', 'recuperados'],
    key_on='feature.properties.cod_canton',
    fill_color='GnBu', 
    fill_opacity=0.75, 
    line_opacity=0.5,
    legend_name='Numero de recuperados',
    name = 'Número de recuperados',
    bins = [0, 2500, 5000, 10000, 15000],            
    control_scale = True,
    overlay = True,                   
    highlight = True,
    smooth_factor=0).add_to(mapa)



# Control de capa


gjson = folium.GeoJson(data = geo_cantones, name = "Cantones" ).add_to(mapa)
folium.features.GeoJsonPopup (fields=['canton'], labels= True , aliases = ['Cantón:'], name = 'Cantones' ).add_to(gjson) 

folium.LayerControl().add_to(mapa) 

mapa



# In[ ]:




