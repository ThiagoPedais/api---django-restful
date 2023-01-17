from rest_framework import serializers
from .models import Course, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'create',
            'active',
        )


class CourseSerializer(serializers.ModelSerializer):
    # evaluations = EvaluationSerializer(many=True, read_only=True)


    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'create',
            'active',
            'evaluations'
        )