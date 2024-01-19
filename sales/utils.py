from core.models import Item

from io import BytesIO
import base64
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime, timedelta

def get_item_name_by_item_id(item_id):
    item = Item.objects.get(id=item_id)
    return item.name



def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(data, created_at, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    
    # d = data.groupby(created_at, as_index=False)['income'].agg('sum')
    
    sns.barplot(x=created_at, y='income',data=data )
    
    plt.tight_layout()
    chart = get_graph()
    return chart


