from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
