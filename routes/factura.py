from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from config.db import conn
from models.factura import factura as factura_model
from schemas.factura import FacturaCreate, FacturaUpdate
from datetime import date
from decimal import Decimal
from sqlalchemy import text

factura_router = APIRouter()

def calcular_monto_total(id_empleado: int, id_periodo: int) -> Decimal:
    try:
        query = text(
            "SELECT salario_neto FROM registro_nomina WHERE id_contrato = "
            "(SELECT id_contrato FROM public.contratos WHERE id_empleado = :id_empleado) AND id_periodo = :id_periodo"
        )
        result = conn.execute(query, {"id_empleado": id_empleado, "id_periodo": id_periodo}).fetchall()

        monto_total = sum(row['salario_neto'] for row in result)
        return Decimal(monto_total)
    except SQLAlchemyError as e:
        print(f"Error al calcular el monto total: {e}")
        raise HTTPException(status_code=500, detail="Error al calcular el monto total")

@factura_router.post("/generar_facturas")
def generar_facturas(id_periodo: int):
    try:
        query = text("SELECT id_empleado FROM public.contratos WHERE id_empleado IS NOT NULL")
        empleados = conn.execute(query).fetchall()
        
        for empleado in empleados:
            id_empleado = empleado[0]  # Accede al primer elemento de la tupla
            monto_total = calcular_monto_total(id_empleado, id_periodo)
            fecha_emision = date.today()
            
            conn.execute(
                factura_model.insert().values(
                    id_empleado=id_empleado,
                    id_periodo=id_periodo,
                    monto_total=monto_total,
                    fecha_emision=fecha_emision
                )
            )
        
        conn.commit()
        return {"message": "Facturas generadas exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al generar facturas: {e}")
        raise HTTPException(status_code=500, detail="Error al generar facturas")
