import requests
try:
    n = float(input("Por favor, ingrese la cantidad de bitcoins que posee: "))
except ValueError:
    print("Error: ingrese un número válido.")
    exit()
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    precio_bitcoin_usd = float(data['bpi']['USD']['rate'].replace(",", ""))
    costo_total = n * precio_bitcoin_usd
    print(f"El valor actual de {n} Bitcoins es: ${costo_total:,.4f} USD")

except requests.RequestException as e:
    print("Ocurrió un error al realizar la consulta:", e)
except KeyError:
    print("No se pudo obtener la información del precio actual.")
