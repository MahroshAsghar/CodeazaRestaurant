
from django.http import JsonResponse
from itsdangerous import Serializer
from .models import FastFood
from .serializers import FastFoodSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

def menu(request, safe=False):
          return render(request, "restaurant/menu.html",{})

@api_view(['GET','POST'])

def FastFood_list(request, format=None):
 #get all the drinks
 #serialize them
 #return json 
 if request.method== 'GET':
   fastfood= FastFood.objects.all()
   serializer=FastFoodSerializer(fastfood, many=True)
   return JsonResponse({'FastFood': serializer.data})
 if request.method=='POST':
    serializer=FastFoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def fastfood_detail(request,id,format=None):
    try:
     fastfood= FastFood.objects.get(pk=id)
    except FastFood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer= FastFoodSerializer(fastfood)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=FastFoodSerializer(fastfood,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        fastfood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        