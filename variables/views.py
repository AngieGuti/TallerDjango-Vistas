from .logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


#Ventajas:
#Es más flexible, ya que permite manejar casos donde el id no es obligatorio (por ejemplo, para listar todos los recursos si no se proporciona un id).
#Es útil para APIs que necesitan soportar múltiples parámetros opcionales.

@csrf_exempt
def variables_view(request): # Get id query parameter
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            variable_dto = vl.get_variable(id)
            variable = serializers.serialize('json', [variable_dto,]) 
            #La serialización es el proceso de convertir objetos de Python (como los resultados de una consulta de Django) en un formato que puede ser transmitido por la red, como JSON
            return HttpResponse(variable, 'application/json')
        else:
            variables_dto = vl.get_variables()
            variables = serializers.serialize('json', variables_dto)
            return HttpResponse(variables, 'application/json')

    if request.method == 'POST':
        variable_dto = vl.create_variable(json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')



#Ventajas:
#Es más limpio y RESTful, ya que sigue el estándar de usar la URL para identificar recursos.
#Es más intuitivo para APIs que siguen el estilo REST.

@csrf_exempt
def variable_view(request, pk): #Get by id (pk)
    if request.method == 'GET':
        variable_dto = vl.get_variable(pk)
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

    if request.method == 'PUT':
        variable_dto = vl.update_variable(pk, json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')
    
