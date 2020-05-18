from . import github_instance_service as instance_service
from ..repository import github_pull_request_repository
from ..model import Github_pull_request
from ..repository import github_user_repository as user_repository
from ..repository import github_repository_repository as repository_repository
from . import github_user_service as user_service
from . import github_repository_extrator_service as repository_service


def save_pulls_by_repo_name(user, repo_name):
    repo = get_repo(user, repo_name)
    save_pulls_by_repo(repo)

def save_pulls_by_repo(repo):
    pulls = repo.get_pulls(state='all')
    for pygithub_pull in pulls:
        github_pull_request = from_pygithub_object(pygithub_pull, repo)
        github_pull_request_repository.save(github_pull_request)

def save_from_issue(issue):
    pull = issue.as_pull_request()

    github_pull_request = from_pygithub_object(pull, issue.repository)

    github_pull_request_repository.save(github_pull_request)

def from_pygithub_object(pygithub_pull, pygithub_repo):
    github_pull_request = Github_pull_request()
    github_pull_request.github_id = pygithub_pull.id
    github_pull_request.title = pygithub_pull.title
    github_pull_request.state = pygithub_pull.state
    github_pull_request.additions = pygithub_pull.additions
    github_pull_request.deletions = pygithub_pull.deletions
    github_pull_request.github_created_at = pygithub_pull._created_at.value
    github_pull_request.github_closed_at = pygithub_pull._closed_at.value
    github_pull_request.is_merged = pygithub_pull.is_merged()
    github_pull_request.github_merged_at = pygithub_pull._merged_at.value
    __set_user(pygithub_pull, github_pull_request)
    __set_repo(pygithub_repo, github_pull_request)
    return github_pull_request

def has_pulls(user_name, repo):
    filters = ['author:' + user_name,
     'repo:' + repo.full_name,
      'is:pr',
      'created:=>2020-01-01']

    g = instance_service.get_available_instance()
    pulls = g.search_issues(' '.join(filters))
    return pulls.totalCount > 0

def get_pulls_by_user_name(user_name):
    filters = ['author:' + user_name,
        'is:merged',
        'is:pr',
        'created:=>2020-01-01']

    g = instance_service.get_available_instance()
    pulls = g.search_issues(' '.join(filters))
    return pulls

def get_pulls_by_repo_full_name(repo_full_name, user_name):
    filters = ['repo:' + repo_full_name,
         '-author:' + user_name,
        'is:merged',
        'is:pr']

    g = instance_service.get_available_instance()
    pulls = g.search_issues(' '.join(filters))
    return pulls

def get_repo(user, repo_name):
    g = instance_service.get_available_instance()
    repo_path = user + '/' +repo_name
    repo = g.get_repo(repo_path , lazy=True).parent
    return repo

def __set_user(pygithub_pull, github_pull_request):
    github_pull_request.user_id = pygithub_pull.user.id
    if (user_repository.get_by_id( github_pull_request.user_id ) is None):
        user = user_service.from_namedUser_to_user(pygithub_pull.user)
        user_repository.save(user)

def __set_repo(pygithub_repo, github_pull_request):
    github_pull_request.repository_id = pygithub_repo.id
    if (repository_repository.get_by_id( pygithub_repo.id ) is None):
        repo = repository_service.from_pygithub_object(pygithub_repo)
        repository_repository.save(repo)
