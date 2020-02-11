from django.urls import path

from .views import token_list, json_most_recent_token, test


urlpatterns = [
    path('', token_list),
    path('most-recent', json_most_recent_token),
    path('test', test),
]