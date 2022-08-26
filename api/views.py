from rest_framework import viewsets, status
from api import ghibli
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
import json
from django.conf import settings


class MoviesViewSet(viewsets.ViewSet):

    @method_decorator(cache_page(settings.GHIBLI_API_CACHE_TIMEOUT))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        """
        Get the movies, each movie have the information of people appeared in it
        :param request:
        :return:
        """
        films = ghibli.get_films()
        films = json.loads(films.content)

        people = ghibli.get_people()
        people = json.loads(people.content)

        _films = ghibli.update_people_in_films(films, people)

        return Response(data=_films, status=status.HTTP_200_OK)
