#Trabajo Practico
#Introduccion a la Programacion
#lenguaje: Python
#Nombre: Nicolás Trusz
#Email: nicolastrus@gmail.com
class Cliente:
    def __init__(self, nombre, edad, licencia, vip):
        self.nombre = nombre
        self.edad = edad
        self.licencia = licencia
        self.vip = vip

class Vehiculo:
    def __init__(self, modelo, disponible):
        self.modelo = modelo
        self.disponible = disponible

def verificar_disponibilidad(modelo):
    # Simulación de consulta de disponibilidad
    vehiculos_disponibles = ["camioneta", "auto 4 puertas", "convertible"]
    return modelo in vehiculos_disponibles

def obtener_tarifa(modelo):
    tarifas = {"camioneta": 50, "auto 4 puertas": 80, "convertible": 100}
    return tarifas.get(modelo, 0)

def mes_del_año(mes):
    meses = {"enero" : 20, "febrero": 20, "marzo": 10, "abril": 10, "mayo": 10, "junio": 10, "julio": 20, "agosto": 20, "septiembre": 10, "octubre": 10, "noviembre": 10, "diciembre": 10}
    return meses.get(mes,0)

def calcular_recargo(tipo_cliente):
    recargos = {"local": 10, "turista nacional": 15, "turista internacional": 20}
    return recargos.get(tipo_cliente, 0)

def obtener_seguro():
    return 30  # Seguro fijo

def calcular_descuento_vip(es_vip):
    return 10 if es_vip else 0

def alquiler_vehiculo():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    if edad < 25:
        print("No cumple con la edad mínima para alquilar.")
        return

    licencia = input("Ingrese tipo de licencia (municipal/nacional/internacional): ").lower()
    tipo_cliente = input("Ingrese tipo de cliente (local/turista nacional/turista internacional): ").lower()
    mes = input("Ingrese mes de alquiler (enero/febrero/marzo/abril/mayo/junio/julio/agosto/septiembre/octubre/noviembre/diciembre): ").lower()
    vip = input("¿Es cliente VIP? (si/no): ").lower() == "si"

    if licencia == "internacional" and tipo_cliente != "turista internacional":
        print("Licencia inválida para alquiler.")
        return

    modelo_vehiculo = input("Ingrese el modelo de vehículo deseado: ")
    if verificar_disponibilidad(modelo_vehiculo):
        print("Vehículo disponible.")
        
        tarifa = obtener_tarifa(modelo_vehiculo)
        recargo = calcular_recargo(tipo_cliente)
        seguro = obtener_seguro()
        descuento = calcular_descuento_vip(vip)
        temporada = mes_del_año(mes)
        total_pago = tarifa + recargo + seguro + temporada - descuento
        print(f"Total a pagar: {total_pago}")

        pago = float(input("Ingrese monto de pago: "))
        if pago < total_pago:
            print(f"Pago insuficiente, saldo pendiente: {total_pago - pago}")
        
        print("Alquiler confirmado. Disfrute su viaje.")
    else:
        print("Vehículo no disponible. Intente con otro modelo.")

alquiler_vehiculo()
