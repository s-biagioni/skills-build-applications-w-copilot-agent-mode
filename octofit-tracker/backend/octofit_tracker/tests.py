from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Team, User, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create sample data
        self.marvel = Team.objects.create(name='Marvel')
        self.dc = Team.objects.create(name='DC')
        self.user1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.marvel)
        self.activity = Activity.objects.create(user=self.user1, type='Running', duration=30, date='2025-11-25')
        self.workout = Workout.objects.create(name='Hero HIIT', description='High intensity')
        self.workout.suggested_for.set([self.marvel, self.dc])
        self.leaderboard = Leaderboard.objects.create(team=self.marvel, points=100)

    def test_api_root(self):
        # API root should exist at / (as we map the router there)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Ensure keys for our endpoints are present
        content = response.json()
        self.assertIn('users', content)
        self.assertIn('teams', content)
        self.assertIn('activities', content)
        self.assertIn('workouts', content)
        self.assertIn('leaderboard', content)

    def test_users_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        self.assertIn('email', data[0])

    def test_teams_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        self.assertIn('name', data[0])

    def test_activities_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        self.assertIn('type', data[0])

    def test_workouts_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        self.assertIn('name', data[0])

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 0)
