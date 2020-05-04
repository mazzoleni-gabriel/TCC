from github import Github
from . import github_repository_extrator_service as repo_service
from . import github_pull_request_extrator_service as pulls_service
from ..repository import github_repository_repository as repo_repository


def extract(user_name, steps):
    extract_pulls(user_name)
    extract_users(user_name)

def extract_pulls(user_name):
    save_pulls_from_issues( pulls_service.get_pulls_by_user_name(user_name))

def extract_users(user_name):
    repos = repo_repository.get_repos_by_user(user_name)
    for r in repos:
        pull_issues = pulls_service.get_pulls_by_repo_full_name(r.full_name, user_name)
        save_pulls_from_issues(pull_issues)

def save_pulls_from_issues(pull_issues):
    for issue in pull_issues:
        pulls_service.save_from_issue(issue)


