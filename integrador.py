import datetime

# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, apellido, dni, edad, origen,
                 licencia_vigente=True, licencia_internacional=False,
                 vip=False, tarjeta_vip=None,
                 forma_pago=None, contacto_agencia=None):
        """
        tarjeta_vip es un diccionario con:
           - 'fecha_vencimiento' (str o datetime)
           - 'descuento' (porcentaje, ej. 10 para 10%)
        """
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.origen = origen  # 'local', 'turista nacional' o 'internacional'
        self.licencia_vigente = licencia_vigente
        self.licencia_internacional = licencia_internacional
        self.vip = vip
        self.tarjeta_vip = tarjeta_vip
        self.forma_pago = forma_pago
        self.contacto_agencia = contacto_agencia

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"


# Clase que representa un vehículo
class Vehiculo:
    def __init__(self, patente, modelo, numero_chasis, motor, tipo,
                 en_bariloche=False, es_4x4=False, equipamiento_invierno=False, permiso_municipal=None):
        self.patente = patente
        self.modelo = modelo
        self.numero_chasis = numero_chasis
        self.motor = motor
        self.tipo = tipo  # Ej: 'auto 4 puertas', 'camioneta', 'convertible', etc.
        self.en_bariloche = en_bariloche  # Indica si el vehículo tiene atributos especiales
        # Atributos especiales para Bariloche
        self.es_4x4 = es_4x4
        self.equipamiento_invierno = equipamiento_invierno
        self.permiso_municipal = permiso_municipal

    def __str__(self):
        return f"{self.modelo} (Patente: {self.patente})"


# Clase que representa una tarifa de alquiler
class Tarifa:
    def __init__(self, codigo, nombre, importe, tarifa_tipo):
        """
        tarifa_tipo: 'diaria', 'fin de semana', 'semana', 'mes o superior'
        importe: valor base por período definido
        """
        self.codigo = codigo
        self.nombre = nombre
        self.importe = importe  # importe base
        self.tarifa_tipo = tarifa_tipo
        # En Bariloche pueden aplicarse recargos adicionales
        self.recargo = 0

    def calcular_costo(self, dias):
        """Calcula costo base multiplicando el importe por la cantidad de días y sumando recargo"""
        return self.importe * dias + self.recargo

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}, Importe: {self.importe})"


# Clase que representa un seguro
class Seguro:
    def __init__(self, codigo, nombre, importe):
        self.codigo = codigo
        self.nombre = nombre
        self.importe = importe

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}, Importe: {self.importe})"


# Clase que representa una factura de alquiler
class Factura:
    def __init__(self, numero, cliente, vehiculo, tarifa, seguro, periodo_dias, recargos=0, descuento=0):
        self.numero = numero
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.tarifa = tarifa
        self.seguro = seguro
        self.periodo_dias = periodo_dias
        self.recargos = recargos
        self.descuento = descuento
        self.fecha_emision = datetime.date.today()
        self.total = self.calcular_total()

    def calcular_total(self):
        """
        El total se calcula como:
         (tarifa base * días) + seguro + recargos – descuento
        """
        base = self.tarifa.importe * self.periodo_dias
        total = base + self.seguro.importe + self.recargos - self.descuento
        return total

    def __str__(self):
        return (f"Factura #{self.numero}\n"
                f"  Cliente: {self.cliente}\n"
                f"  Vehículo: {self.vehiculo}\n"
                f"  Tarifa: {self.tarifa.nombre} x {self.periodo_dias} día/s\n"
                f"  Seguro: {self.seguro.nombre}\n"
                f"  Recargos: {self.recargos}\n"
                f"  Descuento: {self.descuento}\n"
                f"  Total a pagar: {self.total}\n"
                f"  Fecha: {self.fecha_emision}")


# Clase que representa un pago
class Pago:
    def __init__(self, dni, fecha, factura_numero, importe, saldo_pendiente):
        self.dni = dni
        self.fecha = fecha
        self.factura_numero = factura_numero
        self.importe = importe
        self.saldo_pendiente = saldo_pendiente

    def __str__(self):
        return (f"Pago - DNI: {self.dni}, Factura: {self.factura_numero}, "
                f"Importe abonado: {self.importe}, Saldo pendiente: {self.saldo_pendiente}")


# Clase que modela el sistema de alquiler
class RentalSystem:
    def __init__(self):
        self.clientes = []
        self.vehiculos = []
        self.facturas = []
        self.pagos = []
        self.next_factura_num = 1

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def add_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def buscar_vehiculo_por_modelo(self, modelo):
        """Devuelve el primer vehículo disponible que coincida con el modelo solicitado"""
        disponibles = [v for v in self.vehiculos if v.modelo.lower() == modelo.lower()]
        return disponibles[0] if disponibles else None

    def procesar_alquiler(self, cliente, modelo, periodo_dias, tarifa, seguro):
        """
        Procedimiento de alquiler:
          1. Validación de requisitos:
             - Edad mínima 25 años.
             - Licencia vigente.
             - Si el cliente no es local, debe tener licencia internacional.
          2. Buscamos el vehículo (por modelo).
          3. Calculamos descuento VIP si corresponde.
          4. Generamos la factura.
        """
        # 1. Validaciones
        if cliente.edad < 25:
            print("Rechazo de alquiler: Edades menor a 25 años.")
            return None
        if not cliente.licencia_vigente:
            print("Rechazo de alquiler: Licencia no vigente.")
            return None
        if cliente.origen != 'local' and not cliente.licencia_internacional:
            print("Rechazo de alquiler: Turista sin licencia internacional.")
            return None

        # 2. Buscar vehículo disponible
        vehiculo = self.buscar_vehiculo_por_modelo(modelo)
        if vehiculo is None:
            print("Rechazo de alquiler: Vehículo no disponible. Se registra el motivo del rechazo.")
            return None

        # 3. Cálculo de descuento VIP
        descuento = 0
        if cliente.vip and cliente.tarjeta_vip:
            # Se asume que se descuenta sobre la tarifa base (importe * días)
            descuento = (tarifa.importe * periodo_dias) * (cliente.tarjeta_vip.get('descuento', 0) / 100)

        # 4. Generar factura
        factura = Factura(self.next_factura_num, cliente, vehiculo, tarifa, seguro, periodo_dias,
                          recargos=tarifa.recargo, descuento=descuento)
        self.facturas.append(factura)
        self.next_factura_num += 1

        print("Alquiler procesado correctamente. Se ha generado la siguiente factura:")
        print(factura)
        return factura

    def registrar_devolucion(self, factura_numero):
        """Simula el registro de devolución del vehículo."""
        factura = next((f for f in self.facturas if f.numero == factura_numero), None)
        if factura is None:
            print("Error: Factura no encontrada para la devolución.")
            return
        print("\nRegistro de devolución:")
        print(" - Vehículo devuelto.")
        print(" - Copia de la factura enviada al cliente y archivada.")

    def registrar_pago(self, dni, factura_numero, importe, fecha=datetime.date.today()):
        """Registra un pago parcial o total para una factura.
           Se evita registrar pagos que excedan el saldo pendiente."""
        factura = next((f for f in self.facturas if f.numero == factura_numero), None)
        if factura is None:
            print("Error: Factura no encontrada.")
            return

        # Sumar pagos previos para esa factura
        total_pagado = sum(p.importe for p in self.pagos if p.factura_numero == factura_numero)
        saldo = factura.total - total_pagado

        if importe > saldo:
            print("Error: El importe del pago excede el saldo pendiente. Pago no aceptado.")
            return

        nuevo_pago = Pago(dni, fecha, factura_numero, importe, saldo - importe)
        self.pagos.append(nuevo_pago)
        print("Pago registrado exitosamente:")
        print(nuevo_pago)


# Función principal que simula el proceso
def main():
    system = RentalSystem()

    # Agregar vehículos (algunos con atributos especiales para Bariloche)
    veh1 = Vehiculo(patente="ABC123", modelo="Sedan", numero_chasis="CH123", motor="MTR123",
                    tipo="auto 4 puertas", en_bariloche=True, es_4x4=False, equipamiento_invierno=True,
                    permiso_municipal="PM456")
    veh2 = Vehiculo(patente="XYZ789", modelo="SUV", numero_chasis="CH789", motor="MTR789",
                    tipo="camioneta")
    system.add_vehiculo(veh1)
    system.add_vehiculo(veh2)

    # Crear tarifas (se puede ampliar según el tipo de tarifa)
    tarifa_diaria = Tarifa(codigo="T01", nombre="Tarifa Diaria", importe=100, tarifa_tipo="diaria")
    tarifa_diaria.recargo = 20  # Ejemplo de recargo (por temporada alta o zona)
    
    # Crear seguros
    seguro_basico = Seguro(codigo="S01", nombre="Seguro Básico", importe=15)
    # En Bariloche se podrían agregar seguros especiales, si es necesario.

    # Crear clientes
    client1 = Cliente(nombre="Juan", apellido="Pérez", dni="12345678", edad=30, origen="local", # colocar en un input
                      licencia_vigente=True)
    client2 = Cliente(nombre="María", apellido="López", dni="87654321", edad=24, origen="local", # colocar en un input
                      licencia_vigente=True)  # Edad insuficiente (debe rechazar)
    # Cliente VIP
    vip_info = {'fecha_vencimiento': '2025-12-31', 'descuento': 10}  # 10% de descuento
    client3 = Cliente(nombre="Carlos", apellido="Gómez", dni="11223344", edad=40, origen="local",
                      licencia_vigente=True, vip=True, tarjeta_vip=vip_info)

    system.add_cliente(client1)
    system.add_cliente(client2)
    system.add_cliente(client3)

    # Simular alquileres
    print("=== Alquiler 1: Juan solicita un 'Sedan' por 3 días ===")
    factura1 = system.procesar_alquiler(cliente=client1, modelo="Sedan", periodo_dias=3,
                                         tarifa=tarifa_diaria, seguro=seguro_basico)

    print("\n=== Alquiler 2: María solicita un 'SUV' por 2 días (edad insuficiente) ===")
    factura2 = system.procesar_alquiler(cliente=client2, modelo="SUV", periodo_dias=2,
                                         tarifa=tarifa_diaria, seguro=seguro_basico)

    print("\n=== Alquiler 3: Carlos (VIP) solicita un 'Sedan' por 5 días ===")
    factura3 = system.procesar_alquiler(cliente=client3, modelo="Sedan", periodo_dias=5,
                                         tarifa=tarifa_diaria, seguro=seguro_basico)

    # Registrar devolución del vehículo de la factura 1 (si se generó)
    if factura1:
        system.registrar_devolucion(factura1.numero)

    # Registrar pagos
    if factura1:
        print("\n=== Pagos para la Factura 1 ===")
        # Primer pago parcial
        system.registrar_pago(dni=client1.dni, factura_numero=factura1.numero, importe=150)
        # Segundo pago; se intenta pagar un monto que exceda el saldo pendiente
        system.registrar_pago(dni=client1.dni, factura_numero=factura1.numero, importe=200)

    if factura3:
        print("\n=== Pago completo para la Factura 3 (Cliente VIP) ===")
        # Pago total de la factura
        system.registrar_pago(dni=client3.dni, factura_numero=factura3.numero, importe=factura3.total)


if __name__ == "__main__":
    main()
