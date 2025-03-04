from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Test, TestResult
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)



# Create your views here.
