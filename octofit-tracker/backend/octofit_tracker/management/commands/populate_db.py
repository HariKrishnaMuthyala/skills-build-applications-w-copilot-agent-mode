from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data (use filter for Djongo compatibility)
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = []
        users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True))
        users.append(User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True))

        # Create Workouts
        workouts = []
        workouts.append(Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='Easy'))
        workouts.append(Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium'))

        # Create Activities
        Activity.objects.create(user=users[0], type='Push Ups', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Running', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='Push Ups', duration=20, date=date.today())
        Activity.objects.create(user=users[3], type='Running', duration=60, date=date.today())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
