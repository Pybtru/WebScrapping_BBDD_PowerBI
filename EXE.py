import requests
from bs4 import BeautifulSoup

url = 'https://dockerlabs.es/'
respuesta = requests.get(url)

# Abrir el archivo en modo escritura
with open("resultado_maquinas.txt", "w", encoding="utf-8") as file:
    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        maquinas = soup.find_all('div', onclick=True)
        conteo_maquinas = 1
        autores = set()

        # Guardar autores encontrados en el archivo
        file.write("Autores encontrados:\n")
        for autor in autores:
            file.write(f"{autor}\n")

        # Procesar y guardar cada máquina en el archivo
        for maquina in maquinas:
            onclick_text = maquina['onclick']
            autor = onclick_text.split("'")[7]
            autores.add(autor)
            nombre_maquina = onclick_text.split("'")[1]
            dificultad = onclick_text.split("'")[3]

            file.write(f"{nombre_maquina} --> {dificultad} --> {autor}\n")

        print("✅ Resultados guardados en 'resultado_maquinas.txt'")

    else:
        print(f"Hubo un error al hacer la petición {respuesta.status_code}")
