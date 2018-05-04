"""

Bokeh based ISAtools material creation application.

"""

# Add the isadream file to pythons path so it can be imported.
import sys
import os
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import ontology definitinos.
from isadream.ontologies import (
    MATERIAL_SOURCES,
)

# Display and data science imports.
import bokeh
import bokeh.io
import bokeh.layouts


create_button = bokeh.models.widgets.Button(
    label='Create Sample', button_type="success")

layout = bokeh.layouts.layout(
    sizing_mode='fixed',
    children=[[  # 0
        create_button,
    ]]
)
