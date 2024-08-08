from sqlalchemy import Table, Column, Integer, ForeignKey, Date, Numeric
from config.db import meta

factura = Table(
    'facturas',
    meta,
    Column('id_factura', Integer, primary_key=True),
    Column('id_contrato', Integer, ForeignKey('contratos.id')),  # Cambiar a id_contrato
    Column('id_periodo', Integer, ForeignKey('periodo_facturacion.id_periodo')),
    Column('monto_total', Numeric(12, 2)),
    Column('fecha_emision', Date),
)
