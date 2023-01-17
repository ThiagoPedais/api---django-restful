from typing import re

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer


class CourseAPIView(APIView):
    """
    API COURSE
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request):
        snippet = Course.objects.get(id=request.data['id'])

        serializer = CourseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )

    # def delete(self, pk):
    #    snippet = self.get_obeject(pk)
    #    snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)


class EvaluationAPIView(APIView):
    """
    API EVALUATION
    """
    def get(self, request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)



