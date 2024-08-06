from sqlalchemy import Table, Column, Integer, String, ForeignKey
from config.db import meta, engine

# Definición de la tabla 'departamentos'
departamentos = Table(
    'departamentos', meta,
    Column('id_departamento', Integer, primary_key=True, autoincrement=True),  # ID único con autoincremento
    Column('nombre', String(100), nullable=False),  # Nombre del departamento, no nulo
    Column('id_gerente', Integer, ForeignKey('empleados.id_empleado'), nullable=True),  # ID del gerente, puede ser nulo
    Column('correo', String(100), nullable=True),  # Correo del departamento, puede ser nulo
    Column('telefono', String(20), nullable=True)  # Teléfono del departamento, puede ser nulo
)

# Creación de la tabla en la base de datos
try:
    meta.create_all(engine)
except Exception as e:
    print(f"Error al crear la tabla 'departamentos': {e}")
