from datetime import datetime, timedelta

horario=input("ingrese horario: ")
horas=0

if horario == "":
     horas=datetime.now()
else:
    horas=datetime.strptime(horario,"%H.%M.%S")

hora=horas.hour
minutos=horas.minute
segundos=horas.second
if minutos in range (1,5):
    minutos=("y cinco")
elif minutos in range (6,10):
    minutos=("y diez")
elif minutos in range (11,15):
    minutos=("y cuarto")
elif minutos in range (16,20):
    minutos=("y veinte")
elif minutos in range (21,25):
    minutos=("y  veinti cinco")
elif minutos in range (26,30):
    minutos=("y media")
elif minutos in range (31,35):
    minutos=("y treinta y cinco")
elif minutos in range (36,40):
    minutos=("y cuarenta")
elif minutos in range (41,45):
    hora=horas+timedelta(hours=1)
    minutos=("menos cuarto")
elif minutos in range (46,50):
    hora=horas+timedelta(hours=1)
    minutos=("menos diez")
elif minutos in range (51,55):
    hora=horas+timedelta(hours=1)
    minutos=("menos cinco")
elif minutos in range (56,59):
    hora=horas+timedelta(hours=1)
    minutos=("en punto")
hora=hora.hour
if hora==1:
    hora=("una")
elif hora==2:
    hora=("dos")
elif hora==3:
    hora=("tres")
elif hora==4:
    hora=("cuatro")
elif hora==5:
    hora=("cinco")
elif hora==6:
    hora=("seis")
elif hora==7:
    hora=("siete")
elif hora==8:
    hora=("ocho")
elif hora==9:
    hora=("nueve")
elif hora==10:
    hora=("diez")
elif hora==11:
    hora=("once")
elif hora==12:
    hora=("doce")
elif hora==13:
    hora=("trece")
elif hora==14:
    hora=("catorce")
elif hora==15:
    hora=("quince")
elif hora==16:
    hora=("dieciseis")
elif hora==17:
    hora=("diecisiete")
elif hora==18:
    hora=("dieciocho")
elif hora==19:
    hora=("diecinueve")
elif hora==20:
    hora=("veinte")
elif hora==21:
    hora=("veinti una")
elif hora==22:
    hora=("veinti dos")
elif hora==23:
    hora=("veinti tres")
elif hora==24:
    hora=("veinti cuatro")

print(f"la hora es:{hora} {minutos}")
