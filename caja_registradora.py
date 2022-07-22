import datetime

boleta = {}
rut_cliente = input('Ingrese el rut del cliente para asocialo a sus puntos: ')
correo_cliente = input ('ingrese le correo del cliente para su boleta virtual: ' )
fecha_actual = datetime.date.today()
boleta['rut cliente'] = rut_cliente
boleta['correo_cliente'] = correo_cliente
boleta['fecha_actual'] = fecha_actual
boleta['detalle']=[]


print('=====Inicia el ingreso de productos=====: ')

estado = True
while estado:
    codigo_producto = input('ingrese el código de producto: ')
    nombre_producto = input('ingrese el nombre de producto: ')
    categoria = input ('ingrese la categoría del producto: ')
    precio = input('ingrese el precio del producto: ')
    cantidad = input(' ingrese la cantidad de productos: ')
    detalle = {
        'codigo_producto': codigo_producto,
        'nombre_producto': nombre_producto,
        'categoria': categoria,
        'precio': precio,
        'cantidad': cantidad
    }
    boleta.get('detalle').append(detalle)
    respuesta = input('desea continuar? si/no ')
    if respuesta == 'no':
        estado=False

print(f'Cliente: {boleta.get("rut_cliente")}')
print(f'Correo: {boleta.get("correo_cliente")}')
print(f'Fecha: {boleta.get("fecha_actual")}')

for producto in boleta.get('detalle'):
    print(f'{producto["codigo_producto"]} {producto["nombre_producto"]} {producto["cantidad"]} {producto["precio"]} {int(producto["cantidad"]) * int(producto["precio"])} ')



