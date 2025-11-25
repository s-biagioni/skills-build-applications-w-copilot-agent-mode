agent: 'agent'
model: GPT-4.1
description: 'Update Django project files for OctoFit Tracker with models, serializers, views, urls, admin, and test support for collections and API root'

# Django App Updates

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

1. Update `settings.py` for MongoDB connection and CORS.
2. Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, and `admin.py` to support users, teams, activities, leaderboard, and workouts collections.
3. Ensure `/` points to the api and `api_root` is present in `urls.py`.

Additional implementation details and helpful pointers:
- Use Djongo for MongoDB integration and make sure `DATABASES` in `settings.py` points to the `octofit_db` database.
- Make sure `rest_framework`, `corsheaders`, and the `octofit_tracker` app are in `INSTALLED_APPS`.
- Add `CorsMiddleware` to `MIDDLEWARE` and set `CORS_ALLOW_ALL_ORIGINS=True`.
- Create Django REST Framework `serializers.py` for `User`, `Team`, `Activity`, `Leaderboard`, and `Workout` models.
- Create `views.py` with DRF `ModelViewSet` or class-based views for the collections and register them on a `DefaultRouter` within `urls.py` under the path `/api/`.
- Provide a minimal `tests.py` to confirm endpoints return 200 and the serialized data structure matches the model fields for a sample object.
- In `admin.py` register the models for admin access.
- Ensure `octofit_tracker/management/commands/populate_db.py` or equivalent DB population code is available to load test data.

When building the API, ensure these endpoints exist and are reachable:
- `/api/users/`
- `/api/teams/`
- `/api/activities/`
- `/api/workouts/`
- `/api/leaderboard/`
- `/api/` should return an API root linking to the available resources.

Include brief comments where required and write code that follows Django conventions and PEP-8 style.
