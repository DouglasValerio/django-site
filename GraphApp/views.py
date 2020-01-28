from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure,show
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6, Blues
from bokeh.transform import cumsum
#from .models import Products
from numpy import pi
import pandas as pd
from bokeh.resources import CDN


# Create your views here.
def graph(request):
    # prepare some data
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    # using list comprehension to create 3 other data sets
    y0 = [i**2 for i in x]
    y1 = [10**i for i in x]
    y2 = [10**(i**2) for i in x]

    # create a new plot
    p = figure(
    tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair", # this gives us our tools
    y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
    x_axis_label='sections', y_axis_label='particles'
    )

    # add some renderers
    p.line(x, x, legend="y=x") #thin blue line
    p.circle(x, x, legend="y=x", fill_color="white", size=8) # adds circles to y=x line
    p.line(x, y0, legend="y=x^2", line_width=3) # thick blue line
    p.line(x, y1, legend="y=10^x", line_color="red") # red line
    p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6) # adds red circles
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4") # orange dotted line

    script, div = components(p)

    return render(request,'home.html', {'script': script, 'div':div})
