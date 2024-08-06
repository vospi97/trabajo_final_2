from sqlalchemy import create_engine, MetaData

# Detalles de conexión a la base de datos
db_hostname = 'localhost'  # Nombre del host donde se encuentra la base de datos
db_database = 'Recursos_Humanos'  # Nombre de la base de datos
db_username = 'vospi97'  # Nombre de usuario de la base de datos
db_password = '789'  # Contraseña del usuario de la base de datos
db_port = '5432'  # Puerto de la base de datos

# URL de conexión a la base de datos en formato PostgreSQL

# Conexión con contraseña
connection_url = f"postgresql://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_database}"

# Creación del motor y la conexión a la base de datos
try:
    # Creación del motor de conexión con SQLAlchemy
    engine = create_engine(connection_url)
    # Establecimiento de la conexión a la base de datos
    conn = engine.connect()
    # MetaData se utiliza para la gestión de la información sobre la estructura de la base de datos
    meta = MetaData()
except Exception as e:
    # Manejo de excepciones en caso de error al conectar con la base de datos
    print(f"Error al conectar con la base de datos: {e}")
