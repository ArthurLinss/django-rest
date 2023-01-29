

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import views
from django.urls import path, include

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

    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user-detail"),

    path('', views.api_root),
    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(), name="snippet-highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
