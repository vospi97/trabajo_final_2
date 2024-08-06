from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

# Esquema para la creación de un nuevo contrato
class Contrato(BaseModel):
    id_empleado: Optional[int] = None  # ID del empleado asociado al contrato (opcional)
    id_departamento: Optional[int] = None  # ID del departamento asociado al contrato (opcional)
    fecha_inicio: Optional[date] = None  # Fecha de inicio del contrato (opcional)
    fecha_fin: Optional[date] = None  # Fecha de fin del contrato (opcional)
    tipo_contrato: Optional[str] = None  # Tipo de contrato (opcional)
    cargo: Optional[str] = None  # Cargo del empleado (opcional)
    salario_base: Optional[Decimal] = None  # Salario base del contrato (opcional)
    email_empresarial: Optional[str] = None  # Correo empresarial (opcional)
    fecha_desvinculacion: Optional[date] = None  # Fecha de desvinculación (opcional)
    eps: Optional[str] = None  # EPS del empleado (opcional)
    arl: Optional[str] = None  # ARL del empleado (opcional)
    pensiones: Optional[str] = None  # Fondo de pensiones del empleado (opcional)

    class Config:
        orm_mode = True  # Habilita la compatibilidad con ORMs

# Esquema para la actualización de un contrato existente
class ContratoUpdate(BaseModel):
    id_departamento: Optional[int] = None  # ID del departamento asociado al contrato (opcional)
    fecha_inicio: Optional[date] = None  # Fecha de inicio del contrato (opcional)
    fecha_fin: Optional[date] = None  # Fecha de fin del contrato (opcional)
    tipo_contrato: Optional[str] = None  # Tipo de contrato (opcional)
    cargo: Optional[str] = None  # Cargo del empleado (opcional)
    salario_base: Optional[Decimal] = None  # Salario base del contrato (opcional)
    email_empresarial: Optional[str] = None  # Correo empresarial (opcional)
    fecha_desvinculacion: Optional[date] = None  # Fecha de desvinculación (opcional)
    eps: Optional[str] = None  # EPS del empleado (opcional)
    arl: Optional[str] = None  # ARL del empleado (opcional)
    pensiones: Optional[str] = None  # Fondo de pensiones del empleado (opcional)

    class Config:
        orm_mode = True  # Habilita la compatibilidad con ORMs



