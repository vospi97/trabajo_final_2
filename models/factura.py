# models/factura.py
from sqlalchemy import Table, Column, Integer, ForeignKey, Date, Numeric
from config.db import meta
factura = Table(
    'factura',
    meta,
    Column('id_factura', Integer, primary_key=True),
    Column('id_empleado', Integer, ForeignKey('empleado.id_empleado')),
    Column('id_periodo', Integer, ForeignKey('periodo_facturacion.id_periodo')),
    Column('monto_total', Numeric(12, 2)),
    Column('fecha_emision', Date),
)
