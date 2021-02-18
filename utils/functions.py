from Registro.models import Moneda
import decimal

def testFunction():
    return "test function"




def convertirMoneda(moneda1, moneda2, monto):
    if (moneda1.sigla == "ARS" and moneda2 == "USD"):
        #print(type(monto))
        return monto * getARStoUSDvalue()
    else: return -1


def getBTCtoUSDvalue():
    value = 48960
    return value

def getUSDtoARSvalue():
    value = 160
    return decimal.Decimal(value)

def getARStoUSDvalue():
    value = 0.00625
    return decimal.Decimal(value)