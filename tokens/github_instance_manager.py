from github import Github
from . import repository
from datetime import datetime, timedelta
from time import sleep
import pytz

#returns an available github instance
def github_user():
    g = Github(current_token().token)
    return g

#returns an available token, if there isn't, wait...
def current_token():
    utc = pytz.UTC
    tz = pytz.timezone('Brazil/East')

    token = repository.most_recent_token()
    last_expiration = token.last_expiration.replace(tzinfo=utc).astimezone(tz)

    now = datetime.now().replace(tzinfo=utc).astimezone(tz)
    now_minus_1 = now - timedelta(hours=1)
    compare = __token_is_not_ready(last_expiration, now_minus_1)

    if __token_is_not_ready(last_expiration, now_minus_1):
        diference = last_expiration - now_minus_1
        sleep(diference.seconds + 1)

    return token

def __token_is_not_ready(last_expiration, now_minus_1):
    return last_expiration > now_minus_1
    