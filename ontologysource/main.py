# comment/main.py
'''
Ontology Source Creation

A Bokeh application that allows for the generation of one Ontology Source.
'''


# Display and data science imports.
import bokeh
import bokeh.io
import bokeh.layouts


def create_inputs():
    '''Creates the base input widget box.
    '''

    create_button = bokeh.models.widgets.Button(
        label='Create Field', button_type='success')
    create_button.on_click(add_field)

    delete_button = bokeh.models.widgets.Button(
        label='Remove Field', button_type='warning')
    delete_button.on_click(remove_field)

    submit_button = bokeh.models.widgets.Button(
        label='Submit Field', button_type='success')
    submit_button.on_click(submit_fields)

    output_widgetbox = bokeh.layouts.widgetbox(
        sizing_mode='fixed',
        children=[create_button, delete_button, submit_button])

    return output_widgetbox


def create_field():
    '''Creates a field.
        + Name
        + Description
    '''

    name = bokeh.models.widgets.TextInput(
        title='Name')

    description = bokeh.models.widgets.TextInput(
        title='Description', height=400, width=400)

    output_widgetbox = bokeh.layouts.widgetbox(
        sizing_mode='fixed',
        children=[name, description])

    return output_widgetbox


def add_field():
    '''Adds a comment field to the current bokeh document.'''
    new_field = create_field()
    field_layout_hook.insert(-1, new_field)


def remove_field():
    '''Removes a comment field from the current bokeh document.'''
    try:
        field_layout_hook.pop()
    except IndexError as error:
        pass


def submit_fields():
    '''Get all the user-supplied comments currently on the document.'''
    get_values()
    pass


def get_values():
    '''Iterates through the fields and returns their values.'''
    for box in field_layout_hook:
        for item in box.children:
            print(item.title)
            print(item.value)


layout = bokeh.layouts.layout(
    sizing_mode='fixed',
    children=[
        # Row 1.
        [create_inputs()],
        # Row 2.
        [
            bokeh.layouts.column(children=[create_field()])
        ],
    ]
)

field_layout_hook = layout.children[1].children[0].children

bokeh.io.curdoc().add_root(layout)
bokeh.io.curdoc().title = "Create Ontology Source"
