from . import github_instance_service
from ..model import Github_user

def get_user(user_login):
    g = github_instance_service.get_available_instance()
    #TODO return None when 404
    namedUser = g.get_user(user_login)
    github_user = from_namedUser_to_user(namedUser)
    return github_user

def from_namedUser_to_user(namedUser):
    github_user = Github_user()
    github_user.github_id = namedUser.id
    github_user.login = namedUser.login
    github_user.name = namedUser.name
    github_user.location = namedUser.location
    github_user.avatar_url = namedUser.avatar_url
    github_user.bio = namedUser.bio
    github_user.email = namedUser.email
    github_user.hireable = namedUser.hireable
    github_user.github_created_at = namedUser._created_at.value
    return github_user