from django.shortcuts import render
from django.http import HttpResponse
from Registro.forms import FormRegistro,FormRegistroTrade
from Registro.models import Log, Fondo, Log_Trade
import decimal
from utils.functions import testFunction #De carpeta de funciones, para agregar la obtencion de valor de las monedas, etc...
from utils.functions import convertirMoneda
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, View

from PIL import Image

# Create your views here.

def home(request):
    return render(request, "Registro/index.html")

def registrar(request,tipo):
    #return render(request, "Registro/registrar.html")
    #return HttpResponse("Registro")
    if (request.method=="POST"):
        ## Cuando ya cargo informacion
        if (tipo == "trade"): form = FormRegistroTrade(request.POST)
        else: form = FormRegistro(request.POST)
        if (form.is_valid()):
            data = form.cleaned_data
            
            # Si es un trade, carg aun trade
            if (tipo == "trade"): 
                nuevo_log = Log_Trade(**data)
            else: 
                nuevo_log = Log(**data)
                

            #TODO actualizar valor de Bitcoin usando API
            moneda1 = nuevo_log.moneda_origen
            monto1 = nuevo_log.monto_origen
            sub1 = nuevo_log.subcat_origen
            pl_or = nuevo_log.plataforma_or
            sub2 = nuevo_log.subcat_dest
            pl_des = nuevo_log.plataforma_des
            if (tipo == "trade"):
                moneda2 = nuevo_log.moneda_dest
                monto2 = nuevo_log.monto_dest

            # Guarda log con su conversion
            valorUSD = convertirMoneda(moneda1,"USD",monto1)
            #print("Valor USD: %s" % valorUSD)
            nuevo_log.valorBTC = decimal.Decimal(2)
            nuevo_log.valorUSDC = decimal.Decimal(valorUSD)
            
            nuevo_log.save()

            #NOTE Si es un trade, suman la moneda destino, sino, la origen
            if (tipo == "trade"):
                moneda = moneda2
                monto = monto2
            else:
                moneda = moneda1
                monto = monto1

            #NOTE Plataforma de origen, resta
            
            fondoOr = Fondo.objects.filter(subcategoria=sub1, moneda=moneda1, plataforma=pl_or).first()
            if (fondoOr):
                fondoOr.monto -= monto
                # FIXME Si quedan fondos negativos? Dejar?
            #else:
                # FIXME Fondos no existen
                fondoOr.save()



            #NOTE Plataforma destino, suma
            fondoDest = Fondo.objects.filter(subcategoria=sub2, moneda=moneda, plataforma=pl_des).first()
            if (fondoDest):
                fondoDest.monto += monto
            else:
                fondoDest = Fondo(subcategoria=sub2,monto=monto,moneda=moneda,plataforma=pl_des)
            fondoDest.save()
                
            if (tipo == "trade"): form = FormRegistroTrade()
            else: form = FormRegistro()
            return render(request,"Registro/registrar.html",{"form":form, "cargado":True, "data":data })
            #return HttpResponse("Registro cargado")
        else:
            ## Cuadno la informacion es incorrecta
            form = FormRegistro()
            return render(request,"Registro/registrar.html",{"form":form})
            #return HttpResponse("Error form")
    else:
        ## Primera vez que se ingresa al formulario
        if (tipo == "trade"): form = FormRegistroTrade()
        else: form = FormRegistro()
        #form = FormRegistroTrade()
    return render(request,"Registro/registrar.html",{"form":form})

def ver_logs(request):

    logs = Log.objects.all

    im = Image.open("bitcoin.png")
    im = im.rotate(90)
    #im.show()

    return render(request, "Registro/ver_logs.html",{"logs":logs})





#class FormPartidos(FormView):
#    template_name = 'configuracion/formularios/form_partidos.html'
#    form_class = FormPartidos

#LINK[epic=class_views]
class VerFondos(TemplateView):
    #fondos = Fondo.objects.all()
    #NOTE Nombre del template que carga el view
    template_name = 'Registro/ver_fondos.html'

    #NOTE Funcion para setear el contexto (variables) del template
    # *args : para enviar una lista de argumentos, de tamaño variable
    # **kwargs: enviar un diccionario de argumentos con keywords
    def get_context_data(self, **kwargs):
        try:
            context = super(VerFondos, self).get_context_data(**kwargs)
            context['fondos'] = Fondo.objects.all()
        except Exception as e:
            print("Error al obtener datos de contexto.")
            print(e)
        return context

#def ver_fondos(request):
#    fondos = Fondo.objects.all()
#   return render(request, "Registro/ver_fondos.html", {"fondos":fondos})