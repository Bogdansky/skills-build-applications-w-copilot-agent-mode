from django.core.management.base import BaseCommand
from django.conf import settings
 
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Очистка коллекций
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Данные пользователей
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
            {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Данные команд
        teams = [
            {"name": "marvel", "members": [u["email"] for u in users if u["team"] == "marvel"]},
            {"name": "dc", "members": [u["email"] for u in users if u["team"] == "dc"]},
        ]
        db.teams.insert_many(teams)

        # Данные активности
        activities = [
            {"user": "ironman@marvel.com", "activity": "run", "distance": 5},
            {"user": "batman@dc.com", "activity": "cycle", "distance": 20},
            {"user": "spiderman@marvel.com", "activity": "swim", "distance": 2},
            {"user": "superman@dc.com", "activity": "fly", "distance": 100},
        ]
        db.activities.insert_many(activities)

        # Данные лидерборда
        leaderboard = [
            {"team": "marvel", "score": 150},
            {"team": "dc", "score": 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Данные тренировок
        workouts = [
            {"user": "ironman@marvel.com", "workout": "pushups", "reps": 50},
            {"user": "batman@dc.com", "workout": "pullups", "reps": 30},
            {"user": "wonderwoman@dc.com", "workout": "squats", "reps": 100},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
