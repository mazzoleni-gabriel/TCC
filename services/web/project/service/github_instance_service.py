from github import Github
from .reset_token_service import get_available_token, switch_token

def get_new_instance():
    available_token = switch_token()
    return Github(available_token.token_value)

def get_available_instance():
    available_token = get_available_token()
    return Github(available_token.token_value)