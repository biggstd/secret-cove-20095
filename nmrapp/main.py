
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable
from bokeh.io import curdoc

import pandas as pd
import os
import redis


try:
    rd = redis.from_url(os.environ.get("REDIS_URL"))
    df = pd.read_msgpack(rd.get("csv_preview"))

except ValueError as inst:
    print('SESSION FAILED')
    print(f'got {inst} as an error.')
    df = pd.DataFrame({
        'Not': [0, 1, 2, 3],
        'Working': [2, 5, 6, 8]
    })


source = ColumnDataSource(data=df)

print('column names: ', list(df))
# columns = [TableColumn(field=c, title=c) for c in list(df)]

data_table = DataTable(source=source)# columns=columns)


table = widgetbox(data_table)
curdoc().add_root(row(table))

curdoc().title = "Export CSV"
