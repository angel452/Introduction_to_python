print("DETERMINANDO EL DIA, LA FECHA Y MES DE LOS DIAS TRANSCURRIDOS (+30 DIAS)")

dias = int(input("Ingrese el numero de dias trasncurridos: "))
#Con todo esto sacamos el dia de la semana
dias_2 = (dias+30)-4
dias_3 = dias_2 % 7
if dias_3 == 1:
    dia_semana = "domingo"
elif dias_3 == 2:
    dia_semana = "lunes"
elif dias_3 == 3:
    dia_semana = "martes"
elif dias_3 == 4:
    dia_semana = "miercoles"
elif dias_3 == 5:
    dia_semana = "jueves"
elif dias_3 == 6:
    dia_semana = "viernes"
elif dias_3 == 0:
    dia_semana = "sabado"

#con esto calculamos el mes y la fecha
total_dias = (dias +30)
if total_dias == 31:
    nombre_mes = "Enero"
    fecha=31
elif total_dias >= 32 and total_dias <= 60:
    nombre_mes = "Febrero"
    fecha=total_dias-31
elif total_dias >= 61 and total_dias <= 91:
    nombre_mes = "Marzo"
    fecha=total_dias-60
elif total_dias >= 92 and total_dias <= 121:
    nombre_mes = "Abril"
    fecha = total_dias-91
elif total_dias >= 122 and total_dias <= 152:
    nombre_mes = "Mayo"
    fecha = total_dias - 121
elif total_dias >= 153 and total_dias <= 182:
    nombre_mes = "Junio"
    fecha = total_dias - 152
elif total_dias >= 183 and total_dias <= 213:
    nombre_mes = "Julio"
    fecha = total_dias - 182
elif total_dias >= 214 and total_dias <= 244:
    nombre_mes = "Agosto"
    fecha = total_dias -213
elif total_dias >= 245 and total_dias <= 274:
    nombre_mes = "Septiembre"
    fecha = total_dias - 244
elif total_dias >= 275 and total_dias <= 305:
    nombre_mes = "Octubre"
    fecha = total_dias - 274
elif total_dias >= 306 and total_dias <= 335:
    nombre_mes = "Noviembre"
    fecha = total_dias -305
elif total_dias >= 336 and total_dias <= 366:
    nombre_mes = "Diciembre"
    fecha = total_dias - 335

#imprimimos todo
print(dia_semana, fecha, "de", nombre_mes)