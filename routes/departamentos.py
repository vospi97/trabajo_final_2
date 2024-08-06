from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from config.db import conn
from models.departamento import departamentos as departamentos_model
from models.empleado import empleados as empleados_model  # Importar modelo de empleados
from schemas.departamento import Departamento, DepartamentoUpdate

# Crear instancia de APIRouter
departamentos = APIRouter()

# Endpoint para obtener todos los departamentos
@departamentos.get("/departamentos")
def get_departamentos():
    """
    Retorna la lista de todos los departamentos.

    Returns:
        list: Lista de departamentos.
    """
    try:
        result = conn.execute(departamentos_model.select()).fetchall()
        departamentos_list = [dict(row._mapping) for row in result]
        return departamentos_list
    except SQLAlchemyError as e:
        print(f"Error al obtener departamentos: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener departamentos")

# Endpoint para crear un nuevo departamento
@departamentos.post("/departamentos")
def crear_departamento(departamento: Departamento):
    """
    Crea un nuevo departamento en la base de datos.

    Args:
        departamento (Departamento): Objeto departamento con los datos a insertar.

    Returns:
        dict: Mensaje de éxito y ID del departamento creado.
    """
    try:
        new_departamento = departamento.dict(exclude_unset=True)
        result = conn.execute(departamentos_model.insert().values(new_departamento))
        conn.commit()  # Confirmar la transacción
        return {"message": "Departamento creado exitosamente", "id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        conn.rollback()  # Deshacer la transacción en caso de error
        print(f"Error al crear el departamento: {e}")
        raise HTTPException(status_code=400, detail="Error al crear el departamento")

# Endpoint para actualizar un departamento existente
@departamentos.put("/departamentos/{id_departamento}")
def actualizar_departamento(id_departamento: int, departamento_update: DepartamentoUpdate):
    """
    Actualiza los datos de un departamento existente.

    Args:
        id_departamento (int): ID del departamento a actualizar.
        departamento_update (DepartamentoUpdate): Objeto con los datos a actualizar.

    Returns:
        dict: Mensaje de éxito.
    """
    try:
        # Buscar el departamento por su ID
        dept = conn.execute(departamentos_model.select().where(departamentos_model.c.id_departamento == id_departamento)).first()
        if not dept:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")

        # Crear un diccionario de los campos a actualizar
        update_data = departamento_update.dict(exclude_unset=True)

        # Actualizar los datos en la base de datos
        conn.execute(
            departamentos_model.update()
            .where(departamentos_model.c.id_departamento == id_departamento)
            .values(**update_data)
        )
        conn.commit()
        return {"message": "Departamento actualizado exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al actualizar el departamento: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar el departamento")

# Endpoint para eliminar un departamento
@departamentos.delete("/departamentos/{id_departamento}")
def eliminar_departamento(id_departamento: int):
    """
    Elimina un departamento de la base de datos.

    Args:
        id_departamento (int): ID del departamento a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        # Buscar el departamento por su ID
        dept = conn.execute(departamentos_model.select().where(departamentos_model.c.id_departamento == id_departamento)).first()
        if not dept:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")

        # Eliminar el departamento de la base de datos
        conn.execute(departamentos_model.delete().where(departamentos_model.c.id_departamento == id_departamento))
        conn.commit()
        return {"message": "Departamento eliminado exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al eliminar el departamento: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar el departamento")

# Endpoint para asignar un gerente a un departamento
@departamentos.put("/departamentos/{id_departamento}/asignar_gerente")
def asignar_gerente(id_departamento: int, cc: str):
    """
    Asigna un gerente a un departamento usando la cédula del empleado.

    Args:
        id_departamento (int): ID del departamento.
        cc (str): Cédula del empleado a asignar como gerente.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        # Buscar el departamento por su ID
        dept = conn.execute(departamentos_model.select().where(departamentos_model.c.id_departamento == id_departamento)).first()
        if not dept:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")

        # Buscar el empleado por su número de cédula
        empleado = conn.execute(empleados_model.select().where(empleados_model.c.cc == cc)).first()
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")

        # Asignar el id_empleado al campo id_gerente del departamento
        conn.execute(
            departamentos_model.update()
            .where(departamentos_model.c.id_departamento == id_departamento)
            .values(id_gerente=empleado.id_empleado)
        )
        conn.commit()
        return {"message": "Gerente asignado exitosamente al departamento"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al asignar gerente: {e}")
        raise HTTPException(status_code=500, detail="Error al asignar gerente")
