import networkx as nx
import matplotlib.pyplot as plt
from ..repository import metrics_repository, github_user_repository


def load_graph(login):
    main_user = github_user_repository.get_by_login(login)
    graph = nx.Graph()
    temp_list = []
    all_metrics = metrics_repository.list_all()
    for metric in all_metrics: __add_in_graph(metric, graph, temp_list)

    # nx.draw(graph)
    # plt.show()
    # plt.savefig('foo.png')

def __add_in_graph(metric, graph, temp_list):
    m = __metric_to_dic(metric)
    temp_list.append(m)
    if len(temp_list) >= 500:
        print("Adding to graph")
        graph.add_edges_from(temp_list)
        temp_list.clear()

def __metric_to_dic(metric):
    return (metric.user_id_1, metric.user_id_2, {'weight':metric.shared_repositories} )
