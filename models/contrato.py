from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.types import DECIMAL
from config.db import meta, engine, conn

# Definición de la tabla 'contratos'
contratos = Table(
    'contratos', meta,
    Column('id_contrato', Integer, primary_key=True, autoincrement=True),  # ID único con autoincremento
    Column('id_empleado', Integer, ForeignKey('empleados.id_empleado'), nullable=False),  # Clave foránea, no nula
    Column('id_departamento', Integer, ForeignKey('departamentos.id_departamento'), nullable=True),  # Clave foránea, puede ser nula
    Column('fecha_inicio', Date, nullable=True),  # Fecha de inicio del contrato, puede ser nula
    Column('fecha_fin', Date, nullable=True),  # Fecha de fin del contrato, puede ser nula
    Column('tipo_contrato', String(50), nullable=True),  # Tipo de contrato, puede ser nulo
    Column('cargo', String(100), nullable=True),  # Cargo del empleado, puede ser nulo
    Column('salario_base', DECIMAL(10, 2), nullable=True),  # Salario base, puede ser nulo
    Column('email_empresarial', String(100), nullable=True),  # Correo electrónico empresarial, puede ser nulo
    Column('fecha_desvinculacion', Date, nullable=True),  # Fecha de desvinculación, puede ser nula
    Column('eps', String(100), nullable=True),  # EPS, puede ser nula
    Column('arl', String(100), nullable=True),  # ARL, puede ser nula
    Column('pensiones', String(100), nullable=True)  # Fondo de pensiones, puede ser nulo
)

# Creación de la tabla en la base de datos
try:
    meta.create_all(engine)
except Exception as e:
    print(f"Error al crear la tabla 'contratos': {e}")
