import item as item
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Class
from .serializers import CourseSerializer, ClassSerializer


class CoursesViews(APIView):
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        items = Course.objects.all()
        serializer = CourseSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class ClassesViews(APIView):
    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        items = Class.objects.all()
        serializer = ClassSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class CourseViews(APIView):
    def get(self, request, id):
        item = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(item)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        item = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Course, id=id)
        item.delete()
        return Response({"data": None}, status=status.HTTP_200_OK)

class ClassViews(APIView):
    def get(self, request, id):
        item = get_object_or_404(Class, id=id)
        serializer = ClassSerializer(item)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        item = get_object_or_404(Class, id=id)
        serializer = ClassSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Class, id=id)
        item.delete()
        return Response({"data": None}, status=status.HTTP_200_OK)
