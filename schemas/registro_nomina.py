from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

# Esquema para la creación de un nuevo registro de nómina
class RegistroNomina(BaseModel):
    id_nomina: Optional[int] = None  # ID de la nómina, generado automáticamente
    id_contrato: int  # ID del contrato asociado, campo obligatorio
    fecha_pago: Optional[date] = None  # Fecha de pago, campo opcional
    salario_base: Optional[Decimal] = None  # Salario base, campo opcional
    deducciones: Optional[Decimal] = None  # Deducciones, campo opcional
    salario_neto: Optional[Decimal] = None  # Salario neto, campo opcional
    id_periodo: Optional[int] = None  # ID del periodo de facturación, campo opcional

    class Config:
        orm_mode = True  # Habilita la compatibilidad con ORMs

# Esquema para la actualización de un registro de nómina existente
class RegistroNominaUpdate(BaseModel):
    id_contrato: Optional[int] = None  # ID del contrato asociado, campo opcional
    fecha_pago: Optional[date] = None  # Fecha de pago, campo opcional
    salario_base: Optional[Decimal] = None  # Salario base, campo opcional
    deducciones: Optional[Decimal] = None  # Deducciones, campo opcional
    salario_neto: Optional[Decimal] = None  # Salario neto, campo opcional
    id_periodo: Optional[int] = None  # ID del periodo de facturación, campo opcional

    class Config:
        orm_mode = True  # Habilita la compatibilidad con ORMs
