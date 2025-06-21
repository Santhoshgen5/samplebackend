from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class Dataview(APIView):
    
    def get(self, request):
        
        return Response({"data":"This Is From API Endpoint"})




