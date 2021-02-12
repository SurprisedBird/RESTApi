from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from fbvApp.models import Student
from fbvApp.serializers import StudentSerializer

# Create your views here.


def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
