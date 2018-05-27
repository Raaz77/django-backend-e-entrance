from django.shortcuts import render
from rest_framework import viewsets
from.models import Student
from .serializer import Studentserilizer




class studentvues(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer
