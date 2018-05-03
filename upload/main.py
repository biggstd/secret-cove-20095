
from bokeh.layouts import (
    row, widgetbox, column, layout, Spacer)
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import (
    DataTable, TableColumn, Div, Paragraph, Slider, Button)
from bokeh.io import curdoc
from bokeh.models.widgets import (
    Select, TextInput, MultiSelect, RadioButtonGroup)

import pandas as pd
import os
# import redis

# isaDream imports.
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from isadream.ontologies import DATA_TYPES, UNIT_FACTORS, FACTOR_FACTORS


# try:
#     rd = redis.from_url(os.environ.get("REDIS_URL"))
#     df = pd.read_msgpack(rd.get("user_upload"))
#
# except ValueError as inst:


df = dict(variable_a=[0, 1], variable_b=[0, 1])


source = ColumnDataSource(data=df)


OPTIONS = {
    "data_types": [dt['short_display'] for dt in DATA_TYPES],
    "factor_types": [dt['short_display'] for dt in FACTOR_FACTORS],
    "unit_factor_types": [dt['short_display'] for dt in UNIT_FACTORS],
}

IN_DATA_TYPE = RadioButtonGroup(
        labels=OPTIONS["data_types"],
        active=0)

IN_NUMBER_FACTORS = Slider(
    start=0, end=10, value=1, step=1, title="# Factors")

IN_NUMBER_UNIT_FACTORS = Slider(
    start=0, end=10, value=1, step=1, title="# Unit Factors")

generate_form = Button(label="Generate Input Form")


def generate_form_handler():
    gen_unit_types = Select(title="Unit Selection",
                             options=OPTIONS["unit_factor_types"])
    gen_unit_factors_inputs = TextInput(title='placeholder')
    gen_input_rows = row(gen_unit_types, gen_unit_factors_inputs)

    print("Generating form...")
    print(IN_NUMBER_UNIT_FACTORS.value)
    my_layout.children[0] = column(
        IN_DATA_TYPE,
        IN_NUMBER_FACTORS,
        IN_NUMBER_UNIT_FACTORS,
        generate_form,
        *[gen_input_rows for x in range(IN_NUMBER_UNIT_FACTORS.value)]
    )


generate_form.on_click(generate_form_handler)

metadata_col = column(
    IN_DATA_TYPE,
    IN_NUMBER_FACTORS,
    IN_NUMBER_UNIT_FACTORS,
    generate_form
)


def change_plot_data(attr, old, new):
    print(new)
    new_df = pd.DataFrame(new)
    source.data = source.from_df(new_df)

    new_df = pd.DataFrame(source.data)
    columns = [TableColumn(field=c, title=c) for c in list(new_df)]
    data_table = DataTable(source=source, columns=columns)
    my_layout.children[1] = data_table


df = pd.DataFrame(source.data)
columns = [TableColumn(field=c, title=c) for c in list(df)]
data_table = DataTable(source=source)


my_layout = layout(
    children=[metadata_col, data_table],
    sizing_mode='fixed'
)

curdoc().add_root(my_layout)

curdoc().title = "Upload Data CSV"
