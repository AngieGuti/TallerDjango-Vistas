from ..models import Variable

def get_variables():
    variables = Variable.objects.all() #objects.all() permite buscar todos los elementos en una tabla
    return variables

#Get by id (pk)
def get_variable(var_pk):
    variable = Variable.objects.get(pk=var_pk)
    return variable

#Update by id (pk) and new data
def update_variable(var_pk, new_var):
    variable = get_variable(var_pk)
    variable.name = new_var["name"]
    variable.save()
    return variable

def create_variable(var):
    variable = Variable(name=var["name"])
    variable.save()
    return variable