"""

Bokeh based ISAtools material creation application.

"""

# Add the isadream file to pythons path so it can be imported.
import sys
import os
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Display and data science imports.
import bokeh
import bokeh.io
import bokeh.layouts

# Import ontology definitinos.
from isadream.ontologies import (
    MATERIAL_SOURCES,
)


def create_source_field():
    source_field = bokeh.models.widgets.Select(name='source_field',
        options=factor_options, value=factor_options[0])
    return source_field


def add_source_field():
    source_field = create_source_field()
    new_row = bokeh.layouts.row(source_field)
    source_layout_key.insert(-1, new_row)


def delete_source_field():
    try:
        source_layout_key.pop()
    except IndexError as error:
        pass


factor_options = [f.get('name') for f in MATERIAL_SOURCES.values()]


create_source_button = bokeh.models.widgets.Button(
    label='Add Material Source', button_type="success")
create_source_button.on_click(add_source_field)


remove_source_button = bokeh.models.widgets.Button(
    label='Remove Material Source', button_type="warning")
remove_source_button.on_click(delete_source_field)

layout = bokeh.layouts.layout(
    sizing_mode='fixed',
    children=[
        create_source_button,
        remove_source_button,
        bokeh.models.widgets.Paragraph(text='Description...'),
        bokeh.layouts.column(bokeh.layouts.row(create_source_field())),
    ]
)

source_layout_key = layout.children[3].children


bokeh.io.curdoc().add_root(layout)
bokeh.io.curdoc().title = "Sample Creator"
