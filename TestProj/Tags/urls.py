from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('tags/', views.TagsList.as_view()),
    path('tag/<int:pk>', views.Tags.as_view()),
    path('user_tag/<int:pk>', views.UserTag.as_view())
]