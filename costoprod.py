nombre = input()
codigo = int(input())
costo_prod = int(input())

def precio(costo):
    utilidad = (costo * 120) / 100
    impuestos = (costo * 15 ) / 100
    precio_tot = costo + utilidad + impuestos
    print(f'el precio del producto es: {precio_tot}')

precio(costo_prod)
