from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name']

    def get_id(self, obj):
        return str(obj._id) if getattr(obj, '_id', None) else None


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team']

    def get_id(self, obj):
        return str(obj._id) if getattr(obj, '_id', None) else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'date']

    def get_id(self, obj):
        return str(obj._id) if getattr(obj, '_id', None) else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    suggested_for = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']

    def get_id(self, obj):
        return str(obj._id) if getattr(obj, '_id', None) else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

    def get_id(self, obj):
        return str(obj._id) if getattr(obj, '_id', None) else None
