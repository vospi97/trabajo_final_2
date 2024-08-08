from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from config.db import conn
from models.factura import factura as factura_model
from schemas.factura import FacturaCreate, FacturaUpdate
from datetime import date
from decimal import Decimal
from sqlalchemy import text

factura_router = APIRouter()

def calcular_monto_total(id_contrato: int, id_periodo: int) -> Decimal:
    try:
        query = text(
            "SELECT salario_base FROM contratos WHERE id_contrato = :id_contrato"
        )
        result = conn.execute(query, {"id_contrato": id_contrato}).fetchone()

        salario_base = result[0]  # Accede al valor de la primera columna del resultado
        return Decimal(salario_base)
    except SQLAlchemyError as e:
        print(f"Error al calcular el monto total: {e}")
        raise HTTPException(status_code=500, detail="Error al calcular el monto total")

@factura_router.post("/generar_facturas")
def generar_facturas(id_periodo: int):
    try:
        query = text("SELECT id_contrato FROM contratos WHERE id_contrato IS NOT NULL")
        contratos = conn.execute(query).fetchall()
        
        for contrato in contratos:
            id_contrato = contrato[0]  # Accede al primer elemento de la tupla
            monto_total = calcular_monto_total(id_contrato, id_periodo)
            fecha_emision = date.today()
            
            conn.execute(
                factura_model.insert().values(
                    id_contrato=id_contrato,
                    id_periodo=id_periodo,
                    monto_total=monto_total/2,
                    fecha_emision=fecha_emision
                )
            )
        
        conn.commit()
        return {"message": "Facturas generadas exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al generar facturas: {e}")
        raise HTTPException(status_code=500, detail="Error al generar facturas")
