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
            'evaluation',
            'create',
            'active',
        )

    def validate_evaluation(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError("A avaliação precisa ser um número inteiro entre 1 e 5.")


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
