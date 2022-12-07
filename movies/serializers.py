from rest_framework import serializers
from .models import Movie, Rating, MovieOrder


class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        required=False,
        default="",
    )
    rating = serializers.ChoiceField(
        choices=Rating.choices,
        default=Rating.G,
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj) -> str:
        return obj.user.email

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie


class MoviesOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField(read_only=True)

    def get_title(self, obj):
        return obj.movie.title

    def get_buyed_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        order = MovieOrder.objects.create(**validated_data)
        return order
