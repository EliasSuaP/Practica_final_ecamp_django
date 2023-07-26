from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from django.http import HttpResponse

# Create your views here.

def index(request):
    """ 
    Se muestra el template con el formulario para llenar y crear objetos.
    Se realiza una comprobación si se está enviando el formulario toma los datos de los campos para crear
    un objeto en la base de dato. Al crear un objeto responde con un mensaje de éxito.
    """
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        Laboratorio.objects.create(
            nombre = nombre,
            ciudad = ciudad,
            pais = pais
        )
        return HttpResponse('El laboratorio se ha creado con éxito')
    else:
        return render(request, 'index.html')


def laboratorios(request):
    """ Se instancia el modelo laboratorio para entregarselo al template 
    y desde ahí instanciar y renderizar su contenido.
    """
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorios.html', {'laboratorios': laboratorios})


def editar(request, laboratorio_id):
    """ 
    Renderiza un formulario que permite editar los campos del laboratorio seleccionado.
    En caso de enviar el formulario recibe a través de la url el id del laboratorio se busca si existe en el models Laboratorio 
    para obtener sus datos, se realiza una comprobación si se ha enviado un formulario obtiene todos los campos, los modifica y guarda la accion redireccionando al inicio.
    """
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')

        laboratorio.nombre = nombre
        laboratorio.ciudad = ciudad
        laboratorio.pais = pais

        laboratorio.save()
        return redirect('index')
    else:
        return render(request, 'editar.html', {'laboratorio': laboratorio})
    

def eliminar(request, laboratorio_id):
    """ 
    Se recibe la id del laboratorio mediante url se busca la coincidencia en el models
    y elimina el registro seleccionado, finalmente redirige a la información de los laboratorios.
    """
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    laboratorio.delete()
    return redirect('laboratorios')

    