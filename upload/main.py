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
        factor_opts.options=factor_dict.get(factor.value)

    factor.on_change('value', factor_change)

    return [factor, factor_opts]


def add_factor():
    print(len(layout.children))
    factor, factor_opts = create_factor()
    new_row = bokeh.layouts.row(factor, factor_opts)
    layout.children.append(new_row)



def remove_factor():
    if len(layout.children) <= 2:
        return
    layout.children.pop()


b_factor = bokeh.models.widgets.Button(
    label='New Factor', button_type="success")
b_factor.on_click(add_factor)

b_rm_factor = bokeh.models.widgets.Button(
    label='Remove Factor', button_type="warning")
b_rm_factor.on_click(remove_factor)


layout = bokeh.layouts.layout(
    sizing_mode='fixed',
    children=[
        user_data_type,
        [b_factor, b_rm_factor]
    ]
)


bokeh.io.curdoc().add_root(layout)
bokeh.io.curdoc().title = "Upload Data"
