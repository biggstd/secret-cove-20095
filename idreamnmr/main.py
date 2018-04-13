import os

import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.layouts import layout, widgetbox
from bokeh.models import ColumnDataSource, HoverTool, Div, TapTool, LinearInterpolator
from bokeh.models.widgets import Slider, Select, TextInput
from bokeh.io import curdoc
from bokeh.models.widgets import Div, Tabs, Panel
from bokeh.transform import factor_cmap
from bokeh.palettes import d3


df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "data/al_largest_int.csv"))
# Get the column names for use in the selectors.
columns = sorted(df.columns)
discrete = [x for x in columns if df[x].dtype == object]
continuous = [x for x in columns if x not in discrete]
quantileable = [x for x in continuous if len(df[x].unique()) > 20]


source = ColumnDataSource()

hover = HoverTool(tooltips=[
    ('X, Y', '($x, $y)'),
    # ('ppm Al', '@{Al_ppm}'),
    # ('[OH-]', '@{OH_concentration}'),
    # ('[Al] total', '@{Al_concentration}')
])


def update_data():
    """Upodates the Bokeh ColumnDataSource with subsets of data
    collected from a search result."""

    # Set the X and Y values to those selected by the user.
    source.data = dict(
        x=df[x_selector.value],
        y=df[y_selector.value],
    )

    # Iterate over the entire dataframe generated by the 'search'
    # function, and add all of these generated columns to the
    # Bokeh ColumnDataSource.
    for col in list(df):
        source.add(data=df[col], name=col)


def create_figure():
    """
    Create the bokeh plot.
    """
    update_data()

    panels = []

    for axis_type in ["linear", "log"]:

        fig = figure(
            name='primary_figure',
            width=600,
            x_axis_type=axis_type
        )

        sizes = 7
        if size.value != 'None':
            size_scale = LinearInterpolator(
                x=[min(source.data[size.value]), max(source.data[size.value])],
                y=[5, 15]
            )
            sizes = dict(field=size.value, transform=size_scale)

        if color.value != 'None':
            colors = factor_cmap(
                field_name=color.value,
                palette=d3["Category10"][10],
                factors=sorted(source.data[color.value].unique())
            )
        else:
            colors = "#31AADE"

        fig.circle(
            source=source,
            x='x',
            y='y',
            color=colors,
            size=sizes,
            legend=color.value,
        )

        fig.legend.location = "bottom_left"

        x_title = x_selector.value
        y_title = y_selector.value

        fig.xaxis.axis_label = x_title
        fig.yaxis.axis_label = y_title

        fig.add_tools(hover)
        fig.add_tools(TapTool())

        panel = Panel(child=fig, title=axis_type)
        panels.append(panel)

    tabs = Tabs(tabs=panels, width=620)

    return tabs


def update_plot(attr, old, new):
    """
    Define the function to be run upon an update call.
    """
    layout.children[1].children[1] = create_figure()


x_selector = Select(title='X Axis', options=continuous, value=continuous[0])
x_selector.on_change('value', update_plot)

y_selector = Select(title='Y-Axis', options=continuous, value=continuous[1])
y_selector.on_change('value', update_plot)

color = Select(title='Color', value='None', options=['None'] + discrete)
color.on_change('value', update_plot)

size = Select(title='Size', value='None', options=['None'] + continuous)
size.on_change('value', update_plot)

controls = widgetbox([x_selector, y_selector, color, size])

title_div = Div(text="<h1>Aluminate CrossFilter</h1>")

layout = layout(
    children=[
        title_div,
        [controls, create_figure()],
    ],
    sizing_mode='fixed'
)

curdoc().add_root(layout)
curdoc().title = "NMR Crossfilter"
