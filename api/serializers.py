from rest_framework import serializers

from todo import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


class UserHabitSerializer(serializers.ModelSerializer):
    """A serializer for our user habit objects."""

    class Meta:
        model = models.Habit
        fields = ('habit', 'count', 'checked_date',
                    'start_date', 'active_habit')
        extra_kwargs = {'user': {'read_only': True}}
