import requests
from bs4 import BeautifulSoup

# Solicitar la URL al usuario
url = input("Introduce la URL del listado que quieres scrapear: ")

# Hacer la solicitud HTTP
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Buscar los productos
productos = soup.find_all("li", class_="ui-search-layout__item")

# Verificar si se encontró algún producto
if productos:
    # Iterar sobre los productos y extraer título y precio
    for producto in productos:
        titulo_element = producto.find("h2", class_="ui-search-item__title")
        precio_element = producto.find("span", class_="price-tag-fraction")
        
        if titulo_element and precio_element:
            titulo = titulo_element.text.strip()
            precio = precio_element.text.strip()
            print(f"Título: {titulo}")
            print(f"Precio: {precio}")
        else:
            print("No se pudo encontrar el título o el precio de este producto.")
else:
    print("No se encontraron productos en la página.")
