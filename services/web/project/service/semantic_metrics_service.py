from ..repository import metrics_repository, github_user_repository, metrics_calculation_repository


def save_shared_contributions(login):
    main_user = github_user_repository.get_by_login(login)
    main_user_id = main_user.github_id
    initial_metrics = metrics_repository.get_metrics_with_SR(main_user_id)
    user_ids = from_metrics_to_user_ids(initial_metrics, main_user_id)

    for u in user_ids:
        shared_contributions = process_shared_contributions(main_user_id, u)
        metrics_repository.update_shared_contributions(main_user_id, u, shared_contributions)

def process_shared_contributions(user_id_1, user_id_2):
    shared_contributions = 0.0
    repo_ids = metrics_calculation_repository.shared_repo_ids_by_users(user_id_1, user_id_2)
    for r in repo_ids:
        contributions = metrics_calculation_repository.count_contributors(r)
        shared_contributions = shared_contributions + ( 2/contributions )
    return shared_contributions/len(repo_ids)

def from_metrics_to_user_ids(metrics, main_user_id):
    user_ids = []
    for m in metrics:
        if m.user_id_1 == main_user_id:
            user_ids.append(m.user_id_2)
        else:
            user_ids.append(m.user_id_1)
    return user_ids
