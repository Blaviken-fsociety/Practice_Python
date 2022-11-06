# Partido Junior vs Unión Magdalena

"""
PRECIOS:
1 = Sur alta                $40.000
2 = Sur baja                $40.000
3 = Norte alta              $40.000
4 = Norte baja              $40.000
5 = Oriental alta           $80.000
6 = Oriental baja           $90.000
7 = Occidental alta         $120.000
8 = Occidental baja         $140.00

DESCUENTOS:
1. 40% si compra en línea y es barranquillero
2. 25% si compra en línea y es samario
3. 10% si compra en ventanilla y es cualquier lugar
4. 0% si compra en línea y no es ni barranquillero 
   ni samario.

INDICACIONES:
1. Solo hay 10 usuarios
2. Solo 3 usuarios tienen descuentos
3. Mostrar ubicación de los 10 usuarios
4. Mostrar valor venta recaudado
5. Mostrar descuento total
"""

precios_tribunas = """1 = Sur alta                $40.000
2 = Sur baja                $40.000
3 = Norte alta              $40.000
4 = Norte baja              $40.000
5 = Oriental alta           $80.000
6 = Oriental baja           $90.000
7 = Occidental alta         $120.000
8 = Occidental baja         $140.000"""

# Usuario 1
compra_p1 = 1
lugar_p1 = 1
tribuna_p1 = 7
if compra_p1 == 1: # En línea
    compra_p1 = "En línea"
    if lugar_p1 == 1: # Barranquilla
        lugar_p1 = "Barranquilla"
        valor_descuento_p1 = 0.40 # 40%
        if tribuna_p1 == 1:
            tribuna_p1 = "Sur alta"
            subtotal = 40000
        elif tribuna_p1 == 2:
            tribuna_p1 = "Sur baja"
            subtotal = 40000
        elif tribuna_p1 == 3:
            tribuna_p1 = "Norte alta"
            subtotal = 40000
        elif tribuna_p1 == 4:
            tribuna_p1 = "Norte baja"
            subtotal = 40000
        elif tribuna_p1 == 5:
            tribuna_p1 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p1 == 6:
            tribuna_p1 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p1 == 7:
            tribuna_p1 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p1 == 8:
            tribuna_p1 = "Occidental baja"
            subtotal = 140000
        descuento_p1 = subtotal * valor_descuento_p1
        total_p1 = subtotal - descuento_p1
    elif lugar_p1 == 2: # Santa Marta
        lugar_p1 = "Santa Marta"
        valor_descuento_p1 = 0.25 # 25%
        if tribuna_p1 == 1:
            tribuna_p1 = "Sur alta"
            subtotal = 40000
        elif tribuna_p1 == 2:
            tribuna_p1 = "Sur baja"
            subtotal = 40000
        elif tribuna_p1 == 3:
            tribuna_p1 = "Norte alta"
            subtotal = 40000
        elif tribuna_p1 == 4:
            tribuna_p1 = "Norte baja"
            subtotal = 40000
        elif tribuna_p1 == 5:
            tribuna_p1 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p1 == 6:
            tribuna_p1 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p1 == 7:
            tribuna_p1 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p1 == 8:
            tribuna_p1 = "Occidental baja"
            subtotal = 140000
        descuento_p1 = subtotal * valor_descuento_p1
        total_p1 = subtotal - descuento_p1
    else: # Otro
        lugar_p1 = "Otro"
        # 0% de descuento
        if tribuna_p1 == 1:
            tribuna_p1 = "Sur alta"
            subtotal = 40000
        elif tribuna_p1 == 2:
            tribuna_p1 = "Sur baja"
            subtotal = 40000
        elif tribuna_p1 == 3:
            tribuna_p1 = "Norte alta"
            subtotal = 40000
        elif tribuna_p1 == 4:
            tribuna_p1 = "Norte baja"
            subtotal = 40000
        elif tribuna_p1 == 5:
            tribuna_p1 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p1 == 6:
            tribuna_p1 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p1 == 7:
            tribuna_p1 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p1 == 8:
            tribuna_p1 = "Occidental baja"
            subtotal = 140000
        total_p1 = subtotal
else: # Ventanilla
    compra_p1 = "Ventanilla"
    valor_descuento_p1 = 0.10 # 10%
    if lugar_p1 == 1: # Barranquilla
        lugar_p1 = "Barranquilla"
        if tribuna_p1 == 1:
            tribuna_p1 = "Sur alta"
            subtotal = 40000
        elif tribuna_p1 == 2:
            tribuna_p1 = "Sur baja"
            subtotal = 40000
        elif tribuna_p1 == 3:
            tribuna_p1 = "Norte alta"
            subtotal = 40000
        elif tribuna_p1 == 4:
            tribuna_p1 = "Norte baja"
            subtotal = 40000
        elif tribuna_p1 == 5:
            tribuna_p1 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p1 == 6:
            tribuna_p1 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p1 == 7:
            tribuna_p1 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p1 == 8:
            tribuna_p1 = "Occidental baja"
            subtotal = 140000
        descuento_p1 = subtotal * valor_descuento_p1
        total_p1 = subtotal - descuento_p1  
    elif lugar_p1 == 2: # Santa Marta
        lugar_p1 = "Santa Marta"
        if tribuna_p1 == 1:
            tribuna_p1 = "Sur alta"
            subtotal = 40000
        elif tribuna_p1 == 2:
            tribuna_p1 = "Sur baja"
            subtotal = 40000
        elif tribuna_p1 == 3:
            tribuna_p1 = "Norte alta"
            subtotal = 40000
        elif tribuna_p1 == 4:
            tribuna_p1 = "Norte baja"
            subtotal = 40000
        elif tribuna_p1 == 5:
            tribuna_p1 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p1 == 6:
            tribuna_p1 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p1 == 7:
            tribuna_p1 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p1 == 8:
            tribuna_p1 = "Occidental baja"
            subtotal = 140000
        descuento_p1 = subtotal * valor_descuento_p1
        total_p1 = subtotal - descuento_p1
    else: # Otro
        lugar_p1 = "Otro"
        if tribuna_p1 == 1:
            tribuna_p1 = "Sur alta"
            subtotal = 40000
        elif tribuna_p1 == 2:
            tribuna_p1 = "Sur baja"
            subtotal = 40000
        elif tribuna_p1 == 3:
            tribuna_p1 = "Norte alta"
            subtotal = 40000
        elif tribuna_p1 == 4:
            tribuna_p1 = "Norte baja"
            subtotal = 40000
        elif tribuna_p1 == 5:
            tribuna_p1 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p1 == 6:
            tribuna_p1 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p1 == 7:
            tribuna_p1 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p1 == 8:
            tribuna_p1 = "Occidental baja"
            subtotal = 140000
        descuento_p1 = subtotal * valor_descuento_p1
        total_p1 = subtotal - descuento_p1

# Usuario 2
compra_p2 = 1
lugar_p2 = 2
tribuna_p2 = 5
if compra_p2 == 1: # En línea
    compra_p2 = "En línea"
    if lugar_p2 == 1: # Barranquilla
        lugar_p2 = "Barranquilla"
        valor_descuento_p2 = 0.40 # 40%
        if tribuna_p2 == 1:
            tribuna_p2 = "Sur alta"
            subtotal = 40000
        elif tribuna_p2 == 2:
            tribuna_p2 = "Sur baja"
            subtotal = 40000
        elif tribuna_p2 == 3:
            tribuna_p2 = "Norte alta"
            subtotal = 40000
        elif tribuna_p2 == 4:
            tribuna_p2 = "Norte baja"
            subtotal = 40000
        elif tribuna_p2 == 5:
            tribuna_p2 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p2 == 6:
            tribuna_p2 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p2 == 7:
            tribuna_p2 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p2 == 8:
            tribuna_p2 = "Occidental baja"
            subtotal = 140000
        descuento_p2 = subtotal * valor_descuento_p2
        total_p2 = subtotal - descuento_p2
    elif lugar_p2 == 2: # Santa Marta
        lugar_p2 = "Santa Marta"
        valor_descuento_p2 = 0.25 # 25%
        if tribuna_p2 == 1:
            tribuna_p2 = "Sur alta"
            subtotal = 40000
        elif tribuna_p2 == 2:
            tribuna_p2 = "Sur baja"
            subtotal = 40000
        elif tribuna_p2 == 3:
            tribuna_p2 = "Norte alta"
            subtotal = 40000
        elif tribuna_p2 == 4:
            tribuna_p2 = "Norte baja"
            subtotal = 40000
        elif tribuna_p2 == 5:
            tribuna_p2 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p2 == 6:
            tribuna_p2 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p2 == 7:
            tribuna_p2 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p2 == 8:
            tribuna_p2 = "Occidental baja"
            subtotal = 140000
        descuento_p2 = subtotal * valor_descuento_p2
        total_p2 = subtotal - descuento_p2
    else: # Otro
        lugar_p2 = "Otro"
        # 0% de descuento
        if tribuna_p2 == 1:
            tribuna_p2 = "Sur alta"
            subtotal = 40000
        elif tribuna_p2 == 2:
            tribuna_p2 = "Sur baja"
            subtotal = 40000
        elif tribuna_p2 == 3:
            tribuna_p2 = "Norte alta"
            subtotal = 40000
        elif tribuna_p2 == 4:
            tribuna_p2 = "Norte baja"
            subtotal = 40000
        elif tribuna_p2 == 5:
            tribuna_p2 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p2 == 6:
            tribuna_p2 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p2 == 7:
            tribuna_p2 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p2 == 8:
            tribuna_p2 = "Occidental baja"
            subtotal = 140000
        total_p2 = subtotal
else: # Ventanilla
    compra_p2 = "Ventanilla"
    valor_descuento_p2 = 0.10 # 10%
    if lugar_p2 == 1: # Barranquilla
        lugar_p2 = "Barranquilla"
        if tribuna_p2 == 1:
            tribuna_p2 = "Sur alta"
            subtotal = 40000
        elif tribuna_p2 == 2:
            tribuna_p2 = "Sur baja"
            subtotal = 40000
        elif tribuna_p2 == 3:
            tribuna_p2 = "Norte alta"
            subtotal = 40000
        elif tribuna_p2 == 4:
            tribuna_p2 = "Norte baja"
            subtotal = 40000
        elif tribuna_p2 == 5:
            tribuna_p2 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p2 == 6:
            tribuna_p2 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p2 == 7:
            tribuna_p2 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p2 == 8:
            tribuna_p2 = "Occidental baja"
            subtotal = 140000
        descuento_p2 = subtotal * valor_descuento_p2
        total_p2 = subtotal - descuento_p2  
    elif lugar_p2 == 2: # Santa Marta
        lugar_p2 = "Santa Marta"
        if tribuna_p2 == 1:
            tribuna_p2 = "Sur alta"
            subtotal = 40000
        elif tribuna_p2 == 2:
            tribuna_p2 = "Sur baja"
            subtotal = 40000
        elif tribuna_p2 == 3:
            tribuna_p2 = "Norte alta"
            subtotal = 40000
        elif tribuna_p2 == 4:
            tribuna_p2 = "Norte baja"
            subtotal = 40000
        elif tribuna_p2 == 5:
            tribuna_p2 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p2 == 6:
            tribuna_p2 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p2 == 7:
            tribuna_p2 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p2 == 8:
            tribuna_p2 = "Occidental baja"
            subtotal = 140000
        descuento_p2 = subtotal * valor_descuento_p2
        total_p2 = subtotal - descuento_p2
    else: # Otro
        lugar_p2 = "Otro"
        if tribuna_p2 == 1:
            tribuna_p2 = "Sur alta"
            subtotal = 40000
        elif tribuna_p2 == 2:
            tribuna_p2 = "Sur baja"
            subtotal = 40000
        elif tribuna_p2 == 3:
            tribuna_p2 = "Norte alta"
            subtotal = 40000
        elif tribuna_p2 == 4:
            tribuna_p2 = "Norte baja"
            subtotal = 40000
        elif tribuna_p2 == 5:
            tribuna_p2 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p2 == 6:
            tribuna_p2 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p2 == 7:
            tribuna_p2 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p2 == 8:
            tribuna_p2 = "Occidental baja"
            subtotal = 140000
        descuento_p2 = subtotal * valor_descuento_p2
        total_p2 = subtotal - descuento_p2

# Usuario 3
compra_p3 = 2
lugar_p3 = 1
tribuna_p3 = 3
if compra_p3 == 1: # En línea
    compra_p3 = "En línea"
    if lugar_p3 == 1: # Barranquilla
        lugar_p3 = "Barranquilla"
        valor_descuento_p3 = 0.40 # 40%
        if tribuna_p3 == 1:
            tribuna_p3 = "Sur alta"
            subtotal = 40000
        elif tribuna_p3 == 2:
            tribuna_p3 = "Sur baja"
            subtotal = 40000
        elif tribuna_p3 == 3:
            tribuna_p3 = "Norte alta"
            subtotal = 40000
        elif tribuna_p3 == 4:
            tribuna_p3 = "Norte baja"
            subtotal = 40000
        elif tribuna_p3 == 5:
            tribuna_p3 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p3 == 6:
            tribuna_p3 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p3 == 7:
            tribuna_p3 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p3 == 8:
            tribuna_p3 = "Occidental baja"
            subtotal = 140000
        descuento_p3 = subtotal * valor_descuento_p3
        total_p3 = subtotal - descuento_p3
    elif lugar_p3 == 2: # Santa Marta
        lugar_p3 = "Santa Marta"
        valor_descuento_p3 = 0.25 # 25%
        if tribuna_p3 == 1:
            tribuna_p3 = "Sur alta"
            subtotal = 40000
        elif tribuna_p3 == 2:
            tribuna_p3 = "Sur baja"
            subtotal = 40000
        elif tribuna_p3 == 3:
            tribuna_p3 = "Norte alta"
            subtotal = 40000
        elif tribuna_p3 == 4:
            tribuna_p3 = "Norte baja"
            subtotal = 40000
        elif tribuna_p3 == 5:
            tribuna_p3 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p3 == 6:
            tribuna_p3 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p3 == 7:
            tribuna_p3 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p3 == 8:
            tribuna_p3 = "Occidental baja"
            subtotal = 140000
        descuento_p3 = subtotal * valor_descuento_p3
        total_p3 = subtotal - descuento_p3
    else: # Otro
        lugar_p3 = "Otro"
        # 0% de descuento
        if tribuna_p3 == 1:
            tribuna_p3 = "Sur alta"
            subtotal = 40000
        elif tribuna_p3 == 2:
            tribuna_p3 = "Sur baja"
            subtotal = 40000
        elif tribuna_p3 == 3:
            tribuna_p3 = "Norte alta"
            subtotal = 40000
        elif tribuna_p3 == 4:
            tribuna_p3 = "Norte baja"
            subtotal = 40000
        elif tribuna_p3 == 5:
            tribuna_p3 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p3 == 6:
            tribuna_p3 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p3 == 7:
            tribuna_p3 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p3 == 8:
            tribuna_p3 = "Occidental baja"
            subtotal = 140000
        total_p3 = subtotal
else: # Ventanilla
    compra_p3 = "Ventanilla"
    valor_descuento_p3 = 0.10 # 10%
    if lugar_p3 == 1: # Barranquilla
        lugar_p3 = "Barranquilla"
        if tribuna_p3 == 1:
            tribuna_p3 = "Sur alta"
            subtotal = 40000
        elif tribuna_p3 == 2:
            tribuna_p3 = "Sur baja"
            subtotal = 40000
        elif tribuna_p3 == 3:
            tribuna_p3 = "Norte alta"
            subtotal = 40000
        elif tribuna_p3 == 4:
            tribuna_p3 = "Norte baja"
            subtotal = 40000
        elif tribuna_p3 == 5:
            tribuna_p3 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p3 == 6:
            tribuna_p3 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p3 == 7:
            tribuna_p3 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p3 == 8:
            tribuna_p3 = "Occidental baja"
            subtotal = 140000
        descuento_p3 = subtotal * valor_descuento_p3
        total_p3 = subtotal - descuento_p3  
    elif lugar_p3 == 2: # Santa Marta
        lugar_p3 = "Santa Marta"
        if tribuna_p3 == 1:
            tribuna_p3 = "Sur alta"
            subtotal = 40000
        elif tribuna_p3 == 2:
            tribuna_p3 = "Sur baja"
            subtotal = 40000
        elif tribuna_p3 == 3:
            tribuna_p3 = "Norte alta"
            subtotal = 40000
        elif tribuna_p3 == 4:
            tribuna_p3 = "Norte baja"
            subtotal = 40000
        elif tribuna_p3 == 5:
            tribuna_p3 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p3 == 6:
            tribuna_p3 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p3 == 7:
            tribuna_p3 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p3 == 8:
            tribuna_p3 = "Occidental baja"
            subtotal = 140000
        descuento_p3 = subtotal * valor_descuento_p3
        total_p3 = subtotal - descuento_p3
    else: # Otro
        lugar_p3 = "Otro"
        if tribuna_p3 == 1:
            tribuna_p3 = "Sur alta"
            subtotal = 40000
        elif tribuna_p3 == 2:
            tribuna_p3 = "Sur baja"
            subtotal = 40000
        elif tribuna_p3 == 3:
            tribuna_p3 = "Norte alta"
            subtotal = 40000
        elif tribuna_p3 == 4:
            tribuna_p3 = "Norte baja"
            subtotal = 40000
        elif tribuna_p3 == 5:
            tribuna_p3 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p3 == 6:
            tribuna_p3 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p3 == 7:
            tribuna_p3 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p3 == 8:
            tribuna_p3 = "Occidental baja"
            subtotal = 140000
        descuento_p3 = subtotal * valor_descuento_p3
        total_p3 = subtotal - descuento_p3

# Usuario 4
compra_p4 = 1
lugar_p4 = 3
tribuna_p4 = 1
if compra_p4 == 1: # En línea
    compra_p4 = "En línea"
    if lugar_p4 == 1: # Barranquilla
        lugar_p4 = "Barranquilla"
        valor_descuento_p4 = 0.40 # 40%
        if tribuna_p4 == 1:
            tribuna_p4 = "Sur alta"
            subtotal = 40000
        elif tribuna_p4 == 2:
            tribuna_p4 = "Sur baja"
            subtotal = 40000
        elif tribuna_p4 == 3:
            tribuna_p4 = "Norte alta"
            subtotal = 40000
        elif tribuna_p4 == 4:
            tribuna_p4 = "Norte baja"
            subtotal = 40000
        elif tribuna_p4 == 5:
            tribuna_p4 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p4 == 6:
            tribuna_p4 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p4 == 7:
            tribuna_p4 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p4 == 8:
            tribuna_p4 = "Occidental baja"
            subtotal = 140000
        descuento_p4 = subtotal * valor_descuento_p4
        total = subtotal - descuento_p4
    elif lugar_p4 == 2: # Santa Marta
        lugar_p4 = "Santa Marta"
        valor_descuento_p4 = 0.25 # 25%
        if tribuna_p4 == 1:
            tribuna_p4 = "Sur alta"
            subtotal = 40000
        elif tribuna_p4 == 2:
            tribuna_p4 = "Sur baja"
            subtotal = 40000
        elif tribuna_p4 == 3:
            tribuna_p4 = "Norte alta"
            subtotal = 40000
        elif tribuna_p4 == 4:
            tribuna_p4 = "Norte baja"
            subtotal = 40000
        elif tribuna_p4 == 5:
            tribuna_p4 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p4 == 6:
            tribuna_p4 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p4 == 7:
            tribuna_p4 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p4 == 8:
            tribuna_p4 = "Occidental baja"
            subtotal = 140000
        descuento_p4 = subtotal * valor_descuento_p4
        total_p4 = subtotal - descuento_p4
    else: # Otro
        lugar_p4 = "Otro"
        # 0% de descuento
        if tribuna_p4 == 1:
            tribuna_p4 = "Sur alta"
            subtotal = 40000
        elif tribuna_p4 == 2:
            tribuna_p4 = "Sur baja"
            subtotal = 40000
        elif tribuna_p4 == 3:
            tribuna_p4 = "Norte alta"
            subtotal = 40000
        elif tribuna_p4 == 4:
            tribuna_p4 = "Norte baja"
            subtotal = 40000
        elif tribuna_p4 == 5:
            tribuna_p4 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p4 == 6:
            tribuna_p4 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p4 == 7:
            tribuna_p4 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p4 == 8:
            tribuna_p4 = "Occidental baja"
            subtotal = 140000
        total_p4 = subtotal
else: # Ventanilla
    compra_p4 = "Ventanilla"
    valor_descuento_p4 = 0.10 # 10%
    if lugar_p4 == 1: # Barranquilla
        lugar_p4 = "Barranquilla"
        if tribuna_p4 == 1:
            tribuna_p4 = "Sur alta"
            subtotal = 40000
        elif tribuna_p4 == 2:
            tribuna_p4 = "Sur baja"
            subtotal = 40000
        elif tribuna_p4 == 3:
            tribuna_p4 = "Norte alta"
            subtotal = 40000
        elif tribuna_p4 == 4:
            tribuna_p4 = "Norte baja"
            subtotal = 40000
        elif tribuna_p4 == 5:
            tribuna_p4 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p4 == 6:
            tribuna_p4 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p4 == 7:
            tribuna_p4 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p4 == 8:
            tribuna_p4 = "Occidental baja"
            subtotal = 140000
        descuento_p4 = subtotal * valor_descuento_p4
        total_p4 = subtotal - descuento_p4  
    elif lugar_p4 == 2: # Santa Marta
        lugar_p4 = "Santa Marta"
        if tribuna_p4 == 1:
            tribuna_p4 = "Sur alta"
            subtotal = 40000
        elif tribuna_p4 == 2:
            tribuna_p4 = "Sur baja"
            subtotal = 40000
        elif tribuna_p4 == 3:
            tribuna_p4 = "Norte alta"
            subtotal = 40000
        elif tribuna_p4 == 4:
            tribuna_p4 = "Norte baja"
            subtotal = 40000
        elif tribuna_p4 == 5:
            tribuna_p4 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p4 == 6:
            tribuna_p4 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p4 == 7:
            tribuna_p4 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p4 == 8:
            tribuna_p4 = "Occidental baja"
            subtotal = 140000
        descuento_p4 = subtotal * valor_descuento_p4
        total_p4 = subtotal - descuento_p4
    else: # Otro
        lugar_p4 = "Otro"
        if tribuna_p4 == 1:
            tribuna_p4 = "Sur alta"
            subtotal = 40000
        elif tribuna_p4 == 2:
            tribuna_p4 = "Sur baja"
            subtotal = 40000
        elif tribuna_p4 == 3:
            tribuna_p4 = "Norte alta"
            subtotal = 40000
        elif tribuna_p4 == 4:
            tribuna_p4 = "Norte baja"
            subtotal = 40000
        elif tribuna_p4 == 5:
            tribuna_p4 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p4 == 6:
            tribuna_p4 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p4 == 7:
            tribuna_p4 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p4 == 8:
            tribuna_p4 = "Occidental baja"
            subtotal = 140000
        descuento_p4 = subtotal * valor_descuento_p4
        total_p4 = subtotal - descuento_p4

# Usuario 5
compra_p5 = 1
lugar_p5 = 3
tribuna_p5 = 2
if compra_p5 == 1: # En línea
    compra_p5 = "En línea"
    if lugar_p5 == 1: # Barranquilla
        lugar_p5 = "Barranquilla"
        valor_descuento_p5 = 0.40 # 40%
        if tribuna_p5 == 1:
            tribuna_p5 = "Sur alta"
            subtotal = 40000
        elif tribuna_p5 == 2:
            tribuna_p5 = "Sur baja"
            subtotal = 40000
        elif tribuna_p5 == 3:
            tribuna_p5 = "Norte alta"
            subtotal = 40000
        elif tribuna_p5 == 4:
            tribuna_p5 = "Norte baja"
            subtotal = 40000
        elif tribuna_p5 == 5:
            tribuna_p5 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p5 == 6:
            tribuna_p5 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p5 == 7:
            tribuna_p5 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p5 == 8:
            tribuna_p5 = "Occidental baja"
            subtotal = 140000
        descuento_p5 = subtotal * valor_descuento_p5
        total_p5 = subtotal - descuento_p5
    elif lugar_p5 == 2: # Santa Marta
        lugar_p5 = "Santa Marta"
        valor_descuento_p5 = 0.25 # 25%
        if tribuna_p5 == 1:
            tribuna_p5 = "Sur alta"
            subtotal = 40000
        elif tribuna_p5 == 2:
            tribuna_p5 = "Sur baja"
            subtotal = 40000
        elif tribuna_p5 == 3:
            tribuna_p5 = "Norte alta"
            subtotal = 40000
        elif tribuna_p5 == 4:
            tribuna_p5 = "Norte baja"
            subtotal = 40000
        elif tribuna_p5 == 5:
            tribuna_p5 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p5 == 6:
            tribuna_p5 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p5 == 7:
            tribuna_p5 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p5 == 8:
            tribuna_p5 = "Occidental baja"
            subtotal = 140000
        descuento_p5 = subtotal * valor_descuento_p5
        total_p5 = subtotal - descuento_p5
    else: # Otro
        lugar_p5 = "Otro"
        # 0% de descuento
        if tribuna_p5 == 1:
            tribuna_p5 = "Sur alta"
            subtotal = 40000
        elif tribuna_p5 == 2:
            tribuna_p5 = "Sur baja"
            subtotal = 40000
        elif tribuna_p5 == 3:
            tribuna_p5 = "Norte alta"
            subtotal = 40000
        elif tribuna_p5 == 4:
            tribuna_p5 = "Norte baja"
            subtotal = 40000
        elif tribuna_p5 == 5:
            tribuna_p5 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p5 == 6:
            tribuna_p5 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p5 == 7:
            tribuna_p5 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p5 == 8:
            tribuna_p5 = "Occidental baja"
            subtotal = 140000
        total_p5 = subtotal
else: # Ventanilla
    compra_p5 = "Ventanilla"
    valor_descuento_p5 = 0.10 # 10%
    if lugar_p5 == 1: # Barranquilla
        lugar_p5 = "Barranquilla"
        if tribuna_p5 == 1:
            tribuna_p5 = "Sur alta"
            subtotal = 40000
        elif tribuna_p5 == 2:
            tribuna_p5 = "Sur baja"
            subtotal = 40000
        elif tribuna_p5 == 3:
            tribuna_p5 = "Norte alta"
            subtotal = 40000
        elif tribuna_p5 == 4:
            tribuna_p5 = "Norte baja"
            subtotal = 40000
        elif tribuna_p5 == 5:
            tribuna_p5 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p5 == 6:
            tribuna_p5 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p5 == 7:
            tribuna_p5 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p5 == 8:
            tribuna_p5 = "Occidental baja"
            subtotal = 140000
        descuento_p5 = subtotal * valor_descuento_p5
        total_p5 = subtotal - descuento_p5  
    elif lugar_p5 == 2: # Santa Marta
        lugar_p5 = "Santa Marta"
        if tribuna_p5 == 1:
            tribuna_p5 = "Sur alta"
            subtotal = 40000
        elif tribuna_p5 == 2:
            tribuna_p5 = "Sur baja"
            subtotal = 40000
        elif tribuna_p5 == 3:
            tribuna_p5 = "Norte alta"
            subtotal = 40000
        elif tribuna_p5 == 4:
            tribuna_p5 = "Norte baja"
            subtotal = 40000
        elif tribuna_p5 == 5:
            tribuna_p5 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p5 == 6:
            tribuna_p5 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p5 == 7:
            tribuna_p5 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p5 == 8:
            tribuna_p5 = "Occidental baja"
            subtotal = 140000
        descuento_p5 = subtotal * valor_descuento_p5
        total_p5 = subtotal - descuento_p5
    else: # Otro
        lugar_p5 = "Otro"
        if tribuna_p5 == 1:
            tribuna_p5 = "Sur alta"
            subtotal = 40000
        elif tribuna_p5 == 2:
            tribuna_p5 = "Sur baja"
            subtotal = 40000
        elif tribuna_p5 == 3:
            tribuna_p5 = "Norte alta"
            subtotal = 40000
        elif tribuna_p5 == 4:
            tribuna_p5 = "Norte baja"
            subtotal = 40000
        elif tribuna_p5 == 5:
            tribuna_p5 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p5 == 6:
            tribuna_p5 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p5 == 7:
            tribuna_p5 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p5 == 8:
            tribuna_p5 = "Occidental baja"
            subtotal = 140000
        descuento_p5 = subtotal * valor_descuento_p5
        total_p5 = subtotal - descuento_p5

# Usuario 6
compra_p6 = 1
lugar_p6 = 3
tribuna_p6 = 3
if compra_p6 == 1: # En línea
    compra_p6 = "En línea"
    if lugar_p6 == 1: # Barranquilla
        lugar_p6 = "Barranquilla"
        valor_descuento_p6 = 0.40 # 40%
        if tribuna_p6 == 1:
            tribuna_p6 = "Sur alta"
            subtotal = 40000
        elif tribuna_p6 == 2:
            tribuna_p6 = "Sur baja"
            subtotal = 40000
        elif tribuna_p6 == 3:
            tribuna_p6 = "Norte alta"
            subtotal = 40000
        elif tribuna_p6 == 4:
            tribuna_p6 = "Norte baja"
            subtotal = 40000
        elif tribuna_p6 == 5:
            tribuna_p6 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p6 == 6:
            tribuna_p6 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p6 == 7:
            tribuna_p6 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p6 == 8:
            tribuna_p6 = "Occidental baja"
            subtotal = 140000
        descuento_p6 = subtotal * valor_descuento_p6
        total_p6 = subtotal - descuento_p6
    elif lugar_p6 == 2: # Santa Marta
        lugar_p6 = "Santa Marta"
        valor_descuento_p6 = 0.25 # 25%
        if tribuna_p6 == 1:
            tribuna_p6 = "Sur alta"
            subtotal = 40000
        elif tribuna_p6 == 2:
            tribuna_p6 = "Sur baja"
            subtotal = 40000
        elif tribuna_p6 == 3:
            tribuna_p6 = "Norte alta"
            subtotal = 40000
        elif tribuna_p6 == 4:
            tribuna_p6 = "Norte baja"
            subtotal = 40000
        elif tribuna_p6 == 5:
            tribuna_p6 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p6 == 6:
            tribuna_p6 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p6 == 7:
            tribuna_p6 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p6 == 8:
            tribuna_p6 = "Occidental baja"
            subtotal = 140000
        descuento_p6 = subtotal * valor_descuento_p6
        total_p6 = subtotal - descuento_p6
    else: # Otro
        lugar_p6 = "Otro"
        # 0% de descuento
        if tribuna_p6 == 1:
            tribuna_p6 = "Sur alta"
            subtotal = 40000
        elif tribuna_p6 == 2:
            tribuna_p6 = "Sur baja"
            subtotal = 40000
        elif tribuna_p6 == 3:
            tribuna_p6 = "Norte alta"
            subtotal = 40000
        elif tribuna_p6 == 4:
            tribuna_p6 = "Norte baja"
            subtotal = 40000
        elif tribuna_p6 == 5:
            tribuna_p6 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p6 == 6:
            tribuna_p6 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p6 == 7:
            tribuna_p6 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p6 == 8:
            tribuna_p6 = "Occidental baja"
            subtotal = 140000
        total_p6 = subtotal
else: # Ventanilla
    compra_p6 = "Ventanilla"
    valor_descuento_p6 = 0.10 # 10%
    if lugar_p6 == 1: # Barranquilla
        lugar_p6 = "Barranquilla"
        if tribuna_p6 == 1:
            tribuna_p6 = "Sur alta"
            subtotal = 40000
        elif tribuna_p6 == 2:
            tribuna_p6 = "Sur baja"
            subtotal = 40000
        elif tribuna_p6 == 3:
            tribuna_p6 = "Norte alta"
            subtotal = 40000
        elif tribuna_p6 == 4:
            tribuna_p6 = "Norte baja"
            subtotal = 40000
        elif tribuna_p6 == 5:
            tribuna_p6 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p6 == 6:
            tribuna_p6 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p6 == 7:
            tribuna_p6 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p6 == 8:
            tribuna_p6 = "Occidental baja"
            subtotal = 140000
        descuento_p6 = subtotal * valor_descuento_p6
        total_p6 = subtotal - descuento_p6  
    elif lugar_p6 == 2: # Santa Marta
        lugar_p6 = "Santa Marta"
        if tribuna_p6 == 1:
            tribuna_p6 = "Sur alta"
            subtotal = 40000
        elif tribuna_p6 == 2:
            tribuna_p6 = "Sur baja"
            subtotal = 40000
        elif tribuna_p6 == 3:
            tribuna_p6 = "Norte alta"
            subtotal = 40000
        elif tribuna_p6 == 4:
            tribuna_p6 = "Norte baja"
            subtotal = 40000
        elif tribuna_p6 == 5:
            tribuna_p6 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p6 == 6:
            tribuna_p6 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p6 == 7:
            tribuna_p6 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p6 == 8:
            tribuna_p6 = "Occidental baja"
            subtotal = 140000
        descuento_p6 = subtotal * valor_descuento_p6
        total_p6 = subtotal - descuento_p6
    else: # Otro
        lugar_p6 = "Otro"
        if tribuna_p6 == 1:
            tribuna_p6 = "Sur alta"
            subtotal = 40000
        elif tribuna_p6 == 2:
            tribuna_p6 = "Sur baja"
            subtotal = 40000
        elif tribuna_p6 == 3:
            tribuna_p6 = "Norte alta"
            subtotal = 40000
        elif tribuna_p6 == 4:
            tribuna_p6 = "Norte baja"
            subtotal = 40000
        elif tribuna_p6 == 5:
            tribuna_p6 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p6 == 6:
            tribuna_p6 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p6 == 7:
            tribuna_p6 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p6 == 8:
            tribuna_p6 = "Occidental baja"
            subtotal = 140000
        descuento_p6 = subtotal * valor_descuento_p6
        total_p6 = subtotal - descuento_p6

# Usuario 7
compra_p7 = 1
lugar_p7 = 3
tribuna_p7 = 4
if compra_p7 == 1: # En línea
    compra_p7 = "En línea"
    if lugar_p7 == 1: # Barranquilla
        lugar_p7 = "Barranquilla"
        valor_descuento_p7 = 0.40 # 40%
        if tribuna_p7 == 1:
            tribuna_p7 = "Sur alta"
            subtotal = 40000
        elif tribuna_p7 == 2:
            tribuna_p7 = "Sur baja"
            subtotal = 40000
        elif tribuna_p7 == 3:
            tribuna_p7 = "Norte alta"
            subtotal = 40000
        elif tribuna_p7 == 4:
            tribuna_p7 = "Norte baja"
            subtotal = 40000
        elif tribuna_p7 == 5:
            tribuna_p7 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p7 == 6:
            tribuna_p7 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p7 == 7:
            tribuna_p7 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p7 == 8:
            tribuna_p7 = "Occidental baja"
            subtotal = 140000
        descuento_p7 = subtotal * valor_descuento_p7
        total_p7 = subtotal - descuento_p7
    elif lugar_p7 == 2: # Santa Marta
        lugar_p7 = "Santa Marta"
        valor_descuento_p7 = 0.25 # 25%
        if tribuna_p7 == 1:
            tribuna_p7 = "Sur alta"
            subtotal = 40000
        elif tribuna_p7 == 2:
            tribuna_p7 = "Sur baja"
            subtotal = 40000
        elif tribuna_p7 == 3:
            tribuna_p7 = "Norte alta"
            subtotal = 40000
        elif tribuna_p7 == 4:
            tribuna_p7 = "Norte baja"
            subtotal = 40000
        elif tribuna_p7 == 5:
            tribuna_p7 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p7 == 6:
            tribuna_p7 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p7 == 7:
            tribuna_p7 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p7 == 8:
            tribuna_p7 = "Occidental baja"
            subtotal = 140000
        descuento_p7 = subtotal * valor_descuento_p7
        total_p7 = subtotal - descuento_p7
    else: # Otro
        lugar_p7 = "Otro"
        # 0% de descuento
        if tribuna_p7 == 1:
            tribuna_p7 = "Sur alta"
            subtotal = 40000
        elif tribuna_p7 == 2:
            tribuna_p7 = "Sur baja"
            subtotal = 40000
        elif tribuna_p7 == 3:
            tribuna_p7 = "Norte alta"
            subtotal = 40000
        elif tribuna_p7 == 4:
            tribuna_p7 = "Norte baja"
            subtotal = 40000
        elif tribuna_p7 == 5:
            tribuna_p7 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p7 == 6:
            tribuna_p7 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p7 == 7:
            tribuna_p7 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p7 == 8:
            tribuna_p7 = "Occidental baja"
            subtotal = 140000
        total_p7 = subtotal
else: # Ventanilla
    compra_p7 = "Ventanilla"
    valor_descuento_p7 = 0.10 # 10%
    if lugar_p7 == 1: # Barranquilla
        lugar_p7 = "Barranquilla"
        if tribuna_p7 == 1:
            tribuna_p7 = "Sur alta"
            subtotal = 40000
        elif tribuna_p7 == 2:
            tribuna_p7 = "Sur baja"
            subtotal = 40000
        elif tribuna_p7 == 3:
            tribuna_p7 = "Norte alta"
            subtotal = 40000
        elif tribuna_p7 == 4:
            tribuna_p7 = "Norte baja"
            subtotal = 40000
        elif tribuna_p7 == 5:
            tribuna_p7 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p7 == 6:
            tribuna_p7 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p7 == 7:
            tribuna_p7 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p7 == 8:
            tribuna_p7 = "Occidental baja"
            subtotal = 140000
        descuento_p7 = subtotal * valor_descuento_p7
        total_p7 = subtotal - descuento_p7  
    elif lugar_p7 == 2: # Santa Marta
        lugar_p7 = "Santa Marta"
        if tribuna_p7 == 1:
            tribuna_p7 = "Sur alta"
            subtotal = 40000
        elif tribuna_p7 == 2:
            tribuna_p7 = "Sur baja"
            subtotal = 40000
        elif tribuna_p7 == 3:
            tribuna_p7 = "Norte alta"
            subtotal = 40000
        elif tribuna_p7 == 4:
            tribuna_p7 = "Norte baja"
            subtotal = 40000
        elif tribuna_p7 == 5:
            tribuna_p7 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p7 == 6:
            tribuna_p7 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p7 == 7:
            tribuna_p7 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p7 == 8:
            tribuna_p7 = "Occidental baja"
            subtotal = 140000
        descuento_p7 = subtotal * valor_descuento_p7
        total_p7 = subtotal - descuento_p7
    else: # Otro
        lugar_p7 = "Otro"
        if tribuna_p7 == 1:
            tribuna_p7 = "Sur alta"
            subtotal = 40000
        elif tribuna_p7 == 2:
            tribuna_p7 = "Sur baja"
            subtotal = 40000
        elif tribuna_p7 == 3:
            tribuna_p7 = "Norte alta"
            subtotal = 40000
        elif tribuna_p7 == 4:
            tribuna_p7 = "Norte baja"
            subtotal = 40000
        elif tribuna_p7 == 5:
            tribuna_p7 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p7 == 6:
            tribuna_p7 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p7 == 7:
            tribuna_p7 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p7 == 8:
            tribuna_p7 = "Occidental baja"
            subtotal = 140000
        descuento_p7 = subtotal * valor_descuento_p7
        total_p7 = subtotal - descuento_p7

# Usuario 8
compra_p8 = 1
lugar_p8 = 3
tribuna_p8 = 5
if compra_p8 == 1: # En línea
    compra_p8 = "En línea"
    if lugar_p8 == 1: # Barranquilla
        lugar_p8 = "Barranquilla"
        valor_descuento_p8 = 0.40 # 40%
        if tribuna_p8 == 1:
            tribuna_p8 = "Sur alta"
            subtotal = 40000
        elif tribuna_p8 == 2:
            tribuna_p8 = "Sur baja"
            subtotal = 40000
        elif tribuna_p8 == 3:
            tribuna_p8 = "Norte alta"
            subtotal = 40000
        elif tribuna_p8 == 4:
            tribuna_p8 = "Norte baja"
            subtotal = 40000
        elif tribuna_p8 == 5:
            tribuna_p8 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p8 == 6:
            tribuna_p8 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p8 == 7:
            tribuna_p8 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p8 == 8:
            tribuna_p8 = "Occidental baja"
            subtotal = 140000
        descuento_p8 = subtotal * valor_descuento_p8
        total_p8 = subtotal - descuento_p8
    elif lugar_p8 == 2: # Santa Marta
        lugar_p8 = "Santa Marta"
        valor_descuento_p8 = 0.25 # 25%
        if tribuna_p8 == 1:
            tribuna_p8 = "Sur alta"
            subtotal = 40000
        elif tribuna_p8 == 2:
            tribuna_p8 = "Sur baja"
            subtotal = 40000
        elif tribuna_p8 == 3:
            tribuna_p8 = "Norte alta"
            subtotal = 40000
        elif tribuna_p8 == 4:
            tribuna_p8 = "Norte baja"
            subtotal = 40000
        elif tribuna_p8 == 5:
            tribuna_p8 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p8 == 6:
            tribuna_p8 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p8 == 7:
            tribuna_p8 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p8 == 8:
            tribuna_p8 = "Occidental baja"
            subtotal = 140000
        descuento_p8 = subtotal * valor_descuento_p8
        total_p8 = subtotal - descuento_p8
    else: # Otro
        lugar_p8 = "Otro"
        # 0% de descuento
        if tribuna_p8 == 1:
            tribuna_p8 = "Sur alta"
            subtotal = 40000
        elif tribuna_p8 == 2:
            tribuna_p8 = "Sur baja"
            subtotal = 40000
        elif tribuna_p8 == 3:
            tribuna_p8 = "Norte alta"
            subtotal = 40000
        elif tribuna_p8 == 4:
            tribuna_p8 = "Norte baja"
            subtotal = 40000
        elif tribuna_p8 == 5:
            tribuna_p8 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p8 == 6:
            tribuna_p8 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p8 == 7:
            tribuna_p8 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p8 == 8:
            tribuna_p8 = "Occidental baja"
            subtotal = 140000
        total_p8 = subtotal
else: # Ventanilla
    compra_p8 = "En línea"
    valor_descuento_p8 = 0.10 # 10%
    if lugar_p8 == 1: # Barranquilla
        lugar_p8 = "Barranquilla"
        if tribuna_p8 == 1:
            tribuna_p8 = "Sur alta"
            subtotal = 40000
        elif tribuna_p8 == 2:
            tribuna_p8 = "Sur baja"
            subtotal = 40000
        elif tribuna_p8 == 3:
            tribuna_p8 = "Norte alta"
            subtotal = 40000
        elif tribuna_p8 == 4:
            tribuna_p8 = "Norte baja"
            subtotal = 40000
        elif tribuna_p8 == 5:
            tribuna_p8 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p8 == 6:
            tribuna_p8 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p8 == 7:
            tribuna_p8 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p8 == 8:
            tribuna_p8 = "Occidental baja"
            subtotal = 140000
        descuento_p8 = subtotal * valor_descuento_p8
        total_p8 = subtotal - descuento_p8  
    elif lugar_p8 == 2: # Santa Marta
        lugar_p8 = "Santa Marta"
        if tribuna_p8 == 1:
            tribuna_p8 = "Sur alta"
            subtotal = 40000
        elif tribuna_p8 == 2:
            tribuna_p8 = "Sur baja"
            subtotal = 40000
        elif tribuna_p8 == 3:
            tribuna_p8 = "Norte alta"
            subtotal = 40000
        elif tribuna_p8 == 4:
            tribuna_p8 = "Norte baja"
            subtotal = 40000
        elif tribuna_p8 == 5:
            tribuna_p8 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p8 == 6:
            tribuna_p8 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p8 == 7:
            tribuna_p8 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p8 == 8:
            tribuna_p8 = "Occidental baja"
            subtotal = 140000
        descuento_p8 = subtotal * valor_descuento_p8
        total_p8 = subtotal - descuento_p8
    else: # Otro
        lugar_p8 = "Otro"
        if tribuna_p8 == 1:
            tribuna_p8 = "Sur alta"
            subtotal = 40000
        elif tribuna_p8 == 2:
            tribuna_p8 = "Sur baja"
            subtotal = 40000
        elif tribuna_p8 == 3:
            tribuna_p8 = "Norte alta"
            subtotal = 40000
        elif tribuna_p8 == 4:
            tribuna_p8 = "Norte baja"
            subtotal = 40000
        elif tribuna_p8 == 5:
            tribuna_p8 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p8 == 6:
            tribuna_p8 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p8 == 7:
            tribuna_p8 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p8 == 8:
            tribuna_p8 = "Occidental baja"
            subtotal = 140000
        descuento_p8 = subtotal * valor_descuento_p8
        total_p8 = subtotal - descuento_p8

# Usuario 9
compra_p9 = 1
lugar_p9 = 3
tribuna_p9 = 6
if compra_p9 == 1: # En línea
    compra_p9 = "En línea"
    if lugar_p9 == 1: # Barranquilla
        lugar_p9 = "Barranquilla"
        valor_descuento_p9 = 0.40 # 40%
        if tribuna_p9 == 1:
            tribuna_p9 = "Sur alta"
            subtotal = 40000
        elif tribuna_p9 == 2:
            tribuna_p9 = "Sur baja"
            subtotal = 40000
        elif tribuna_p9 == 3:
            tribuna_p9 = "Norte alta"
            subtotal = 40000
        elif tribuna_p9 == 4:
            tribuna_p9 = "Norte baja"
            subtotal = 40000
        elif tribuna_p9 == 5:
            tribuna_p9 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p9 == 6:
            tribuna_p9 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p9 == 7:
            tribuna_p9 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p9 == 8:
            tribuna_p9 = "Occidental baja"
            subtotal = 140000
        descuento_p9 = subtotal * valor_descuento_p9
        total_p9 = subtotal - descuento_p9
    elif lugar_p9 == 2: # Santa Marta
        lugar_p9 = "Santa Marta"
        valor_descuento_p9 = 0.25 # 25%
        if tribuna_p9 == 1:
            tribuna_p9 = "Sur alta"
            subtotal = 40000
        elif tribuna_p9 == 2:
            tribuna_p9 = "Sur baja"
            subtotal = 40000
        elif tribuna_p9 == 3:
            tribuna_p9 = "Norte alta"
            subtotal = 40000
        elif tribuna_p9 == 4:
            tribuna_p9 = "Norte baja"
            subtotal = 40000
        elif tribuna_p9 == 5:
            tribuna_p9 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p9 == 6:
            tribuna_p9 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p9 == 7:
            tribuna_p9 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p9 == 8:
            tribuna_p9 = "Occidental baja"
            subtotal = 140000
        descuento_p9 = subtotal * valor_descuento_p9
        total_p9 = subtotal - descuento_p9
    else: # Otro
        lugar_p9 = "Otro"
        # 0% de descuento
        if tribuna_p9 == 1:
            tribuna_p9 = "Sur alta"
            subtotal = 40000
        elif tribuna_p9 == 2:
            tribuna_p9 = "Sur baja"
            subtotal = 40000
        elif tribuna_p9 == 3:
            tribuna_p9 = "Norte alta"
            subtotal = 40000
        elif tribuna_p9 == 4:
            tribuna_p9 = "Norte baja"
            subtotal = 40000
        elif tribuna_p9 == 5:
            tribuna_p9 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p9 == 6:
            tribuna_p9 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p9 == 7:
            tribuna_p9 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p9 == 8:
            tribuna_p9 = "Occidental baja"
            subtotal = 140000
        total_p9 = subtotal
else: # Ventanilla
    compra_p9 = "Ventanilla"
    valor_descuento_p9 = 0.10 # 10%
    if lugar_p9 == 1: # Barranquilla
        lugar_p9 = "Barranquilla"
        if tribuna_p9 == 1:
            tribuna_p9 = "Sur alta"
            subtotal = 40000
        elif tribuna_p9 == 2:
            tribuna_p9 = "Sur baja"
            subtotal = 40000
        elif tribuna_p9 == 3:
            tribuna_p9 = "Norte alta"
            subtotal = 40000
        elif tribuna_p9 == 4:
            tribuna_p9 = "Norte baja"
            subtotal = 40000
        elif tribuna_p9 == 5:
            tribuna_p9 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p9 == 6:
            tribuna_p9 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p9 == 7:
            tribuna_p9 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p9 == 8:
            tribuna_p9 = "Occidental baja"
            subtotal = 140000
        descuento_p9 = subtotal * valor_descuento_p9
        total_p9 = subtotal - descuento_p9  
    elif lugar_p9 == 2: # Santa Marta
        lugar_p9 = "Santa Marta"
        if tribuna_p9 == 1:
            tribuna_p9 = "Sur alta"
            subtotal = 40000
        elif tribuna_p9 == 2:
            tribuna_p9 = "Sur baja"
            subtotal = 40000
        elif tribuna_p9 == 3:
            tribuna_p9 = "Norte alta"
            subtotal = 40000
        elif tribuna_p9 == 4:
            tribuna_p9 = "Norte baja"
            subtotal = 40000
        elif tribuna_p9 == 5:
            tribuna_p9 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p9 == 6:
            tribuna_p9 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p9 == 7:
            tribuna_p9 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p9 == 8:
            tribuna_p9 = "Occidental baja"
            subtotal = 140000
        descuento_p9 = subtotal * valor_descuento_p9
        total_p9 = subtotal - descuento_p9
    else: # Otro
        lugar_p9 = "Otro"
        if tribuna_p9 == 1:
            tribuna_p9 = "Sur alta"
            subtotal = 40000
        elif tribuna_p9 == 2:
            tribuna_p9 = "Sur baja"
            subtotal = 40000
        elif tribuna_p9 == 3:
            tribuna_p9 = "Norte alta"
            subtotal = 40000
        elif tribuna_p9 == 4:
            tribuna_p9 = "Norte baja"
            subtotal = 40000
        elif tribuna_p9 == 5:
            tribuna_p9 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p9 == 6:
            tribuna_p9 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p9 == 7:
            tribuna_p9 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p9 == 8:
            tribuna_p9 = "Occidental baja"
            subtotal = 140000
        descuento_p9 = subtotal * valor_descuento_p9
        total_p9 = subtotal - descuento_p9

# Usuario 10
compra_p10 = 1
lugar_p10 = 3
tribuna_p10 = 7
if compra_p10 == 1: # En línea
    compra_p10 = "En línea"
    if lugar_p10 == 1: # Barranquilla
        lugar_p10 = "Barranquilla"
        valor_descuento_p10 = 0.40 # 40%
        if tribuna_p10 == 1:
            tribuna_p10 = "Sur alta"
            subtotal = 40000
        elif tribuna_p10 == 2:
            tribuna_p10 = "Sur baja"
            subtotal = 40000
        elif tribuna_p10 == 3:
            tribuna_p10 = "Norte alta"
            subtotal = 40000
        elif tribuna_p10 == 4:
            tribuna_p10 = "Norte baja"
            subtotal = 40000
        elif tribuna_p10 == 5:
            tribuna_p10 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p10 == 6:
            tribuna_p10 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p10 == 7:
            tribuna_p10 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p10 == 8:
            tribuna_p10 = "Occidental baja"
            subtotal = 140000
        descuento_p10 = subtotal * valor_descuento_p10
        total_p10 = subtotal - descuento_p10
    elif lugar_p10 == 2: # Santa Marta
        lugar_p10 = "Santa Marta"
        valor_descuento_p10 = 0.25 # 25%
        if tribuna_p10 == 1:
            tribuna_p10 = "Sur alta"
            subtotal = 40000
        elif tribuna_p10 == 2:
            tribuna_p10 = "Sur baja"
            subtotal = 40000
        elif tribuna_p10 == 3:
            tribuna_p10 = "Norte alta"
            subtotal = 40000
        elif tribuna_p10 == 4:
            tribuna_p10 = "Norte baja"
            subtotal = 40000
        elif tribuna_p10 == 5:
            tribuna_p10 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p10 == 6:
            tribuna_p10 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p10 == 7:
            tribuna_p10 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p10 == 8:
            tribuna_p10 = "Occidental baja"
            subtotal = 140000
        descuento_p10 = subtotal * valor_descuento_p10
        total_p10 = subtotal - descuento_p10
    else: # Otro
        lugar_p10 = "Otro"
        # 0% de descuento
        if tribuna_p10 == 1:
            tribuna_p10 = "Sur alta"
            subtotal = 40000
        elif tribuna_p10 == 2:
            tribuna_p10 = "Sur baja"
            subtotal = 40000
        elif tribuna_p10 == 3:
            tribuna_p10 = "Norte alta"
            subtotal = 40000
        elif tribuna_p10 == 4:
            tribuna_p10 = "Norte baja"
            subtotal = 40000
        elif tribuna_p10 == 5:
            tribuna_p10 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p10 == 6:
            tribuna_p10 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p10 == 7:
            tribuna_p10 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p10 == 8:
            tribuna_p10 = "Occidental baja"
            subtotal = 140000
        total_p10 = subtotal
else: # Ventanilla
    compra_p10 = "Ventanilla"
    valor_descuento_p10 = 0.10 # 10%
    if lugar_p10 == 1: # Barranquilla
        lugar_p10 = "Barranquilla"
        if tribuna_p10 == 1:
            tribuna_p10 = "Sur alta"
            subtotal = 40000
        elif tribuna_p10 == 2:
            tribuna_p10 = "Sur baja"
            subtotal = 40000
        elif tribuna_p10 == 3:
            tribuna_p10 = "Norte alta"
            subtotal = 40000
        elif tribuna_p10 == 4:
            tribuna_p10 = "Norte baja"
            subtotal = 40000
        elif tribuna_p10 == 5:
            tribuna_p10 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p10 == 6:
            tribuna_p10 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p10 == 7:
            tribuna_p10 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p10 == 8:
            tribuna_p10 = "Occidental baja"
            subtotal = 140000
        descuento_p10 = subtotal * valor_descuento_p10
        total_p10 = subtotal - descuento_p10  
    elif lugar_p10 == 2: # Santa Marta
        lugar_p10 = "Santa Marta"
        if tribuna_p10 == 1:
            tribuna_p10 = "Sur alta"
            subtotal = 40000
        elif tribuna_p10 == 2:
            tribuna_p10 = "Sur baja"
            subtotal = 40000
        elif tribuna_p10 == 3:
            tribuna_p10 = "Norte alta"
            subtotal = 40000
        elif tribuna_p10 == 4:
            tribuna_p10 = "Norte baja"
            subtotal = 40000
        elif tribuna_p10 == 5:
            tribuna_p10 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p10 == 6:
            tribuna_p10 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p10 == 7:
            tribuna_p10 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p10 == 8:
            tribuna_p10 = "Occidental baja"
            subtotal = 140000
        descuento_p10 = subtotal * valor_descuento_p10
        total_p10 = subtotal - descuento_p10
    else: # Otro
        lugar_p10 = "Otro"
        if tribuna_p10 == 1:
            tribuna_p10 = "Sur alta"
            subtotal = 40000
        elif tribuna_p10 == 2:
            tribuna_p10 = "Sur baja"
            subtotal = 40000
        elif tribuna_p10 == 3:
            tribuna_p10 = "Norte alta"
            subtotal = 40000
        elif tribuna_p10 == 4:
            tribuna_p10 = "Norte baja"
            subtotal = 40000
        elif tribuna_p10 == 5:
            tribuna_p10 = "Oriental alta"
            subtotal = 80000
        elif tribuna_p10 == 6:
            tribuna_p10 = "Oriental baja"
            subtotal = 90000
        elif tribuna_p10 == 7:
            tribuna_p10 = "Occidental alta"
            subtotal = 120000
        elif tribuna_p10 == 8:
            tribuna_p10 = "Occidental baja"
            subtotal = 140000
        descuento_p10 = subtotal * valor_descuento_p10
        total_p10 = subtotal - descuento_p10

# Imprimir resultados
print("Tribuna usuario 1:", tribuna_p1, ", Boleto: $",  total_p1, ", Tipo pago:", compra_p1, ", Lugar:", lugar_p1)
print("Tribuna usuario 2:", tribuna_p2, ", Boleto: $",  total_p2, ", Tipo pago:", compra_p2, ", Lugar:", lugar_p2)
print("Tribuna usuario 3:", tribuna_p3, ", Boleto: $",  total_p3, ", Tipo pago:", compra_p3, ", Lugar:", lugar_p3)
print("Tribuna usuario 4:", tribuna_p4, ", Boleto: $",  total_p4, ", Tipo pago:", compra_p4, ", Lugar:", lugar_p4)
print("Tribuna usuario 5:", tribuna_p5, ", Boleto: $",  total_p5, ", Tipo pago:", compra_p5, ", Lugar:", lugar_p5)
print("Tribuna usuario 6:", tribuna_p6, ", Boleto: $",  total_p6, ", Tipo pago:", compra_p6, ", Lugar:", lugar_p6)
print("Tribuna usuario 7:", tribuna_p7, ", Boleto: $",  total_p7, ", Tipo pago:", compra_p7, ", Lugar:", lugar_p7)
print("Tribuna usuario 8:", tribuna_p8, ", Boleto: $",  total_p8, ", Tipo pago:", compra_p8, ", Lugar:", lugar_p8)
print("Tribuna usuario 9:", tribuna_p9, ", Boleto: $",  total_p9, ", Tipo pago:", compra_p9, ", Lugar:", lugar_p9)
print("Tribuna usuario 10:", tribuna_p10, ", Boleto: $",  total_p10, ", Tipo pago:", compra_p10, ", Lugar:", lugar_p10)

# Mostrar valor venta recaudado
venta_total = total_p1 + total_p2 + total_p3 + total_p4 + total_p5 + total_p6 + total_p7 + total_p8 + total_p9 + total_p10
print("TOTAL VENTAS: $", venta_total)

# Mostrar descuento total
descuento_total = descuento_p1 + descuento_p2 + descuento_p3
print("DESCUENTO VENTAS: $", descuento_total)