from django import forms
from Registro.models import Subcategoria, Moneda, Tipo_log,Plataforma
import datetime

class FormRegistro(forms.Form):
    fecha = forms.DateTimeField(initial=datetime.date.today)
    descripcion = forms.CharField()
    tipo = forms.ModelChoiceField(
        queryset = Tipo_log.objects.all(),
        widget = forms.Select(attrs={"onChange":'tipoUpdate()'})
    )
    #subcat_origen = forms.Select(choices= Subcategoria.objects.all())
    subcat_origen = forms.ModelChoiceField(queryset=Subcategoria.objects.all())
    subcat_dest = forms.ModelChoiceField(queryset=Subcategoria.objects.all())
    moneda_origen = forms.ModelChoiceField(queryset=Moneda.objects.all())
    monto_origen = forms.DecimalField()
    plataforma_or = forms.ModelChoiceField(queryset=Plataforma.objects.all())
    plataforma_des = forms.ModelChoiceField(queryset=Plataforma.objects.all())

    #valorDai ? automatico?