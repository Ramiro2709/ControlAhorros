from django.db import models

class Tipo_log(models.Model):
    # TODO Poner las opciones aca? 
    tipo = models.CharField(max_length=20) 
    def __str__(self):
        return ' %s '% (self.tipo)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30) 
    def __str__(self):
        return ' %s '% (self.nombre)

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=30) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return ' %s '% (self.nombre)

class Moneda(models.Model):
    nombre = models.CharField(max_length=30) 
    sigla = models.CharField(max_length=10) 
    def __str__(self):
        return ' %s '% (self.sigla)
    # TODO Valor?

class Plataforma(models.Model):
    nombre = models.CharField(max_length=30) 
    def __str__(self):
        return ' %s '% (self.nombre)

class Log(models.Model):
    # LINK[epic=options] Opciones 
    INGRESO = 1
    RETIRO = 2
    TRANSFERENCIA = 3
    TIPO_REGISTRO = [
        (INGRESO, 'Ingreso'),
        (RETIRO, 'Retiro'),
        (TRANSFERENCIA, 'Transferencia'),
    ]

    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=100) 
    # LINK[epic=foreign] Foreign Key, para 1 a muchos
    # tipo = models.ForeignKey(
    #     Tipo_log,
    #     on_delete=models.CASCADE,

    #     choices=TIPO_REGISTRO,
    #     default=1
    # )
    tipo = models.ForeignKey(Tipo_log,on_delete=models.CASCADE,null=True)
    categoria_origen = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='origen',null=True)
    subcat_origen = models.ForeignKey(Subcategoria,on_delete=models.CASCADE, related_name='origen',null=True)
    categoria_dest = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='destino',null=True)
    subcat_dest = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, related_name='destino',null=True)
    moneda_origen = models.ForeignKey(Moneda, on_delete=models.CASCADE, null=True, related_name='origen')
    monto_origen = models.DecimalField(max_digits=20, decimal_places=10)
    plataforma_or = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name='origen' , null=True)
    plataforma_des = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name='destino' , null=True)
    valorUSDC = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    valorBTC = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    comision = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    porcentaje_fijo = models.BooleanField(null=True)
    def __str__(self):
        return ' %s ; %s %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ;'% (self.fecha,self.descripcion,self.tipo,self.subcat_origen,self.subcat_dest,self.moneda_origen,self.monto_origen,self.valorBTC,self.valorUSDC,self.plataforma_or,self.plataforma_des)

# LINK[epic=inheritance] Heredacion de modelos, cada modelo como tabla independiente
class Log_Trade(Log):
    monto_dest = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    moneda_dest = models.ForeignKey(Moneda, on_delete=models.CASCADE, null=True, related_name='destino')
    precio = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    moneda_com = models.ForeignKey(Moneda, on_delete=models.CASCADE, null=True, related_name='comision')
    # super + extension?
    def __str__(self):
        return ' %s ; %s %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ;'% (self.fecha,self.descripcion,self.tipo,self.subcat_origen,self.subcat_dest,self.moneda_origen,self.monto_origen,self.valorBTC,self.valorUSDC,self.plataforma_or,self.plataforma_des)

class Tipo_fondo(models.Model):
    tipo = models.CharField(max_length=30) 
    interes = models.DecimalField(max_digits=10, decimal_places=10)


    
class Fondo(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null=True)
    monto = models.DecimalField(max_digits=20, decimal_places=10)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, null=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return ' %s ; %s ; %s ; %s'% (self.subcategoria,self.monto,self.moneda,self.plataforma)

