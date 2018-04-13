
from bokeh.layouts import row, widgetbox, column, layout, Spacer
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn, Div, Paragraph
from bokeh.io import curdoc
from bokeh.models.widgets import Select, TextInput, MultiSelect

import pandas as pd
import os
import redis

try:
    rd = redis.from_url(os.environ.get("REDIS_URL"))
    df = pd.read_msgpack(rd.get("user_upload"))

except ValueError as inst:
    df = dict(variable_a=[0, 1], variable_b=[0, 1])


source = ColumnDataSource(data=df)


TEMP_OPTIONS = ['a', 'b', 'c']

# ROW 2
# Metadata
doi_selector = TextInput(title="DOI")
author_mselector = MultiSelect(
    title="Author",
    options=TEMP_OPTIONS
)

# Study Factors
al_source_sel = Select(title="Aluminum Source", options=TEMP_OPTIONS)
al_text_in = TextInput(title="New Aluminum Source")
al_concentration_in = TextInput(title="Al Molarity")
base_source_sel = Select(title="Base Source", options=TEMP_OPTIONS)
base_concentration_in = TextInput(title="Base Molarity")
counter_ion_sel = Select(title="Counter Ion Element", options=TEMP_OPTIONS)
peak_type_sel = Select(title="Peak Type", options=TEMP_OPTIONS)

or_text = Paragraph(text="or")

metadata_col = column(widgetbox([
    doi_selector,
    author_mselector,
    al_source_sel,
    or_text,
    al_text_in,
    al_concentration_in,
    base_source_sel,
    base_concentration_in,
    counter_ion_sel,
    peak_type_sel,
]))


def change_plot_data(attr, old, new):
    print(new)
    new_df = pd.DataFrame(new)
    source.data = source.from_df(new_df)

    new_df = pd.DataFrame(source.data)
    columns = [TableColumn(field=c, title=c) for c in list(new_df)]
    data_table = DataTable(source=source, columns=columns)
    my_layout.children[1].children[1] = data_table


df = pd.DataFrame(source.data)
columns = [TableColumn(field=c, title=c) for c in list(df)]
data_table = DataTable(source=source)


my_layout = layout(
    children=[
        [metadata_col, data_table],
    ],
    sizing_mode='fixed'
)

curdoc().add_root(my_layout)

curdoc().title = "Upload Data CSV"
