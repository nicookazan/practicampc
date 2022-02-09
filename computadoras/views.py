from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from computadoras.forms import *
from computadoras.models import *


def bienvenido(request):

    compus = Computadora.objects.order_by('id')
    return render(request, 'bienvenido.html', {'compus':compus})

def nuevaPC(request):
    if request.method == 'POST':
        formaCompu = CompuForm(request.POST)
        if formaCompu.is_valid():
            formaCompu.save()
            return redirect('index')
    else:
        formaCompu = CompuForm()

    return render(request, 'nueva_pc.html', {'formaCompu': formaCompu})

def detalle_compu(request, id):
    compu = get_object_or_404(Computadora, pk=id)
    return render(request, 'detalle_compu.html', {'compu': compu})

def editar_compu(request, id):
    compu = get_object_or_404(Computadora, pk=id)
    if request.method == 'POST':
        formaCompu = CompuForm(request.POST, instance=compu)
        if formaCompu.is_valid():
            formaCompu.save()
            return redirect('index')
    else:
        formaCompu = CompuForm(instance=compu)

    return render(request, 'editar_pc.html', {'formaCompu':formaCompu})

def eliminar_compu(request, id):
    compu = get_object_or_404(Computadora, pk=id)
    if compu:
        compu.delete()
    return redirect('index')

def carga_mon(request):
    monitores = Monitor.objects.order_by('id')
    return render(request, 'monitores/monitores.html', {'monitores':monitores})

def carga_rat(request):
    ratones = Mouse.objects.order_by('id')
    return render(request, 'ratones/ratones.html', {'ratones':ratones})

def carga_tec(request):
    teclados = Teclado.objects.order_by('id')
    return render(request, 'teclados/teclados.html', {'teclados':teclados})

def nuevo_monitor(request):
    if request.method == 'POST':
        formaMon = MonitorForm(request.POST)
        if formaMon.is_valid():
            formaMon.save()
            return redirect('mon')
    else:
        formaMon = MonitorForm()

    return render(request, 'monitores/nuevo_monitor.html', {'formaMon': formaMon})

def detalle_mon(request, id):
    monitor = get_object_or_404(Monitor, pk=id)
    return render(request, 'monitores/detalle_monitor.html', {'monitor': monitor})

def editar_mon(request,id):
    monitor = get_object_or_404(Monitor, pk=id)
    if request.method == 'POST':
        formaMon = MonitorForm(request.POST, instance=monitor)
        if formaMon.is_valid():
            formaMon.save()
            return redirect('mon')
    else:
        formaMon = MonitorForm(instance=monitor)

    return render(request, 'monitores/editar_mon.html', {'formaMon':formaMon})

def eliminar_mon(request, id):
    monitor = get_object_or_404(Monitor, pk=id)
    if monitor:
        monitor.delete()
    return redirect('mon')

def nuevo_tec(request):
    if request.method == 'POST':
        formaTec = TecladoForm(request.POST)
        if formaTec.is_valid():
            formaTec.save()
            return redirect('tec')
    else:
        formaTec = TecladoForm()
    return render(request, 'teclados/nuevo_teclado.html', {'formaTec': formaTec})

def detalle_tec(request, id):
    teclado = get_object_or_404(Teclado, pk=id)
    return render(request, 'teclados/detalle_teclado.html', {'teclado': teclado})

def editar_tec(request, id):
    teclado = get_object_or_404(Teclado, pk=id)
    if request.method == 'POST':
        formaTec = TecladoForm(request.POST, instance=teclado)
        if formaTec.is_valid():
            formaTec.save()
            return redirect('tec')
    else:
        formaTec = TecladoForm(instance=teclado)

    return render(request, 'teclados/editar_teclado.html', {'formaTec':formaTec})

def eliminar_tec(request, id):
    teclado = get_object_or_404(Teclado, pk=id)
    if teclado:
        teclado.delete()
    return redirect('tec')

def nuevo_raton(request):
    if request.method == 'POST':
        formaRat = MouseForm(request.POST)
        if formaRat.is_valid():
            formaRat.save()
            return redirect('rat')
    else:
        formaRat = MouseForm()
    return render(request, 'ratones/nuevo_raton.html', {'formaRat': formaRat})

def detalle_raton(request, id):
    raton = get_object_or_404(Mouse, pk=id)
    return render(request, 'ratones/detalle_raton.html', {'raton':raton})

def editar_raton(request, id):
    raton = get_object_or_404(Mouse, pk=id)
    if request.method == 'POST':
        formaRat = MouseForm(request.POST, instance=raton)
        if formaRat.is_valid():
            formaRat.save()
            return redirect('rat')
    else:
        formaRat = MouseForm(instance=raton)

    return render(request, 'ratones/editar_raton.html', {'formaRat':formaRat})

def eliminar_raton(request, id):
    raton = get_object_or_404(Mouse, pk=id)
    if raton:
        raton.delete()
    return redirect('rat')