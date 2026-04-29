import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]

    genres = [Genre(name=item) for item in genres]
    actors = [Actor(**item) for item in actors]

    # 1. CREATE
    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors)

    # 2. UPDATE
    Genre.objects.filter(id=3).update(name="Drama")
    Actor.objects.filter(id=1).update(last_name="Clooney")
    Actor.objects.filter(id=2).update(first_name="Keanu", last_name="Reeves")

    # 3. DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. READ
    smiths = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smiths
