from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

# API URLs are now determined automatically by the router
urlpatterns = [
    url(r'^', include(router.urls)),
]

