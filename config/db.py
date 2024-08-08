# config/db.py
from sqlalchemy import create_engine, MetaData

# Detalles de conexión a la base de datos
db_hostname = 'localhost'
db_database = 'Recursos_Humanos'
db_username = 'vospi97'
db_password = '789'
db_port = '5432'

# URL de conexión a la base de datos en formato PostgreSQL
connection_url = f"postgresql://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_database}"

# Creación del motor y la conexión a la base de datos
try:
    engine = create_engine(connection_url)
    conn = engine.connect()
    # Exportar el MetaData
    meta = MetaData()
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

# Asegúrate de que `meta` se exporte
__all__ = ["conn", "meta"]
