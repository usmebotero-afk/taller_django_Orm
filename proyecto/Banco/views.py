from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Cuenta  # Importamos tu modelo

def listar_cuentas(request):
    # Esto equivale a un: SELECT * FROM cuenta;
    cuentas = Cuenta.objects.all() 
    
    # Enviamos los datos al HTML mediante el diccionario de contexto
    return render(request, 'gestionCuentas.html', {'cuentas': cuentas})

# VISTA 2: Solo se encarga de insertar (INSERT)
def registrar_cuenta(request):
    if request.method == 'POST':
        v_tipocuenta = request.POST.get('txtTipoCuenta')
        v_descripcion = request.POST.get('txtDescripcion')
        v_saldo = request.POST.get('txtSaldo')
        
        Cuenta.objects.create(
            tipocuenta=v_tipocuenta,
            descripcion=v_descripcion,
            saldo=v_saldo
        )
    # Al terminar de insertar, redirige a la vista de consultas para actualizar la tabla
    return redirect('listar_cuentas')

#VISTA 3: Eliminar (DELETE)
def eliminar_cuenta(request, cuenta_id):
        cuenta= Cuenta.objects.get(Cuenta, id= id)

        cuenta.delete()
        
        return redirect('listar_cuentas')

def actualizar_cuenta(request, id):
    cuenta = Cuenta.objects.get(pk=id)

    if request.method == 'POST':
        cuenta.tipocuenta = request.POST.get('txtTipoCuenta')
        cuenta.descripcion = request.POST.get('txtDescripcion')
        cuenta.saldo = request.POST.get('txtSaldo')
        cuenta.save()
        return redirect('listar_cuentas')

    # Si es GET, solo muestra el formulario con los datos actuales
    return render(request, 'editarCuenta.html', {'cuenta': cuenta})