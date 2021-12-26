#-------------------------test installation packages-----------------------
import os

try:
    import numpy
except ImportError:
    os.system('pip install numpy')

try:
    import pandas
except ImportError:
    os.system('pip install pandas')

try:
    import dash
except ImportError:
    os.system('pip install dash')

try:
    import geopy
except ImportError:
    os.system('pip install geopy')


import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from geopy.geocoders import Nominatim
import random as rd

#Lecture des fichier csv et nettoyage des données
df1 = pd.read_csv('players.csv')
df2 = pd.read_csv('3ppy.csv')
df3 = pd.DataFrame({ 'year' : df1["draft_year"], 'position' : df1["position"]})

#----------------------------------------------------Histogramme------------------------------------------------

#Création d'une df propre pour la création d'un histogramme
years = [i for i in range (1970, 2019)]
position = ["Ailier Fort", "Pivot", "Meneur", "Ailier", "Arrière"]
df5 = pd.DataFrame(columns= years, index=position)
#Remplissage du dataframe
for i in range (2008, 2019):
    df6 = df1[df1["draft_year"] == str(i)]
    df7 = df6[df6["position"] == "Center"]
    df5[i]["Pivot"] = len(df7.index)
    df8 = df6[df6["position"] == "Power Forward"]
    df5[i]["Ailier Fort"] = len(df8.index)
    df9 = df6[df6["position"] == "Point Guard"]
    df5[i]["Meneur"] = len(df9.index)
    df10 = df6[df6["position"] == "Small Forward"]
    df5[i]["Ailier"] = len(df10.index)
    df11 = df6[df6["position"] == "Shooting Guard"]
    df5[i]["Arrière"] = len(df11.index)

#--------------------------------------------------------Carte------------------------------------------------------------
#Choix de 100 joueurs aléatoires pour le lieu de naissence (car 4600 c'est trop et trop long)
joueuralea = []
for i in range (100):
    joueuralea.append(rd.randint(0,4680))

#Création des listes qui contiennent la latitude et la longitude des endroits de naissence
#grâce à un API, ainsi qu'une liste qui contient les noms des joueurs choisis
longitudeco = []
latitudeco = []
name = []
geocoder = Nominatim(user_agent="geoloc.py")
for i in range(len(joueuralea)):
    if type(df1['birthPlace'][joueuralea[i]]) == str:      
        adresse = df1['birthPlace'][joueuralea[i]]
        location = geocoder.geocode(adresse)
        if (str(type(location))) == "<class 'NoneType'>":
            print("Un des joueur ne possède pas de lieu de naissence connu")
        else:
            latitudeco.append(float(location.latitude))
            longitudeco.append(float(location.longitude))
            name.append(str(df1["name"][i]))

#Création d'une df qui contient toutes les données        
df4 = pd.DataFrame({'lat' : latitudeco,'lon' : longitudeco, 'name' : name})

#On place les lieux de naissences sur la carte (carte libre de droits)
fig = px.scatter_mapbox(df4, lat="lat", lon="lon", hover_name = "name",
                        color_discrete_sequence=["red"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#-----------------------------------------Graph poste drafté--------------------------
# Création d'un graph pour le nombre de poste drafé chaque année
value = 1970
fig2 = {'data': [go.Bar(
                    x=df5.index,
                    y=df5[value]
                    )],
                    'layout': {'title':dict(
            text = 'Nombre de poste drafté dans lannée choisie',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':400,
        "line":dict(
                color="white",
                width=3,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='years',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='pts',color='white')
                    }
        }
#------------------------------------------Application-------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY]) #Thème sombre car plus simple pour la visibilité
app.layout = html.Div(
    children = [
        #Titre
        html.H1(children = "Analyse des données NBA",
            style={"textAlign" : "center", "fontSize": "48px", "color": "white"}),
        html.Label('\n'),
        html.Label('\n'),

        html.H1(children = "Qui est le meilleur shooter ?",
            style={"textAlign" : "center", "fontSize": "30px", "color": "white"}),
        #Création d'un grapgh directement dans l'application
        dcc.Graph(
            figure={
                'data': [go.Bar(
                    x=df2['years'],
                    y=df2['3pts'])],
                    'layout': {'title':dict(
            text = 'Nombre de 3 points marqués par le meilleur shooter par an depuis 1980',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':400,
        "line":dict(
                color="white",
                width=3,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Année',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Nombre de 3 points',color='white')
                
            }
        }
        ),

        html.H1(children = "Où sont nés les joueurs ?",
            style={"textAlign" : "center", "fontSize": "30px", "color": "white"}),

        #Importation de la carte
        html.Label('\n'),
        html.Label('Carte de naissence de 100 joueurs de NBA'),
        html.Label('\n'),
        dcc.Graph(figure= fig),

        html.H1(children = "Quel poste a été le plus drafté ?",
            style={"textAlign" : "center", "fontSize": "30px", "color": "white"}),

        #Création du menu déroulant pour le choix des années
        html.Label('Année'),
        html.Label('\n'),
        dcc.Dropdown(
            id="year_option",
            options = [{'label': '2008', 'value': 2008},
            {'label': '2009', 'value': 2009},
            {'label': '2010', 'value': 2010},
            {'label': '2011', 'value': 2011},
            {'label': '2012', 'value': 2012},
            {'label': '2013', 'value': 2013},
            {'label': '2014', 'value': 2014},
            {'label': '2015', 'value': 2015},
            {'label': '2016', 'value': 2016},
            {'label': '2017', 'value': 2017},
            {'label': '2018', 'value': 2018}
            ],
            value=1970,
            style={"textAlign" : "center", "fontSize": "10px", "color": "black"}
        ),
        #Importation de la dernière figure
        html.Label('\n'),
        html.Div(id='slider-output-container'),
        dcc.Graph( 
            id='graph1',
            figure = fig2
        )

    ]
)
#------------------------------------Menu déroulant année-------------------------------------
#Création de la foniction qui obtient la valeur choisie
@app.callback(
    dash.dependencies.Output(component_id='graph1', component_property='figure'),
    [dash.dependencies.Input(component_id='year_option', component_property='value')]
)
#Création de la fonction qui actualise le graphique à barre en fonction de l'année choisie
def update_output(value):
    return {'data': [go.Bar(
                    x=df5.index,
                    y=df5[value]
                    )],
                    'layout': {'title':dict(
            text = 'Nombre de joueurs draftés par poste dans l’année choisie',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':400,
        "line":dict(
                color="white",
                width=3,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Postes',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='',color='white')
                    }
        }

if __name__ == "__main__":
    app.run_server(debug=True)