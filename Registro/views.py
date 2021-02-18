from django.shortcuts import render
from django.http import HttpResponse
from Registro.forms import FormRegistro
from Registro.models import Log, Fondo
import decimal
from utils.functions import testFunction #De carpeta de funciones, para agregar la obtencion de valor de las monedas, etc...
from utils.functions import convertirMoneda

from PIL import Image

# Create your views here.

def home(request):
    return render(request, "Registro/index.html")

def registrar(request):
    #return render(request, "Registro/registrar.html")
    #return HttpResponse("Registro")
    if (request.method=="POST"):
        ## Cuando ya cargo informacion
        form = FormRegistro(request.POST)
        if (form.is_valid()):
            data = form.cleaned_data
            

            nuevo_log = Log(**data)
            #TODO actualizar valor de Bitcoin usando API
            moneda1 = nuevo_log.moneda_origen
            monto = nuevo_log.monto_origen
            sub = nuevo_log.subcat_dest
            pl_des = nuevo_log.plataforma_des

            # Guarda log con su conversion
            valorUSD = convertirMoneda(moneda1,"USD",monto)
            #print("Valor USD: %s" % valorUSD)
            nuevo_log.valorBTC = decimal.Decimal(2)
            nuevo_log.valorDAI = decimal.Decimal(valorUSD)
            nuevo_log.save()

            #TODO Plataforma origen? destino?
            fondoDest = Fondo.objects.filter(subcategoria=sub, moneda=moneda1, plataforma=pl_des).first()
            if (fondoDest):
                fondoDest.monto += monto
            else:
                fondoDest = Fondo(subcategoria=sub,monto=monto,moneda=moneda1,plataforma=pl_des)
            fondoDest.save()
                

            form = FormRegistro()
            return render(request,"Registro/registrar.html",{"form":form, "cargado":True, "data":data })
            #return HttpResponse("Registro cargado")
        else:
            ## Cuadno la informacion es incorrecta
            form = FormRegistro()
            return render(request,"Registro/registrar.html",{"form":form})
            #return HttpResponse("Error form")
    else:
        ## Primera vez que se ingresa al formulario
        form = FormRegistro()
    return render(request,"Registro/registrar.html",{"form":form})

def ver_logs(request):

    logs = Log.objects.all

    im = Image.open("bitcoin.png")
    im = im.rotate(90)
    #im.show()

    return render(request, "Registro/ver_logs.html",{"logs":logs})

def ver_fondos(request):
    fondos = Fondo.objects.all()

    return render(request, "Registro/ver_fondos.html", {"fondos":fondos})