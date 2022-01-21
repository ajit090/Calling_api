from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import company_details,contact
from .serializers import company_detailsSerializer,contactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


class company_detailsAPIView(APIView):
    model = company_details
    serializer_class = company_detailsSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        companys = company_details.objects.all()
        serializer = company_detailsSerializer(companys, many=True)
        return Response(serializer.data)

    
    
    def post(self,request):
        serializer = company_detailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','POST'])
def company_list(request):

    if request.method=='GET':
        companys = company_details.objects.all()
        serializer = company_detailsSerializer(companys,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=company_detailsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    try:
        companys = company_details.objects.get(pk=pk)
    except company_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = company_detailsSerializer(companys)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = company_detailsSerializer(companys,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        companys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class contactAPIView(APIView):
    model = contact()
    serializer_class = contactSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        companys = company_details.objects.all()
        serializer = company_detailsSerializer(companys, many=True)
        return Response(serializer.data)

    
    
    def post(self,request):
        serializer = contactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def contact_list(request):

    if request.method=='GET':
        contacts = contact.objects.all()
        serializer = contactSerializer(contacts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=contactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    try:
        contacts = contact.objects.get(pk=pk)
    except contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = contactSerializer(contacts)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = contactSerializer(contacts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contacts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
