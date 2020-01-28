import dash
#import dash_auth
import dash_core_components as dcc
import dash_html_components as html
#from flask import request
from flask_login import current_user
from colour import Color
import base64
import pandas as pd
from dash.dependencies import Input, Output
#from flask import Flask, render_template
#from flask_basicauth import BasicAuth







app = dash.Dash()
app.title = 'Incentivos DPA'



image_filename = 'dpa.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())




df=pd.read_csv("dados.csv",delimiter=',', encoding="utf-8-sig")
df2=pd.read_csv("dados_meta.csv",delimiter=',', encoding="utf-8-sig")
df3=pd.read_csv("dist.csv",delimiter=';', encoding="utf-8-sig")
df4=pd.read_csv("tempo.csv",delimiter=';', encoding="utf-8-sig")
opcoes=df3['dist_TD'].tolist()
meta=df2[opcoes[0]]
real=df[opcoes[0]]






app.layout = html.Div( style={'width': '100%', 'display': 'inline-block'},

    children=[html.H1(children=html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height=120)),
    html.H2('Dash Campanhas de Incentivo'),
   #inicio do dropdown

   html.H3(id='user-div', children=''),

    html.Div(style={'width' : '48%'},children=[
    dcc.Dropdown(
    id='teste',
    options=[{'label':opcao, 'value':opcao} for opcao in opcoes
    ],
    placeholder="Selecione um distribuidor",

    )],
            ),#fim do dropdown




  html.Div(

    dcc.Graph(id='example',
        figure=({
            'data': [
                {'x': df4["mês"], 'y': meta, 'type': 'bar', 'name': 'META','marker' : { "color" :  'rgb(23, 86, 166)'}},

                {'x': df4["mês"], 'y': real, 'type': 'bar', 'name': 'REALIZADO','marker' : { "color" :  'rgb(114, 178, 66)'}},
            ],
            'layout': {
                'title': 'Meta vs Realizado'
                 }
                }),
        style={'width': '600'} ),


    style={'display': 'inline-block'}),

html.Div(

    dcc.Graph(id='example2',
        figure=({
            'data': [
        {'x': df4["mês"], 'y': meta, 'type': 'line', 'name': 'META','marker' : { "color" :  'rgb(23, 86, 166)'}},
        {'x': df4["mês"], 'y': real, 'type': 'line', 'name': 'REALIZADO','marker' : { "color" :  'rgb(114, 178, 66)'}},
    ],
            'layout': {
                'title': 'Meta vs Realizado'
                 }
                }),
        style={'width': '600'}
        ),


    style={'display': 'inline-block'})



])#final da página
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})



@app.callback(
    Output(component_id='example',component_property='figure'),
    [Input(component_id='teste', component_property='value')]
)
def atualiza_grafico(dist_valor):
    meta=df2[dist_valor].tolist()
    real=df[dist_valor].tolist()
    nome=dist_valor

    return {
    'data': [
        {'x': df4["mês"], 'y': meta, 'type': 'bar', 'name': 'META','marker' : { "color" :  'rgb(23, 86, 166)'}},
        {'x': df4["mês"], 'y': real, 'type': 'bar', 'name': 'REALIZADO','marker' : { "color" :  'rgb(114, 178, 66)'}},
    ],
      'layout': {
         	'title': 'Meta vs Realizado - '+str(nome)
           }
}

@app.callback(
    Output(component_id='example2',component_property='figure'),
    [Input(component_id='teste', component_property='value')]
)
def atualiza_grafico2(dist_valor):
    meta=df2[dist_valor].tolist()
    real=df[dist_valor].tolist()
    nome=dist_valor

    return {
    'data': [
        {'x': df4["mês"], 'y': meta, 'type': 'line', 'name': 'META','marker' : { "color" :  'rgb(23, 86, 166)'}},
        {'x': df4["mês"], 'y': real, 'type': 'line', 'name': 'REALIZADO','marker' : { "color" :  'rgb(114, 178, 66)'}},
    ],
      'layout': {
         	'title': 'Meta vs Realizado - '+str(nome)
           }
}



if __name__ == '__main__':
    app.run_server(debug=False)
