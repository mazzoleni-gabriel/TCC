from ..repository import metrics_repository, github_user_repository

def compile(login):
    main_user = github_user_repository.get_by_login(login)
    limit = 3

    metrics = {}

    from_adamic = metrics_repository.ordered_by_adamic_adar(main_user.github_id, limit)
    from_jaccard = metrics_repository.ordered_by_jaccard_coefficient(main_user.github_id, limit)
    from_resource_allocation = metrics_repository.ordered_by_resource_allocation(main_user.github_id, limit)
    from_shared_contributions = metrics_repository.ordered_by_shared_contributions(main_user.github_id, limit)
    from_shared_pulls = metrics_repository.ordered_by_shared_pulls(main_user.github_id, limit)
    from_shared_repositories = metrics_repository.ordered_by_shared_repositories(main_user.github_id, limit)

    for m in from_adamic: add_metric(metrics, m, main_user.github_id)
    for m in from_jaccard: add_metric(metrics, m, main_user.github_id)
    for m in from_resource_allocation: add_metric(metrics, m, main_user.github_id)
    for m in from_shared_contributions: add_metric(metrics, m, main_user.github_id)
    for m in from_shared_pulls: add_metric(metrics, m, main_user.github_id)
    for m in from_shared_repositories: add_metric(metrics, m, main_user.github_id)

    print_header()
    for key in metrics: print_metric(metrics[key])



def add_metric(metrics, m, main_user_id):
    metrics[m.id] = { 'metric' : m, 'user' : get_recommendation_user(m, main_user_id) }

def get_recommendation_user(metric, main_user_id):
    if metric.user_id_1 != main_user_id:
        return github_user_repository.get_by_id( metric.user_id_1 )
    return github_user_repository.get_by_id( metric.user_id_2 )

def print_metric(m):
    cell_separator = '	'
    github_url = 'github.com/'
    user = m['user']
    metric = m['metric']

    to_print = [ github_url + user.login,
                user.avatar_url,
                    format_float( metric.shared_repositories ),
                    format_float( metric.shared_contributions ),
                    format_float( metric.shared_pulls ),
                    format_float( metric.adamic_adar ),
                    format_float( metric.resource_allocation ),
                    format_float( metric.jaccard_coefficient )]

    print( cell_separator.join(to_print) )

def print_header():
    cell_separator = '	'
    
    to_print = [ 'User name',
                'Avatar URL',
                'shared_repositories',
                'shared_contributions',
                'shared_pulls',
                'adamic_adar',
                'resource_allocation',
                'jaccard_coefficient' ]
    print( cell_separator.join(to_print) )

def format_float(f):
    return str(f).replace('.', ',')