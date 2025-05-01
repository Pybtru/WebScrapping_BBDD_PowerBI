import sqlite3

# Abrir y leer el archivo de texto
with open('resultado_maquinas.txt', 'r') as file:
    raw_data = file.read()

# Convertimos la salida en una lista de diccionarios
maquinas_obtenidas = []
for line in raw_data.strip().split('\n'):
    # Asegurarnos de que la línea tiene exactamente tres partes
    try:
        nombre, dificultad, autor = line.split(" --> ")
        maquinas_obtenidas.append({
            "nombre": nombre.strip(),
            "dificultad": dificultad.strip(),
            "autor": autor.strip()
        })
    except ValueError:
        # Si la línea no tiene tres partes, la ignoramos
        print(f"Línea ignorada (formato incorrecto): {line}")

# Conexión a la base de datos SQLite
conn = sqlite3.connect("listado_maquinas.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS maquinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    dificultad TEXT,
    autor TEXT
)
""")

# Preparar los datos de las maquinas para insertar
maquinas = [(maquina["nombre"], maquina["dificultad"], maquina["autor"]) for maquina in maquinas_obtenidas]

# Insertar los datos en la tabla maquinas
cursor.executemany("""
INSERT INTO maquinas (nombre, dificultad, autor)
VALUES (?, ?, ?)
""", maquinas)

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

print("✅ Datos insertados correctamente en la base de datos.")