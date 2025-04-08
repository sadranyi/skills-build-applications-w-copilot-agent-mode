from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.name, "Test User")

    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, calories_burned=300, date="2025-04-08")
        self.assertEqual(activity.activity_type, "Running")

    def test_activity_creation(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="1:00:00")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team A")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_leaderboard_creation(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Workout A", description="Test workout", duration=60, difficulty="Medium")
        self.assertEqual(workout.name, "Workout A")

    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")
