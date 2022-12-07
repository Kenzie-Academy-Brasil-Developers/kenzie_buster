from django.db import models


class Rating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default="")
    rating = models.CharField(
        max_length=20,
        choices=Rating.choices,
        default=Rating.G,
    )
    synopsis = models.TextField(
        null=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user",
    )
