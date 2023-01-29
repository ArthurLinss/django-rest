

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


"""
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# https://stackoverflow.com/questions/27368024/django-rest-framework-relationships-hyperlinked-api-issues
router.include_format_suffixes = False
#router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('snippets/', views.snippet_list), #fbv
    # path('snippets/<int:pk>/', views.snippet_detail), #fbv
    path('snippets', views.SnippetList.as_view(), name="snippet-list"),
    path('snippet/<int:pk>', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(), name="snippet-highlight"),

    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user-detail"),

    path('', views.api_root),

]
"""


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.include_format_suffixes = False
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
