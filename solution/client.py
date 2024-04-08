import requests

base_url = 'http://localhost:8000/orders'

orders = [
    {
        "client": "Eduardo Valdez",
        "status": "Pendiente",
        "payment": "Tarjeta de Crédito",
        "shipping": 10.0,
        "products": ["Camiseta", "Pantalón", "Zapatos"],
        "order_type": "Física"
    },
    {
        "client": "Maria Rodriguez",
        "status": "Pendiente",
        "payment": "PayPal",
        "code": "ABC123",
        "expiration": "2022-12-31",
        "order_type": "Digital"
    },
    {
        "client": "Carlos Mendoza",
        "status": "Pendiente",
        "payment": "Bitcoin",
        "shipping": 15.0,
        "products": ["Libro", "Lápiz", "Cuaderno"],
        "order_type": "Física"
    },
    {
        "client": "Patricia Paredes",
        "status": "Pendiente",
        "payment": "Transferencia Bancaria",
        "code": "XYZ456",
        "expiration": "2023-01-31",
        "order_type": "Digital"
    },
    {
        "client": "Luis Guzman",
        "status": "Pendiente",
        "payment": "Tarjeta de Débito",
        "shipping": 20.0,
        "products": ["Silla", "Mesa", "Lámpara"],
        "order_type": "Física"
    },
    {
        "client": "Gabriela Torres",
        "status": "Pendiente",
        "payment": "PayPal",
        "code": "DEF789",
        "expiration": "2023-02-28",
        "order_type": "Digital"
    },
    {
        "client": "Ana Gutierrez",
        "status": "Pendiente",
        "payment": "Tarjeta de Débito",
        "shipping": 20.0,
        "products": ["Licuadora", "Refrigeradora", "Lavadora"],
        "order_type": "Física"
    }
]

for order in orders:
    response = requests.post(base_url, json=order)
    print(response.json())

response = requests.get(base_url)
print(response.json())
