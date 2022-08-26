from rest_framework.routers import DefaultRouter
from api.views import *


routes = DefaultRouter()

routes.register("movies", MoviesViewSet, basename="Movies")

urlpatterns = [*routes.urls]
