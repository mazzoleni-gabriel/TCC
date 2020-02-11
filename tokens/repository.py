from .models import Token


def most_recent_token():
    query = '''SELECT * from tokens_token
                        ORDER BY last_expiration
                        NULLS FIRST
                        LIMIT 1'''
    return Token.objects.raw(query)[0]