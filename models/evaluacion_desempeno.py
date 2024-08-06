from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.types import DECIMAL  
from config.db import meta, engine

# Definición de la tabla 'evaluacion_desempeno'
evaluacion_desempeno = Table(
    'evaluacion_desempeno', meta,
    Column('id_evaluacion', Integer, primary_key=True, autoincrement=True),  # ID único con autoincremento
    Column('id_empleado', Integer, ForeignKey('empleados.id_empleado'), nullable=False),  # Clave foránea a empleados, no nula
    Column('id_periodo', Integer, ForeignKey('periodo_facturacion.id_periodo'), nullable=False),  # Clave foránea a periodo_facturacion, no nula
    Column('calificacion', DECIMAL(3, 2), nullable=True)  # Calificación del desempeño, puede ser nula
)

# Creación de la tabla en la base de datos
try:
    meta.create_all(engine)
except Exception as e:
    print(f"Error al crear la tabla 'evaluacion_desempeno': {e}")
