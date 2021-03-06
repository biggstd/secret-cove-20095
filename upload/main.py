"""

Bokeh application for creating new ISA documents.

Datatypes to be implement:

+ NMR
    + Simulated
    + Experimental
    + Literature
+ Raman
    + Simulated
    + Experimental
    + Literature
+ Sources (can take characteristics only)
+ Samples

"""

# Add the isadream file to pythons path so it can be imported.
import sys
import os
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import ontology definitinos.
from isadream.ontologies import (
    DATA_TYPES,
    ONTOLOGY_ANNOTATIONS,
    UNIT_FACTORS,
    FACTOR_FACTORS,
)

# Display and data science imports.
import bokeh
import bokeh.io
import bokeh.layouts


# Form generation widgets.
user_data_type = bokeh.models.widgets.RadioButtonGroup(
    labels=[f.get('short_display') for f in DATA_TYPES.values()],
    active=0,
)


factor_options = [f.get('long_display') for f in FACTOR_FACTORS.values()]
factor_values = [f.get('factor_options') for f in FACTOR_FACTORS.values()]
factor_dict = {k: v for k, v in zip(factor_options, factor_values)}


def create_factor():

    factor = bokeh.models.widgets.Select(
        options=factor_options, value=factor_options[0])

    factor_opts = bokeh.models.widgets.Select(
        options=["None"], value="None")

    def factor_change(attr, old, new):
        factor_opts.options = factor_dict.get(factor.value)

    factor.on_change('value', factor_change)

    return [factor, factor_opts]


def add_factor():
    factor, factor_opts = create_factor()
    new_row = bokeh.layouts.row(factor, factor_opts)
    factor_layout_key.insert(-1, new_row)


def remove_factor():
    try:
        factor_layout_key.pop()
    except IndexError as error:
        pass


unit_factor_values = [f.get('factor_options') for f in UNIT_FACTORS.values()]
unit_factor_options = [f.get('long_display') for f in UNIT_FACTORS.values()]
unit_factor_dict = {
    k: v for k, v in zip(unit_factor_options, unit_factor_values)}


def create_unit_factor():

    unit_factor = bokeh.models.widgets.Select(
        options=unit_factor_options, value=unit_factor_options[0])

    # unit_factor_opts = bokeh.models.widgets.Select(
    #     options=["None"], value="None")

    unit_factor_text = bokeh.models.widgets.TextInput(title='value')

    # def unit_factor_change(attr, old, new):
    #     unit_factor_opts.options = unit_factor_dict.get(unit_factor.value)

    # unit_factor.on_change('value', unit_factor_change)

    return [unit_factor, unit_factor_text]


def add_unit_factor():
    unit_factor, unit_factor_text = create_unit_factor()
    new_row = bokeh.layouts.row(unit_factor, unit_factor_text)
    unit_factor_layout_key.insert(-1, new_row)


def remove_unit_factor():
    try:
        unit_factor_layout_key.pop()
    except IndexError as error:
        pass


b_factor = bokeh.models.widgets.Button(
    label='New Factor', button_type="success")
b_factor.on_click(add_factor)

b_rm_factor = bokeh.models.widgets.Button(
    label='Remove Factor', button_type="warning")
b_rm_factor.on_click(remove_factor)

b_unit_factor = bokeh.models.widgets.Button(
    label='New Factor', button_type="success")
b_unit_factor.on_click(add_unit_factor)

b_rm_unit_factor = bokeh.models.widgets.Button(
    label='Remove Factor', button_type="warning")
b_rm_unit_factor.on_click(remove_unit_factor)


from random import randint
data = dict(
    other=[randint(0, 100) for i in range(10)],
    downloads=[randint(0, 100) for i in range(10)],
)
source = bokeh.models.ColumnDataSource(data)
columns = [
    bokeh.models.widgets.TableColumn(field='other', title='other'),
    bokeh.models.widgets.TableColumn(field='downloads', title='bar'),
]
demo_table = bokeh.models.widgets.DataTable(
    source=source, columns=columns)


layout = bokeh.layouts.layout(
    sizing_mode='fixed',
    children=[[  # 0
            bokeh.layouts.column(  # 0.0
                bokeh.layouts.widgetbox(  # 0.0.1
                    user_data_type,
                    b_factor, b_rm_factor,
                    b_unit_factor, b_rm_unit_factor,
                ),
                bokeh.layouts.column(*create_unit_factor()),
                bokeh.layouts.column(*create_factor()),
            ),
            bokeh.layouts.column(demo_table)
        ],
    ]
)

factor_layout_key = layout.children[0].children[0].children[1].children
unit_factor_layout_key = layout.children[0].children[0].children[2].children

bokeh.io.curdoc().add_root(layout)
bokeh.io.curdoc().title = "Upload Data"
