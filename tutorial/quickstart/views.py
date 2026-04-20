from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):# By inheriting from viewsets.ModelViewSet, you are telling DRF
    #to automatically provide the logic for standard "CRUD" operations.
    #This single class automatically handles list (GET all), create (POST),
    #retrieve (GET one), update (PUT/PATCH), and destroy (DELETE).
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset=User.objects.all().order_by("-date_joined")#The - prefix indicates descending order
    serializer_class=UserSerializer 
    """
    This line tells the view to use UserSerializer to convert the User database objects 
    into JSON format (for outgoing responses) and to validate incoming JSON data before saving it to the database.
    """
    permission_classes=[permissions.IsAuthenticated]#IsAuthenticated ensures that only users who are 
    #logged in (providing a valid token or session) can access this endpoint.

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset=Group.objects.all().order_by("name")
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]

