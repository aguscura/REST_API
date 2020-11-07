from rest_framework import serializers
from . models import operacion

class operacionSerializers(serializers.ModelSerializer):
    class MetaData:

        model = operacion
        fields = "__all__" #Importa TODAS los campos de la clase Operacion.

    