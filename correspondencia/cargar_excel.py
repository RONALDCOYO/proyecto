import pandas as pd
import mysql.connector

# Configuración de conexión a MySQL
conexion = mysql.connector.connect(
    host='localhost',     # Cambia según tu configuración
    user='root',    # Tu usuario de MySQL
    password='123ABCJG',  # Tu contraseña de MySQL
    database='gestion'  # La base de datos donde está la tabla
)

# Leer el archivo de Excel
archivo_excel = '/media/Dependencias.xlsx'  # Cambia a la ruta de tu archivo
archivo_excel = 'C:\\proyecto\\media\\Dependencias.xlsx'
df = pd.read_excel(archivo_excel)

# Asegúrate de que las columnas coinciden con las de la tabla en MySQL
# Supongamos que el archivo Excel tiene las columnas 'id', 'nombre', 'codigo', y 'empresa_id'
for _, row in df.iterrows():
    cursor = conexion.cursor()
    sql = """
    INSERT INTO gestion_dependencia (id, nombre, codigo, empresa_id) 
    VALUES (%s, %s, %s, %s)
    """
    valores = (row['id'], row['nombre'], row['codigo'], row['empresa_id'])
    cursor.execute(sql, valores)

conexion.commit()
conexion.close()

print("Datos cargados exitosamente.")
