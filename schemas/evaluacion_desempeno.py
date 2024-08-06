from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

# Esquema para la creación de una nueva evaluación de desempeño
class EvaluacionDesempeno(BaseModel):
    id_empleado: int  # ID del empleado, campo obligatorio
    id_periodo: int  # ID del periodo de facturación, campo obligatorio
    calificacion: Optional[Decimal] = None  # Calificación del desempeño, campo opcional

    class Config:
        orm_mode = True  # Habilita la compatibilidad con ORMs

# Esquema para la actualización de una evaluación de desempeño existente
class EvaluacionDesempenoUpdate(BaseModel):
    id_empleado: Optional[int] = None  # ID del empleado, campo opcional
    id_periodo: Optional[int] = None  # ID del periodo de facturación, campo opcional
    calificacion: Optional[Decimal] = None  # Calificación del desempeño, campo opcional

    class Config:
        orm_mode = True  # Habilita la compatibilidad con ORMs
