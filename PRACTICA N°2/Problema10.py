# Problema 10: Convertir fechas al formato AAAA-MM-DD
def fecha(fecha):
    meses = [
        "Enero", 
        "Febrero", 
        "Marzo", 
        "Abril", 
        "Mayo", 
        "Junio", 
        "Julio", 
        "Agosto",
        "Septiembre", 
        "Octubre", 
        "Noviembre", 
        "Diciembre"
    ]
    if '/' in fecha:
        mes, dia, año = fecha.split('/')
        
        return f"{año}-{int(mes):02}-{int(dia):02}"
    else:
        fecha = fecha.replace(',', '')
        mes_p, dia, año = fecha.split(' ')
        mes_n = meses.index(mes_p) + 1
        
        return f"{año}-{mes_n:02}-{int(dia):02}"

def convertir_texto():
    fecha_u = input("Ingrese la fecha 'Mes Día, Año'): ")
    print("Fecha en formato AAAA-MM-DD:", fecha(fecha_u))

convertir_texto()
