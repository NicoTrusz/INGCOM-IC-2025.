#Trabajo Practico
#Introduccion a la Programacion
#lenguaje: Python
#Nombre: Nicolás Trusz
#        Pablo Alejandro Hernandez
#        Tania Belén Sanchez
#Email: nicolastrus@gmail.com
#Email: pabli.edu.ale@gmail.com
#Email: sanchez.taniabelen@gmail.com

# Este programa simula un sistema de alquiler de vehículos con diversas condiciones y tarifas.
def verificar_disponibilidad(modelo):
    # Simulación de consulta de disponibilidad
    vehiculos_disponibles = ["mini compactos", "pequeños", "compactos", "grandes", "de prestigio", "de lujo", "suv", "familiares"]
    return modelo in vehiculos_disponibles

def obtener_tarifa(modelo):
    tarifas = {"mini compactos": 50, "pequeños": 80, "compactos": 100, "grandes": 120,"de prestigio":140,"de lujo":160,"suv":180,"familiares":200}
    return tarifas.get(modelo, 0)

def equipamiento_vehiculo(equipo):
    equipamiento = {"sin":0 ,"cadenas":10,"neumaticos especiales":20 }
    return equipamiento.get(equipo,0)

def mes_del_año(mes):
    meses = {"enero" : 20, "febrero": 20, "marzo": 10, "abril": 10, "mayo": 10, "junio": 20, "julio": 20, "agosto": 20, "septiembre": 20, "octubre": 10, "noviembre": 10, "diciembre": 20}
    return meses.get(mes,0)

def tiempo_alquiler(dias):
    tarifas = {"diaria": 1, "fin de semana": 3, "semana": 5, "mes o superior": 30}
    return tarifas.get(dias, 0)

def calcular_recargo(tipo_cliente):
    recargos = {"local": 10, "turista nacional": 15, "turista internacional": 20}
    return recargos.get(tipo_cliente, 0)

def obtener_seguro():
    return 30  # Seguro fijo

def calcular_descuento_vip(es_vip):
    return 10 if es_vip else 0

def zona_geografica(lugar):
    zona = {"circuito chico":10,"cerro catedral":20,"ruta 40":100,}
    return zona.get(lugar,0)

def alquiler_vehiculo():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    if edad < 25:
        print("No cumple con la edad mínima para alquilar.")
        return

    licencia = input("Ingrese tipo de licencia (municipal/nacional/internacional): ").lower()
    tipo_cliente = input("Ingrese tipo de cliente (local/turista nacional/turista internacional): ").lower()
    permiso = input("¿Tiene permiso munisipal? (si/no): ").lower() 
    zona = input("Ingrese zona geografica (circuito chico/cerro catedral/ruta 40): ").lower()
    mes = input("Ingrese mes de alquiler (enero/febrero/marzo/abril/mayo/junio/julio/agosto/septiembre/octubre/noviembre/diciembre): ").lower()
    tiempo_de_alquiler = input("cantidad de tiempo de alquiler: (diaria/fin de semana/semana/mes o superior): ").lower()
    vip = input("¿Es cliente VIP? (si/no): ").lower() == "si"

    if licencia == "internacional" and tipo_cliente != "turista internacional":
        print("Licencia inválida para alquiler.")
        return

    modelo_vehiculo = input("Ingrese el modelo de vehículo deseado (mini compactos/pequeños/compactos/grandes/de prestigio/de lujo/suv/familiares): ").lower()
    if verificar_disponibilidad(modelo_vehiculo):
        print("Vehículo disponible.")
        equipamiento = input("Ingrese equipamiento deseado (sin/cadenas/neumaticos especiales): ").lower()
        tarifa = obtener_tarifa(modelo_vehiculo)
        recargo = calcular_recargo(tipo_cliente)
        seguro = obtener_seguro()
        lugar = zona_geografica(zona)
        descuento = calcular_descuento_vip(vip)
        temporada = mes_del_año(mes)
        tiempo = tiempo_alquiler (tiempo_de_alquiler)
        equipamiento_auto = equipamiento_vehiculo(equipamiento) 
        total_pago = (tarifa + recargo + seguro + temporada + equipamiento_auto + lugar )*tiempo - descuento
        print(f"Total a pagar: {total_pago}")

        pago = float(input("Ingrese monto de pago: "))
        if pago < total_pago:
            print(f"Pago insuficiente, saldo pendiente: {total_pago - pago}")
        
        print("Alquiler confirmado, permiso municipal:", permiso, ". Disfrute su viaje.")

    else:
        print("Vehículo no disponible. Intente con otro modelo.")

alquiler_vehiculo()
