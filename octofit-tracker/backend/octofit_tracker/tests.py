from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'U')
    def test_activity_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@test.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2025-01-01')
        self.assertEqual(str(activity), 'U2 - Run')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T3', description='d3')
        user = User.objects.create(name='U3', email='u3@test.com', team=team, is_superhero=True)
        lb = Leaderboard.objects.create(user=user, score=10, rank=1)
        self.assertEqual(str(lb), 'U3 - Rank 1')
