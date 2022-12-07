from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies.serializers import MoviesSerializer
from .permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MoviesSerializer(movie, many=True)
        return Response(serializer.data)

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self, request: Request) -> Response:
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieViewTest(APIView):
    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
