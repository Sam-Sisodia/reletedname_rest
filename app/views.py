from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView
# Create your views here.


from  rest_framework.response import Response
from . serializer import *
from . models import *
from  rest_framework.views import APIView


from django.shortcuts import get_object_or_404
from rest_framework import   status

class Statedetails(ListCreateAPIView):
    serializer_class = stateSerializer
    queryset = ""
    def get(self,request,State_name=None):
        if State_name :
            statetid = get_object_or_404(State,State_name=State_name)
            serializer = stateSerializer(statetid)
            return Response(serializer.data , status= status.HTTP_200_OK)

        else:
            states = State.objects.all()
            serializer = stateSerializer(states,many=True)
            return Response(serializer.data ,status= status.HTTP_200_OK)



    




class citydetails(ListCreateAPIView):
    queryset = ""
    serializer_class = citySerializer


class towndetails(ListCreateAPIView):
    queryset = ""
    serializer_class = townSerializer



    