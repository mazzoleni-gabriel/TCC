from ..repository import metrics_calculation_repository, metrics_repository
from ..model import Metrics


def calculate_shared_repos():
     query_result = metrics_calculation_repository.shared_repos()
     __save_all(query_result)

def __save_all(query_result): # TODO fazer insert em lote (bulk)
    for r in query_result: __save(r)

def __save(query_single_result):
    metrics_repository.save(__to_metric(query_single_result))

def __to_metric(result):
    metric = Metrics()
    metric.shared_repositories = result.shared_repositories
    metric.user_id_1 = result.user_id_1
    metric.user_id_2 = result.user_id_2
    return metric