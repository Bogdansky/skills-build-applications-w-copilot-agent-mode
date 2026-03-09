from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com', first_name='Member', last_name='User')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='active', email='active@example.com', first_name='Active', last_name='User')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories=200, date='2023-01-01T10:00:00Z')
        self.assertEqual(activity.activity_type, 'Run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workout', email='workout@example.com', first_name='Workout', last_name='User')
        workout = Workout.objects.create(user=user, workout_type='Yoga', description='Morning yoga', suggested_by='Coach', date='2023-01-01T08:00:00Z')
        self.assertEqual(workout.workout_type, 'Yoga')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
