from django.shortcuts import render

import os
import random
from django.conf import settings
from django.shortcuts import render

def home(request):
    # --- Lógica de Oyentes (Random) ---
    oyentes_random = random.randint(1000, 2500)
    oyentes_formateados = "{:,}".format(oyentes_random)

    # --- Lógica de Galería (Trayectoria) ---
    # Construimos la ruta hacia la carpeta trayectoria
    img_path = os.path.join(settings.BASE_DIR, 'viewradio', 'static', 'viewradio', 'assets', 'img', 'trayectoria')
    
    lista_imagenes = []
    if os.path.exists(img_path):
        # Filtramos solo .jpeg o .jpg
        lista_imagenes = [f for f in os.listdir(img_path) if f.lower().endswith(('.jpeg', '.jpg'))]
        lista_imagenes.sort()
    else:
        print(f"ALERTA: No se encontró la carpeta en {img_path}")

    # --- Lógica HTMX ---
    is_htmx = request.headers.get('HX-Request') == 'true'

    # Enviamos TODO al context de home.html
    context = {
        'oyentes': oyentes_formateados,
        'imagenes': lista_imagenes,
        'is_htmx': is_htmx,
    }

    return render(request, 'viewradio/home.html', context)

def programas(request):
    # Esta línea es vital para que el template sepa qué base usar
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    context = {
        'is_htmx': is_htmx,
    }
    return render(request, 'viewradio/programas.html', context)
def inmobiliaria(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
    return render(request, 'viewradio/inmobiliaria.html', {'is_htmx': is_htmx})

def studio_live(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
    return render(request, 'viewradio/studio_live.html', {'is_htmx': is_htmx})

def contacto(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
    return render(request, 'viewradio/contacto.html', {'is_htmx': is_htmx})

import random

def tu_vista(request):
    oyentes_random = random.randint(1000, 2500)
    # Formatear con comas: 1,284
    oyentes_formateados = "{:,}".format(oyentes_random)
    
    return render(request, 'home.html', {
        'oyentes': oyentes_formateados,
        'is_htmx': request.headers.get('HX-Request') == 'true'
    })

import os
from django.conf import settings
from django.shortcuts import render

def trayectoria_galeria(request):
    # Esta línea construye la ruta buscando la carpeta 'static' dentro de tu app 'viewradio'
    img_path = os.path.join(settings.BASE_DIR, 'viewradio', 'static', 'viewradio', 'assets', 'img', 'trayectoria')
    
    # Imprime la ruta en la terminal donde corres el 'runserver' para verificar
    print(f"--- RUTA BUSCADA: {img_path} ---")

    lista_imagenes = []
    
    if os.path.exists(img_path):
        # Buscamos archivos .jpeg y .jpg (en minúsculas o mayúsculas)
        lista_imagenes = [f for f in os.listdir(img_path) if f.lower().endswith(('.jpeg', '.jpg'))]
        # Ordenamos por nombre para que la 1 vaya antes que la 49
        lista_imagenes.sort()
    else:
        print("--- LA CARPETA NO EXISTE EN ESA RUTA ---")

    return render(request, 'viewradio/home.html', {'imagenes': lista_imagenes})