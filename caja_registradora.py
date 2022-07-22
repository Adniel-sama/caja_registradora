import datetime
import logging

logging.basicConfig(filename='cajaRegistradora.log', encoding='utf-8', level=logging.DEBUG)
logging.info('Este es nuestro primer log y se guardará en un archivo llamado cajaRegistradora.log')

boleta = {}
rut_cliente = input('Ingrese el rut del cliente para asocialo a sus puntos: ')
correo_cliente = input ('ingrese le correo del cliente para su boleta virtual: ' )
fecha_actual = datetime.date.today()
boleta['rut_cliente'] = rut_cliente
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
total=0

for producto in boleta.get('detalle'):
    print(f'{producto["codigo_producto"]} {producto["nombre_producto"]} {producto["cantidad"]} {producto["precio"]} {int(producto["cantidad"]) * int(producto["precio"])} ')
    total+=int(producto["cantidad"])*int(producto["precio"])
print(f'total a pagar : {total}')

with open('boleta.txt', 'w') as archivo:
    archivo.write(f'Cliente: {boleta.get("rut_cliente")}\n')
    archivo.write(f'Correo: {boleta.get("correo_cliente")}\n')
    archivo.write(f'Fecha: {boleta.get("fecha_actual")}\n')
    for producto in boleta.get('detalle'):
        archivo.write(f'{producto["codigo_producto"]} {producto["nombre_producto"]} {producto["cantidad"]} {producto["precio"]} {int(producto["cantidad"]) * int(producto["precio"])} \n')
    archivo.write(f'total a pagar: {total}')

