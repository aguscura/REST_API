from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import operacion
from . serializers import operacionSerializers
from . forms import operacionform
import pickle
import json
import numpy as np
from django.contrib import messages

# Create your views here.


class operacionViews(viewsets.ModelViewSet):
    queryset = operacion.objects.all() #Cada vez que pida una requests van a estar TODOS los objetos puestos en Operacion. 
    serializer_class = operacionSerializers #Y usará el OperacionSerializer.

# @api_view(["POST"]) #Decorador, no se bien para que es.
def approvereject(dic): #Funcion que le doy la request y me dice si está OK.

    try:

        def SUMA(num1, num2):
            resultado = num1 + num2
            return resultado

        def RESTA(num1, num2):
            resultado = num1 - num2
            return resultado

        def MULTIPLICACION(num1, num2):
            resultado = num1 * num2       
            return resultado 

        def DIVISION(num1, num2):
            resultado = num1 / num2
            return resultado

        data = dic["operacion_math"] #Los valores del dicc (No las keys) se van a una lista.
        num1 = int(dic["num1"])
        num2 = int(dic["num2"])

        if data == "SUMA":
            resultado = SUMA(num1,num2)

        elif data == "RESTA":
            resultado = RESTA(num1,num2)
 
        elif data == "MULTIPLICACION":
            resultado = MULTIPLICACION(num1,num2)
        
        elif data == "DIVISION":
            resultado = DIVISION(num1,num2)

        # respuesta_json = JsonResponse("El resultado de la operacion es: " + str(resultado), safe= False
        return str(resultado)

    except ValueError as error:

        return Response(error.args[0], status.HTTP_400_BAD_REQUEST) 

        

def cxcontact(request): #En vez de usar el decorador de arriba, que solo servía para POST, este me va a dejar cualquier request.
    
    if request.method == "POST": #Si es un metodo post, arma un form con todos los datos.
        form = operacionform(request.POST)
        if form.is_valid():
            operacion_math = form.cleaned_data['operacion_math']
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            print(operacion_math)

            mydict = (request.POST).dict() #Todo lo que le mande en la request lo va a convertir en Diccionario.

            respuesta = approvereject(mydict)
            messages.success(request, "El resultado de la operación es: {} ".format(respuesta))

    else:
        form = operacionform() #Si no es un metodo post, devuelve el coso vacio. 

    return render(request, 'myform/cxform.html', {'form':form})
