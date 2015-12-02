# -*- coding: utf-8 -*-
from django.shortcuts import render

import uuid
import os
import logging
import json
import collections
# REST Framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import generics

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import default_storage as storage
from django.http import HttpResponseRedirect
from datetime import datetime
from models import *
from django.conf import settings
from serializers import *


logger = logging.getLogger('basicrest')



class PetView(APIView):
    throttle_scope = '1persecond'
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        """
        Creates a new Pet
        """
            
        name = request.data["name"]
        race = request.data["race"]
        
        if(not name or not race):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        pet = Pet.objects.create(name=name, race=race)
        
        serializer = PetSerializer(pet)
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    
    def get(self, request, id=None):
        """
        Gets a Pet by its ID
        """
        
        if(not id):
            return Response(status=status.HTTP_400_BAD_REQUEST)


        pet = Pet.objects.get(id=id)

        if(not pet):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PetSerializer(pet)

        return Response(serializer.data)


    def put(self, request, id=None):
        """
        Edit a Pet
        """
            
        if(not id):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        name = request.data["name"]
        race = request.data["race"]
        
        if(not name or not race):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        pet = Pet.objects.get(id=id)
        pet.name=name
        pet.race=race
        pet.save()
        
        serializer = PetSerializer(pet)
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



class PetActivityView(APIView):
    throttle_scope = '1persecond'
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated,)

   
    def post(self, request, id=None):
        """
        Creates a new Pet
        """
            
        activity = request.data["activity"]
        pet = Pet.objects.get(id=id)
        
        if(not id or not activity or not pet):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        petactivity = PetActivity.objects.create(pet=pet, activity=activity)
        
        serializer = PetActivitySerializer(petactivity)
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class PetListView(generics.ListAPIView):
    renderer_classes = (JSONRenderer,)
    serializer_class = PetSerializer

    def get_queryset(self):
        """
        Retorna el listado de facturas basado en "desde" y "hasta"
        """

        since = self.request.query_params.get('since', None)
        until = self.request.query_params.get('until', None)

        if(until and 'T' not in until):
            # tiempo no especificado
            until = until + "T23:59:59.0000Z"

        if(since and until):
            result = Pet.objects.filter(fecha_creacion__range=(since, until))
        elif(since and not until):
            result = Pet.objects.filter(fecha_creacion__gte=since)
        elif(until and not since):
            result = Pet.objects.filter(fecha_creacion__lte=until)
        elif(not since and not until):
            result = Pet.objects.all()

        return result



