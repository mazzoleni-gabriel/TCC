from . import github_instance_service as instance_service
from ..repository import github_repository_repository
from ..model import Github_repository


def save_repos_by_user(user_login):
    g = instance_service.get_available_instance()
    namedUser = g.get_user(user_login)
    for pygithub_repo in namedUser.get_repos():
        github_repository = from_pygithub_object(pygithub_repo)
        github_repository_repository.save(github_repository)

def from_pygithub_object(pygithub_repo):
    github_repository = Github_repository()
    github_repository.github_id = pygithub_repo.id
    github_repository.name = pygithub_repo.name
    github_repository.full_name = pygithub_repo.full_name
    github_repository.is_fork = pygithub_repo.fork
    github_repository.language = pygithub_repo.language
    github_repository.github_created_at = pygithub_repo._created_at.value
    return github_repository
