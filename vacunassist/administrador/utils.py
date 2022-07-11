import enum
import numpy as np
import pandas as pd
import uuid, base64
from .models import *
from io import BytesIO
from matplotlib import pyplot


def generate_code():
    return str(uuid.uuid4()).replace('-', '').upper()[:12]

def get_key(res_by):
    if res_by == '#1':
        key = 'solicitud_id'
    elif res_by == '#2':
        key = 'solicitud_id'
    elif res_by == '#3':
        key = 'solicitud_id'
    elif res_by == '#4':
        key = 'solicitud_id'
    return key

def get_graph():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, results_by, **kwargs):
    pyplot.switch_backend('AGG')
    fig = pyplot.figure(figsize=(10, 4))
    key = get_key(results_by)

    line_color = {
        'Terminal' : 'red',
        'Cementerio' : 'green',
        'Municipalidad' : 'blue',
    }

    d = data.sort_values('fecha_estimada', ascending=True).groupby(['fecha_estimada', 'centro_vacunatorio'], as_index=False)['solicitud_id'].agg('count')
    print('Normal:')
    print(d)
    # d = data.sort_values('fecha_estimada', ascending=True).groupby(['fecha_estimada', 'centro_vacunatorio'])['solicitud_id'].count().unstack(fill_value=0).stack()

    d = pd.pivot_table(d, index=['fecha_estimada', 'centro_vacunatorio'], values='solicitud_id', fill_value=0, dropna=False, aggfunc=np.sum).reset_index()
    print('Pivot:')
    print(d)
    d['fecha_estimada'] = d['fecha_estimada'].apply(lambda x: x.strftime('%d/%m/%Y'))
    xlabels = d['fecha_estimada'].unique()
    print(xlabels)


    for centro in ['Terminal', 'Cementerio', 'Municipalidad']:
        pyplot.plot(xlabels, d.query(f"centro_vacunatorio=='{centro}'")['solicitud_id'], color=line_color[centro], marker='o', linestyle='-.', linewidth=1, label=centro)

    if chart_type == '#1':
        print("Bar graph")
        pyplot.bar(d['fecha_estimada'], d['solicitud_id'])
    elif chart_type == '#2':
        print("Pie chart")
        pyplot.pie(data=d,x='fecha_estimada', labels=d['solicitud_id'])
    elif chart_type == '#3':
        print("Line graph")
        # pyplot.plot(d['fecha_estimada'], d['solicitud_id'], color='gray', marker='o', linestyle='solid', linewidth=2, label='Centro')
        # for i, v in zip(d['fecha_estimada'], d['solicitud_id']):
        #     label = int(v)
        #     pyplot.annotate(label, (i,v), textcoords='offset points', xytext=(0,10), ha='center')
    else:
        print("Apparently...chart_type not identified")

    pyplot.title('Cantidad de solicitudes por fecha sugerida.')
    pyplot.xlabel('Fecha de Solicitud')
    pyplot.ylabel('Solicitudes Recibidas')
    pyplot.tight_layout()
    pyplot.legend()
    chart = get_graph()
    
    return chart