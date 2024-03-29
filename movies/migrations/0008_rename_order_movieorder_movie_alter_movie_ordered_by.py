# Generated by Django 4.1.3 on 2022-12-07 21:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0007_movieorder_movie_ordered_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movieorder",
            old_name="order",
            new_name="movie",
        ),
        migrations.AlterField(
            model_name="movie",
            name="ordered_by",
            field=models.ManyToManyField(
                related_name="movie",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
