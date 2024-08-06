from sqlalchemy import Table, Column, Integer, String, Date
from config.db import meta, engine

# Definición de la tabla 'empleados'
empleados = Table(
    'empleados', meta,
    Column('id_empleado', Integer, primary_key=True, autoincrement=True),  # ID único con autoincremento (llave primaria)
    Column('nombres', String(100), nullable=False),  # Nombres del empleado, no nulo
    Column('apellidos', String(100), nullable=False),  # Apellidos del empleado, no nulo
    Column('cc', String(50), unique=True, nullable=False),  # Cédula única y no nula
    Column('fecha_nacimiento', Date, nullable=False),  # Fecha de nacimiento, no nula
    Column('direccion', String(200), nullable=True),  # Dirección del empleado, puede ser nula
    Column('telefono', String(20), nullable=True),  # Teléfono del empleado, puede ser nulo
    Column('email', String(100), nullable=True),  # Email del empleado, puede ser nulo
    Column('tipo_sangre', String(10), nullable=True)  # Tipo de sangre del empleado, puede ser nulo
)

# Creación de la tabla en la base de datos
try:
    meta.create_all(engine)
except Exception as e:
    print(f"Error al crear la tabla 'empleados': {e}")
