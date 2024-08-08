# schemas/factura.py
from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

class Factura(BaseModel):
    id_factura: Optional[int] = None
    id_empleado: int
    id_periodo: int
    monto_total: Decimal
    fecha_emision: date

    class Config:
        from_attributes = True

class FacturaCreate(BaseModel):
    id_empleado: int
    id_periodo: int
    monto_total: Decimal
    fecha_emision: date

    class Config:
        from_attributes = True

class FacturaUpdate(BaseModel):
    monto_total: Optional[Decimal] = None
    fecha_emision: Optional[date] = None

    class Config:
        from_attributes = True
