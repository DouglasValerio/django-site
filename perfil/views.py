from django.shortcuts import render
from django.shortcuts import render
from bokeh.layouts import row, column
from django.contrib.auth.models import User,auth
from bokeh.core.properties import value
from django.http import HttpResponse
from bokeh.plotting import figure,show
from bokeh.embed import components
from bokeh.transform import dodge
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource, FactorRange, ranges, LabelSet
from collections import Counter
from bokeh.palettes import Category20c
from bokeh.palettes import Category20c, Spectral6, Blues
from bokeh.transform import cumsum
#from .models import Products
from numpy import pi
import pandas as pd
from bokeh.resources import CDN



def my_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        return(username)








# Create your views here.
def perfil(request):
    dados_meta=pd.read_csv('C:/Users/Douglas/Documents/Python Scripts/virtual_env/DASH_/perfil/dados_meta.csv')
    dados_real=pd.read_csv('C:/Users/Douglas/Documents/Python Scripts/virtual_env/DASH_/perfil/dados.csv')
    meses = ['JAN', 'FEV', 'MAR', 'ABR', 'JUN', 'JUL']
    dados = ['Meta', 'Real']
    userID=my_view(request)

    lista_distribuidores=list(dados_meta.columns.values)

    if userID in lista_distribuidores:

            real=dados_real[userID].tolist()
            meta=dados_meta[userID].tolist()
            data = {'meses' : meses,
                    'Meta'   :meta,
                    'Real'   :real}

            list_range=max([max(data['Meta']),max(data['Real'])])

            source = ColumnDataSource(data=data)
            p1 = figure(x_range=meses, y_range=(0, list_range+1), plot_width=750, title="Meta vs Realizado", toolbar_location=None, tools="pan,wheel_zoom,box_zoom,reset, tap")
            p1.vbar(x=dodge('meses', -0.15, range=p1.x_range),  top='Meta', width=0.3, source=source, color="#c9d9d3", legend=value("Meta"))
            p1.vbar(x=dodge('meses', 0.15, range=p1.x_range), top='Real', width=0.3, source=source, color="#2C125D", legend=value("Real"))

            #labels = LabelSet(x='weight', y='height', text='names', level='glyph',
                      #x_offset=5, y_offset=5, source=source, render_mode='canvas')

            p1.x_range.range_padding = 0.0
            p1.xgrid.grid_line_color = None
            p1.ygrid.grid_line_color = None
            p1.min_border_left = 150
            p1.min_border_top = 50
            p1.legend.location = "top_center"
            p1.legend.orientation = "horizontal"

            x = Counter({
                'Produto_1': 157, 'Produto_2': 93, 'Produto_3': 89, 'Produto_4': 63
            })

            data = pd.DataFrame.from_dict(dict(x), orient='index').reset_index().rename(index=str, columns={0:'value', 'index':'country'})
            data['angle'] = data['value']/sum(x.values()) * 2*pi
            data['color'] = Category20c[len(x)]

            # Plotting code

            p2 = figure(plot_width=750, title="Gráfico Teste", toolbar_location=None,
                       tools="hover", tooltips=[("Country", "@country"),("Value", "@value")])

            p2.annular_wedge(x=0, y=1, inner_radius=0.2, outer_radius=0.4,
                            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                            line_color="white", fill_color='color', legend='country', source=data)

            p2.axis.axis_label=None
            p2.axis.visible=False
            p2.xgrid.grid_line_color = None
            p2.ygrid.grid_line_color = None
            p2.min_border_left = 150
            p2.min_border_top = 50
            p2.legend.location = "top_left"


            p3=row(p1,p2)
            p4=row(p1,p2)
            p=column(p3,p4)
            #p.add_layout(labels)
            script, div = components(p)

            return render(request,'home.html', {'script': script, 'div':div})
    else:
            return render(request,'profile.html')
