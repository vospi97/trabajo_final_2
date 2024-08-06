from sqlalchemy import Table, Column, Integer, Date, ForeignKey
from sqlalchemy.types import DECIMAL  
from config.db import meta, engine

# Definición de la tabla 'registro_nomina'
registro_nomina = Table(
    'registro_nomina', meta,
    Column('id_nomina', Integer, primary_key=True, autoincrement=True),  # ID único con autoincremento
    Column('id_contrato', Integer, ForeignKey('contratos.id_contrato'), nullable=False),  # Clave foránea, no nula
    Column('fecha_pago', Date, nullable=True),  # Fecha de pago, puede ser nula
    Column('salario_base', DECIMAL(10, 2), nullable=True),  # Salario base, puede ser nulo
    Column('deducciones', DECIMAL(10, 2), nullable=True),  # Deducciones, pueden ser nulas
    Column('salario_neto', DECIMAL(10, 2), nullable=True),  # Salario neto, puede ser nulo
    Column('id_periodo', Integer, ForeignKey('periodo_facturacion.id_periodo'), nullable=True)  # Clave foránea, puede ser nula
)

# Creación de la tabla en la base de datos
try:
    meta.create_all(engine)
except Exception as e:
    print(f"Error al crear la tabla 'registro_nomina': {e}")
