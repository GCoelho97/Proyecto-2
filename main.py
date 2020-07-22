import requests
from Client import Client
#def show_stats(tour_clients, tour_spend, tickets_clients, tickets_spend):
   # """show_stats Saca las estadisticas que se piden
    
   # Arguments:
    #    tour_clients, tour_spend, tickets_clients, tickets_spend {list} -- Clientes de tour, gasto de tour, clientes de cruceros, gasto de cruceros
        
    #return:
     #   Print -- Las estadisticas que se piden
    #"""
 #   total_tour_spend = sum(tour_spend)
  #  total_tour_clients = sum(tour_clients)

   # print(f'El promedio de gasto de cliente es: {total_tour_spend} + {total_tickets_spend}/{tour_clients} + {tickets_clients})
   # print(f'Los clientes que no compran tour son: {tickets_clients*100}/{tour_clients} + {tickets_clients})

def tour_stats(file_name):
    """tour_stats Revisa las estadisticas de tour
    
    Arguments:
        tour_log.txt {txt} -- Log de tours
        
    return:
        List -- Cantidad de clientes y de gasto
    """
    tour_spend = []
    tour_clients = []
    with open(file_name) as f:
        for line in f:
            tour_spend.append(line.split(',')[1])
    return tour_spend

    with open(file_name) as f:
        for line in f:
            tour_clients.append(line.split(',')[2])
    return tour_clients

def check_food_option(food_option):
    """check_food_option Revisa que se eliga una opcion viable
    
    Arguments:
        food_option {input} -- La respuesta de la persona
        
    return:
        bool -- Si la opcion es viable
    """
    if food_option == '1' or food_option == '2' or food_option == '3' or food_option == '4' or food_option == '5' or food_option == '6' or food_option == '7':
        return True
    else:
        return False

def check_food_type(food_type):
    """check_food_type Revisa si es una comida o bebida
    
    Arguments:
        food_option {input} -- El tipo de comida
        
    return:
        bool -- Si la respuesta es aceptada o no
    """
    if food_type == 'comida' or food_type == 'bebida':
        return True
    else:
        return False

def check_new_food(new_food):
    """check_new_food Revisa que la comida tenga un nombre de puras letras
    
    Arguments:
        new_food {input} -- La comida introducida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if new_food.isalpha():
        return True
    else:
        return False

def check_new_food_price(new_food_prices):
    """check_new_food_price Revisa que el precio sea un numero
    
    Arguments:
        new_food_prices {input} -- El precio de la comida
        
    return:
        bool -- Si el precio es aceptado
    """
    if new_food_prices.isnumeric():
        return True
    else:
        return False

def check_food_size(food_size):
    """check_food_size Revisa que el tamaño sea aceptado (pequeña/mediana/grande/no)
    
    Arguments:
        food_size {input} -- El tamaño de la comida
        
    return:
        bool -- Si el tamaño es aceptado
    """
    if food_size == 'pequeña' or food_size == 'mediana' or food_size == 'grande' or food_size == 'no':
        return True
    else:
        return False

def check_food_cont(food_cont):
    """check_food_cont Revisa que como se guarda la comida sea aceptado
    
    Arguments:
        food_cont {input} -- Como se guarda la comida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if food_cont == 'empaque' or food_cont == 'preparacion':
        return True
    else:
        return False

def check_combo_price(combo_price):
    """check_combo_price Revisa que el precio de los combos sea un numero
    
    Arguments:
        combo_price {input} -- El precio del combo
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if combo_price.isnumeric():
        return True
    else:
        return False

def check_delete_food(delete_food):
    """check_delete_food Revisa que la comida sean letras
    
    Arguments:
        delete_food {input} -- La comida ingresada
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if delete_food.isalpha():
        return True
    else:
        return False

def check_delete_combo(delete_combo):
    """check_delete_combo Revisa que el nombre del combos sean letras
    
    Arguments:
        delete_combo {input} -- El nombre del combo a eliminar
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if delete_combo.isalpha():
        return True
    else:
        return False

def manage_food(food, combos, file_name):
    """manage_food Se encarga de la parte de administrar comida
    
    Arguments:
        food, combos {dict} -- Los menus de comida y combos
        
    return:
        dict -- Los menus actualizados
    """
    while True:
        try:
            food_option = input("""Que desea hacer
            1- Agregar platos
            2- Eliminar producto
            3- Modificar producto
            4- Agregar combos
            5- Eliminar combos
            6- Buscar productos
            7- Buscar combos
            -""")
            if not check_food_option(food_option):
                raise Exception
            break
        except:
            print("Valor Invalido")
    
    if food_option == '1':
        while True:
            try:
                food_type = input("Que tipo de comida quiere agregar (comida/bebida):")
                if not check_food_type(food_type):
                    raise Exception
                new_food = input("Nombre de la nueva comida:")
                if not check_new_food(new_food):
                    raise Exception
                new_food_price = input("Precio de la nueva comida:")
                if not check_new_food_price(new_food_price):
                    raise Exception
                break
            except:
                print("Valor invalido")
        
        food_size = 'no aplica'
        food_cont = 'no aplica'
        if food_type == 'bebida':
            while True:
                try:
                    food_size = input("Tamaño de bebida (pequeña/mediana/grande):")
                    if not check_food_size(food_size):
                        raise Exception
                    break
                except:
                    print("Valor Invalido")

        if food_type == 'comida':
            while True:
                try:
                    food_cont = input("Como guardar el alimento (empaque/preparacion):")
                    if not check_food_cont(food_cont):
                        raise Exception
                    break
                except:
                    print("Valor Invalido")
            


        food_price = int(new_food_price) + (int(new_food_price)*.16) 
        food = f'Nombre: {new_food}', f'tipo: {food_type}',f'precio: {food_price}',f' tamaño: {food_size}',f' guardar: {food_cont}'

    elif food_option == '2':

        while True:
            try:
                delete_food = input("Cual comida desea eliminar:")
                if not check_delete_food(delete_food):
                    raise Exception
                break
            except:
                print("Valor Invalido")

        del food[f'{delete_food}']

    elif food_option == '3':
        while True:
            try:
                modify = input("Cual comida desea modificar:")
                food_type = input("Introduzca el tipo:")
                if not check_food_type(food_type):
                    raise Exception
                new_food_price = input("Introduzca el precio:")
                if not check_new_food_price(new_food_price):
                    raise Exception
                food_size = input("Introduzca el tamaño (pequeña/mediana/grande/no):")
                if not check_food_size(food_size):
                    raise Exception
                food_cont = input("Como guardar (empaque/preparacion)")
                if not check_food_cont(food_cont):
                    raise Exception
                break
            except:
                print("Valor Invalido")

        del food[f'{modify}']
        food_price = int(new_food_price) + (int(new_food_price)*.16)
        food[f'{modify}'] = f'Nombre: {modify}',f'tipo: {food_type}',f'precio: {food_price}',f' tamaño: {food_size}',f' guardar: {food_cont}'

    elif food_option == '4':
        while True:
            try:
                new_combo = input("Nombre del nuevo combo:")
                items = input("Introduzca los items:")
                combo_price = input("Introduzca el precio:")
                if not check_combo_price(combo_price):
                    raise Exception
                break
            except:
                print("Valor Invalido")

        combo_price_real = int(combo_price) + (int(combo_price)*.16) 
        combos[f'{new_combo}'] = f'Nombre {new_combo}',f'Items: {items}', f'Precio: {combo_price_real}'
    
    elif food_option == '5':

        while True:
            try:
                delete_combo = input("Cual combo desea eliminar:")
                if not check_delete_combo(delete_combo):
                    raise Exception
                break
            except:
                print("Valor Invalido")

        del combos[f'{delete_combo}']

    elif food_option == '6':

            while True:
                try:
                    new_food = input("Cual comida desea buscar:")
                    if not check_new_food(new_food):
                        raise Exception
                    break
                except:
                    print("Valor Invalido")

            if new_food in food:
                return food['new_food']
            else:
                return 'No Se Encuentra!'

    elif food_option == '7':

            while True:
                try:
                    new_food = input("Cual combo desea buscar:")
                    if not check_new_food(new_food):
                        raise Exception
                    break
                except:
                    print("Valor Invalido")

            if new_food in combos:
                return combos[f'{new_food}']
            else:
                return 'No Se Encuentra!'

    with open(file_name, 'a') as f:
            f.write(f'{food} \n')

    with open(file_name, 'a') as f:
        f.write(f'{combos}, \n')

    return food, combos

def open_menu(file_name):
    """open_menu Abre el texto del menu
    
    Arguments:
        menu.txt {txt} -- El texto del menu
        
    return:
        txt -- El contenido del txt
    """
    with open(file_name) as f:
           print(f.read())

def check_tour_choice(tour_choice):
    """check_tour_choice Revisa que el tour elegido sea una opcion viable
    
    Arguments:
        tour_choice {input} -- El tour elegido
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if tour_choice == '1' or tour_choice == '2' or tour_choice == '3' or tour_choice == '4':
        return True
    else:
        return False

def check_tour_clients(tour_clients):
    """check_tour_clients Revisa que la cantidad de clientes sea un numero
    
    Arguments:
        tour_clients {input} -- La cantidad de clientes
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if tour_clients.isnumeric():
        return True
    else:
        return False

def reserve_tour(tour_tickets, file_name):
    """reserve_tour Comprar boletos para tours
    
    Arguments:
        tour_tickets, tour_log.txt {txt} -- Cupos de tour, El registro de tour
        
    return:
        list -- Cupos actualizado
    """
    while True:
        try:
            id_num = input("Cual es su cedula:")
            if not check_id(id_num):
                raise Exception
            tour_choice = input("""Cual tour desea
            1- Tour en el puerto
            2- Degustacion de Comida
            3- Trotar por la ciudad
            4- Visita lugares historicos
            -""")
            if not check_tour_choice(tour_choice):
                raise Exception
            tour_clients = input("Cuantas personas:")
            if not check_tour_clients(tour_clients):
                raise Exception
            break
        except:
            print("Valor Invalido")

    price = 0
    time = '00:00'

    if tour_choice == '1':
        if int(tour_clients) > tour_tickets[0]:
                print(f"No hay cupos suficientes, quedan {tour_tickets[0]} cupos")
        elif tour_clients > '4':
            print("Hasta 4 personas")
        elif tour_clients == '3':
            price = 87
            time = '7 AM'
            tour_tickets[0] = tour_tickets[0] - int(tour_clients)
        elif tour_clients == '4':
            price = 114
            time = '7 AM'
            tour_tickets[0] = tour_tickets[0] - int(tour_clients)
        else:
            price = 30 * int(tour_clients)
            time = '7 AM'
            tour_tickets[0] = tour_tickets[0] - int(tour_clients)

    elif tour_choice == '2':
        if int(tour_clients) > tour_tickets[1]:
            print(f"No hay cupos suficientes, quedan {tour_clients[1]} cupos")
        elif tour_clients > '2':
            print("Hasta 2 personas")
        else:
            price = 100 * int(tour_clients)
            time = '12 PM'
            tour_tickets[1] = tour_tickets[1] - int(tour_clients)
        
    elif tour_choice == '3':

        price = 0
        time = '6 AM'

    elif tour_choice == '4':
        if int(tour_clients) > tour_tickets[2]:
            print(f"No hay cupos suficientes, quedan {tour_tickets[2]} cupos")
        if tour_clients > '4':
            print("Hasta 4 personas")
        elif tour_clients == '3':
            price = 116
            time = '10 AM'
            tour_tickets[2] = tour_tickets[2] - int(tour_clients)
        elif tour_clients == '4':
            price = 152
            time = '10 AM'
            tour_tickets[2] = tour_tickets[2] - int(tour_clients)
        else:
            price = 40 * int(tour_clients)
            time = '10 AM'
            tour_tickets[2] = tour_tickets[2] - int(tour_clients)

    print(f'Su precio es {price} y el tiempo de partida es {time}')

    result = f' Cedula {id_num},{price},1,'
    with open(file_name, 'a') as f:
        f.write(f'{result} \n')

    return tour_tickets

def open_tour_log(file_name):
    """open_tour_log Abre el texto de tour
    
    Arguments:
        tour_log.txt {txt} -- El texto del tour 
        
    return:
        txt -- El contenido del texto
    """
    with open(file_name) as f:
           print(f.read())

def check_choice(choice):
    """check_choice Revisa si la opcion elegida es un numero
    
    Arguments:
        choice {input} -- La opcion elegida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if choice == '1' or choice == '2':
        return True
    else:
        return False

def check_room_type(room_type):
    """check_room_type Revisa que el tipo de cuarto elegido sea una opcion viable (numero)
    
    Arguments:
        room_type {input} -- La opcion elegida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if room_type == '1' or room_type == '2' or room_type == '3':
        return True
    else:
        return False

def check_number(number_people):
    """check_number Revisa que la cantidad de personas sea un numero
    
    Arguments:
        number_people {input} -- La cantidad elegida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if number_people.isnumeric():
        return True
    else:
        return False

def check_name(name):
    """check_name Revisa que se introduzca un nombre aceptado
    
    Arguments:
        name {input} -- El nombre de la persona
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if name.isalpha():
        return True
    else:
        return False

def check_id(id_number):
    """check_id Revisa si la cedula ingresada es un numero
    
    Arguments:
        id_number {input} -- El numero de cedula
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if id_number.isnumeric():
        return True
    else:
        return False

def check_age(age):
    """check_age Revisa si la edad elegida es un numero
    
    Arguments:
        age {input} -- La edad elegida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if age.isnumeric():
        return True
    else:
        return False

def check_cripple(cripple):
    """check_cripple Revisa si la opcion elegida es aceptada
    
    Arguments:
        cripple {input} -- La opcion elegida
        
    return:
        bool -- Si la respuesta es aceptada
    """
    if cripple == '1' or cripple == '2':
        return True
    else:
        return False

def id_prime(id_num):
    """id_prime Revisa que la cedula sea un numero primo
    
    Arguments:
        id_num {input} -- La cedula ingresada
        
    return:
        bool -- Si la cedula es un numero primo
    """
    if id_num > 1:
        for i in range(2, id_num//2):
            if (id_num % i) == 0:
                return False
    else:
        return True

def id_abun(id_num):
    """id_abun Revisa que la cedula es un numero abundante
    
    Arguments:
        id_num {input} -- La cedula ingresada
        
    return:
        bool -- Si la cedula es un numero abundante
    """
    divisores = []
    for i in range(1, id_num):
        if id_num % i == 0:
            divisores.append(i)
    suma_divisores = sum(divisores)

    if suma_divisores > id_num:
        return True
    
    elif suma_divisores <= id_num:
        return False

def check_decision(decision):
    """check_decision Revisa que se eliga una opcion viable
    
    Arguments:
        decision {input} -- La decision del barco que se desea tomar
        
    return:
        bool -- Si es una opcion viable
    """
    if decision == '1' or decision == '2' or decision == '3' or decision == '4':
        return True
    else:
        return False

def register_client(file_name):
    """register_clients Registra la compra de un crucero
    
    Arguments:
        clients.txt {txt}-- La lista de clientes
    return:
        list -- La lista de clientes actualizada
    """

    name = ''
    decision = ''
    amount = 0
    number_people = 0
    id_num = 0
    age = 0
    cripple = ''

    url = "https://saman-caribbean.vercel.app/api/cruise-ships"
    data = requests.get(url).json()

    name_1 = data[0]['name']
    name_2 = data[1]['name']
    name_3 = data[2]['name']
    name_4 = data[3]['name']
    names = name_1, name_2, name_3, name_4

    route_1 = data[0]['route']
    route_2 = data[1]['route']
    route_3 = data[2]['route']
    route_4 = data[3]['route']
    routes = route_1, route_2, route_3, route_4

    while True:
        try:

            choice = input("Comprar en base a (1-Barco/2-Destino): ")
            if not check_choice(choice):
                raise Exception
            break
        except:
            print("Valor Invalido")
    
    if choice == '1':

        print (f'{names}')

        while True:
            try:
                decision = input("Cual barco desea tomar (1/2/3/4):")
                if not check_decision(decision):
                    raise Exception
                break
            except:
                print("Valor Invalido")

    elif choice == '2':

        print(f'{routes}')

        while True:
            try:
                decision = input("Cual barco desea tomar (1/2/3/4):")
                if not check_decision(decision):
                    raise Exception
                break
            except:
                print("Valor Invalido")
    
    while True:
            try:
                room_type = input("Tipo de cuarto: 1-Simple/2-Premium/3-VIP: ")
                if not check_room_type(room_type):
                    raise Exception
                break
                number_people = input("Cuantas personas viajan con usted?:")
                if not check_number(number_people):
                    raise Exception
                break

                name = input("Cual es su nombre?:")
                if not check_name(name):
                    raise Exception
                break

                id_num = input("Cual es su ID?:")
                if not check_id(id_num):
                    raise Exception
                break 

                age = input("Cual es su edad?:")
                if not check_age(age):
                    raise Exception
                break

                cripple = input("Tiene alguna discapacidad 1-Si/2-No:")
                if not check_cripple(cripple):
                    raise Exception
                break
            except:
                print("Valor Invalido")

    if decision == '1':

        if room_type == '1':
            amount = 69.99
        elif room_type == '2':
            amount = 89.99
        elif room_type == '3':
            amount = 129.99

    elif decision == '2':
        if room_type == '1':
            amount = 59.99
        elif room_type == '2': 
            amount = 99.99
        elif room_type == '3':
            amount = 119.99

    elif decision == '3':
        if room_type == '1':
            amount = 49.99
        elif room_type == '2':
            amount = 89.99
        elif room_type == '3':
            amount = 139.99

    elif decision == '4':
        if room_type == '1':
            amount = 59.99
        elif room_type == '2':
            amount = 99.99
        elif room_type == '3':
            amount = 119.99 

    if cripple == '1':

        amount = amount *(.70)

    if id_prime(id_num):

        amount = amount *(.90)

    if id_abun(id_num):

        amount = amount *(85)

    client = Client(name, decision, amount, number_people, id_num, age, cripple)

    with open(file_name, 'a') as f:
        f.write(f'{client.name}\n {client.id_num}\n {client.age}\n {client.amount}')

    return client

def open_clients(file_name):
    """open_clients Abre el texto de clientes
    
    Arguments:
        clients.txt {txt} -- El texto de clientes
        
    return:
        txt -- El contenido del texto
    """
    with open(file_name) as f:
           print(f.read())

def leave_room(clients):
    """leave_room Elimina a un cliente de la lista
    
    Arguments:
        clients {list} -- La lista de clientes
        
    return:
        list -- La lista actualizada
    """
    while True:
        try:
            name = input("Ingrese su nombre: ")
            if not check_name(name):
                raise Exception
        except:
            print("Valor Invalido")

    for client in clients:
        if client.name == name:
            client.leave()
            return True
    return False

def check_ships():
    """check_ships Muestra los barcos disponibles
    
    Arguments:
        Api -- La base de datos de los barcos
        
    return:
        Str -- Los datos de los barcos disponibles
    """
    url = "https://saman-caribbean.vercel.app/api/cruise-ships"

    data = requests.get(url).json()
    name_1 = data[0]['name']
    route_1 = data[0]['route']
    departure_1 = data[0]['departure']
    capacity_1 = data[0]['capacity']
    cost_1 = data[0]['cost']
    rooms_1 = data[0]['rooms']

    name_2 = data[1]['name']
    route_2 = data[1]['route']
    departure_2 = data[1]['departure']
    capacity_2 = data[1]['capacity']
    cost_2 = data[1]['cost']
    rooms_2 = data[1]['rooms']

    name_3 = data[2]['name']
    route_3 = data[2]['route']
    departure_3 = data[2]['departure']
    capacity_3 = data[2]['capacity']
    cost_3 = data[2]['cost']
    rooms_3 = data[2]['rooms']

    name_4 = data[3]['name']
    route_4 = data[3]['route']
    departure_4 = data[3]['departure']
    capacity_4 = data[3]['capacity']
    cost_4 = data[3]['cost']
    rooms_4 = data[3]['rooms']

    data_1 = name_1, route_1, departure_1, capacity_1, cost_1, rooms_1
    data_2 = name_2, route_2, departure_2, capacity_2, cost_2, rooms_2
    data_3 = name_3, route_3, departure_3, capacity_3, cost_3, rooms_3
    data_4 = name_4, route_4, departure_4, capacity_4, cost_4, rooms_4

    return f'{data_1}\n {data_2}\n {data_3}\n {data_4}'

def main():

    clients = []
    food = {}
    combos = {}
    tour_tickets = [10, 100, 15]
    tour_clients = 0
    tour_spend = 0
    tickets_clients = 0
    tickets_spend = 0

    while True:

        opcion = input("""Bienvenido a Saman Caribbean!
        1- Ver Cruceros Disponibles
        2- Reservar Cuartos
        3- Desalojar Cuartos
        4- Ver Clientes
        5- Reservar Tour
        6- Ver Registro de Compra de Tour
        7- Administrar Comida
        8- Ver Registro de Menu
        9- Gestion Administrativa
        10- Salir
        """)

        if opcion == '1':

            print(check_ships())
        
        elif opcion == '2':
            
            clients.append(register_client('clients.txt'))

        elif opcion == '3':

            if not leave_room(clients):
                print("No existe el Cliente")

        elif opcion == '4':

            open_clients('clients.txt')

        elif opcion == '5':

            reserve_tour(tour_tickets, 'tour_log.txt')
        
        elif opcion == '6':

            open_tour_log('tour_log.txt')

        elif opcion == '7':

            print(manage_food(food, combos,'menu.txt'))

        elif opcion == '8':

            open_menu('menu.txt')

        elif opcion == '9':

            #tour_stats('tour_log.txt')
            #room_stats()
            #food_stats('menu.txt')
            #print(show_stats(tour_clients, tour_spend))
            pass
        
        else:
            print("Adios")
            break


main()