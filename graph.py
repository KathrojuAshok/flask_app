import matplotlib.pyplot as plt
import io
import base64

def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.figure(figsize=(15,8))
    plt.bar(x_coordinates, y_coordinates)
    plt.xticks(rotation='vertical')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode("utf-8")
    plt.close()
    return graph_url
#    return 'data:image/png;base64,{}'.format(graph_url)