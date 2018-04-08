
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.io import curdoc

import pandas as pd
import os
import redis

rd = redis.from_url(os.environ.get("REDIS_URL"))

try:
    # Get the HTML session context in order to find the appropriate json filepath.
    args = curdoc().session_context.request.arguments
    data_hash = args.get('hash')[0].decode("utf-8")
    print(data_hash)
    print("bokeh trying to read hash object.")
    df = rd.get("T35TH45H")

except Exception as inst:
    print('SESSION FAILED')
    print(f'got {inst} as an error.')
    df = pd.DataFrame({
        'Not': [0, 1, 2, 3],
        'Working': [2, 5, 6, 8]
    })


source = ColumnDataSource(data=df)

print('column names: ', list(df))
columns = [TableColumn(field=c, title=c) for c in list(df)]

data_table = DataTable(source=source, columns=columns)


table = widgetbox(data_table)
curdoc().add_root(row(table))

curdoc().title = "Export CSV"
