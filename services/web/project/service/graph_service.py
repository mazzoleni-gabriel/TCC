import networkx as nx
from ..repository import metrics_repository, github_user_repository


def load_graph(login):
    main_user = github_user_repository.get_by_login(login)
    graph = nx.Graph()
    temp_list = []
    all_metrics = metrics_repository.list_all()
    for metric in all_metrics: __add_in_graph(metric, graph, temp_list)

    to_predict = __nodes_to_predict(graph.nodes, main_user.github_id)

    calculate_and_save_adamic(graph, to_predict)
    calculate_and_save_jaccard(graph, to_predict)
    calculate_and_save_resource_allocation(graph, to_predict)


    print("done")
    # nx.draw(graph)
    # plt.show()
    # plt.savefig('foo.png')

def calculate_and_save_adamic(graph, to_predict):
    print("Calculating adamic")
    adamic = nx.adamic_adar_index(graph, to_predict)
    for u, v, p in adamic:
        metrics_repository.update_adamic(u, v, p)

def calculate_and_save_resource_allocation(graph, to_predict):
    print("Calculating resource_allocation")
    resource_allocation = nx.resource_allocation_index(graph, to_predict)
    for u, v, p in resource_allocation:
        metrics_repository.update_resource_allocation(u, v, p)

def calculate_and_save_jaccard(graph, to_predict):
    print("Calculating jaccard")
    jaccard = nx.jaccard_coefficient(graph, to_predict)
    for u, v, p in jaccard:
        metrics_repository.update_jaccard(u, v, p)

def __add_in_graph(metric, graph, temp_list):
    m = __metric_to_dic(metric)
    temp_list.append(m)
    if len(temp_list) >= 1000: #TODO arrumar casos que sobram
        print("Adding to graph")
        graph.add_edges_from(temp_list)
        temp_list.clear()

def __metric_to_dic(metric):
    return (metric.user_id_1, metric.user_id_2, {'weight':metric.shared_repositories} )

def __nodes_to_predict(nodes, main_user_id):
    to_predict = []
    for n in nodes:
        if n != main_user_id: to_predict.append( (main_user_id, n) )
    return to_predict