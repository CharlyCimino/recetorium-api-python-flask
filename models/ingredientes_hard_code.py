ingrediente_id_counter = 25

def next_id():
    global ingrediente_id_counter
    ingrediente_id_counter += 1
    return ingrediente_id_counter

lista_de_ingredientes = [
    {"id": 1, "nombre": 'Masa', "foto": '/api/ingredientes/img/ing_1.jpg', "color": '#EBE6D8'},
    {"id": 2, "nombre": 'Tomate', "foto": '/api/ingredientes/img/ing_2.jpg', "color": '#EA1A03'},
    {"id": 3, "nombre": 'Mozzarella', "foto": '/api/ingredientes/img/ing_3.jpg', "color": '#F0D9C2'},
    {"id": 4, "nombre": 'Albahaca', "foto": '/api/ingredientes/img/ing_4.jpg', "color": '#568207'},
    {"id": 5, "nombre": 'Lechuga', "foto": '/api/ingredientes/img/ing_5.jpg', "color": '#78BF27'},
    {"id": 6, "nombre": 'Crutón', "foto": '/api/ingredientes/img/ing_6.jpg', "color": '#E09828'},
    {"id": 7, "nombre": 'Pollo', "foto": '/api/ingredientes/img/ing_7.jpg', "color": '#CFB6BA'},
    {"id": 8, "nombre": 'Queso Parmesano', "foto": '/api/ingredientes/img/ing_8.jpg', "color": '#DFCAB3'},
    {"id": 9, "nombre": 'Salsa César', "foto": '/api/ingredientes/img/ing_9.jpg', "color": '#D5C5A6'},
    {"id": 10, "nombre": 'Carne picada', "foto": '/api/ingredientes/img/ing_10.jpg', "color": '#AB5D60'},
    {"id": 11, "nombre": 'Ricota', "foto": '/api/ingredientes/img/ing_11.jpg', "color": '#F0E8DC'},
    {"id": 12, "nombre": 'Arroz', "foto": '/api/ingredientes/img/ing_12.jpg', "color": '#C0B8A1'},
    {"id": 13, "nombre": 'Caldo', "foto": '/api/ingredientes/img/ing_13.jpg', "color": '#6D624C'},
    {"id": 14, "nombre": 'Morrón', "foto": '/api/ingredientes/img/ing_14.jpg', "color": '#D6311B'},
    {"id": 15, "nombre": 'Camarones', "foto": '/api/ingredientes/img/ing_15.jpg', "color": '#F96060'},
    {"id": 16, "nombre": 'Palta', "foto": '/api/ingredientes/img/ing_16.jpg', "color": '#576D1C'},
    {"id": 17, "nombre": 'Tortilla de maiz', "foto": '/api/ingredientes/img/ing_17.jpg', "color": '#E1CEBA'},
    {"id": 18, "nombre": 'Canela', "foto": '/api/ingredientes/img/ing_18.jpg', "color": '#BB7744'},
    {"id": 19, "nombre": 'Cebolla', "foto": '/api/ingredientes/img/ing_19.jpg', "color": '#BF8671'},
    {"id": 20, "nombre": 'Champignones', "foto": '/api/ingredientes/img/ing_20.jpg', "color": '#EFE3CE'},
    {"id": 21, "nombre": 'Lentejas', "foto": '/api/ingredientes/img/ing_21.jpg', "color": '#E4C6A0'},
    {"id": 22, "nombre": 'Zanahoria', "foto": '/api/ingredientes/img/ing_22.jpg', "color": '#F47309'},
    {"id": 23, "nombre": 'Especias', "foto": '/api/ingredientes/img/ing_23.jpg', "color": '#B14805'},
    {"id": 24, "nombre": 'Manzana', "foto": '/api/ingredientes/img/ing_24.jpg', "color": '#C71B35'},
    {"id": 25, "nombre": 'Ajo', "foto": '/api/ingredientes/img/ing_25.jpg', "color": '#D5B49F'}
]
