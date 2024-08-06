from fastapi import FastAPI, APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from config.db import conn
from models.empleado import empleados as empleados_model
from schemas.empleado import Empleado, EmpleadoUpdate

# Crear instancia de APIRouter
empleados = APIRouter()

# Endpoint para obtener todos los empleados
@empleados.get("/empleados")
def get_empleados():
    """
    Retorna la lista de todos los empleados.

    Returns:
        list: Lista de empleados.
    """
    try:
        result = conn.execute(empleados_model.select()).fetchall()
        empleados_list = [dict(row._mapping) for row in result]
        return empleados_list
    except SQLAlchemyError as e:
        print(f"Error al obtener empleados: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener empleados")

# Endpoint para crear un nuevo empleado
@empleados.post("/empleados")
def nuevo_empleado(empleado: Empleado):
    """
    Crea un nuevo empleado en la base de datos.

    Args:
        empleado (Empleado): Objeto empleado con los datos a insertar.

    Returns:
        dict: Mensaje de éxito y ID del empleado creado.
    """
    new_empleado = {
        "nombres": empleado.nombres,
        "apellidos": empleado.apellidos,
        "cc": empleado.cc,
        "fecha_nacimiento": empleado.fecha_nacimiento,
        "direccion": empleado.direccion,
        "telefono": empleado.telefono,
        "email": empleado.email,
        "tipo_sangre": empleado.tipo_sangre
    }

    try:
        result = conn.execute(empleados_model.insert().values(new_empleado))
        conn.commit()  # Confirmar la transacción
        return {"message": "Empleado creado exitosamente", "id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        conn.rollback()  # Deshacer la transacción en caso de error
        print(f"Error al crear el empleado: {e}")
        raise HTTPException(status_code=400, detail="Error al crear el empleado")

# Endpoint para actualizar un empleado existente
@empleados.put("/empleados/{cc}")
def actualizar_empleado(cc: str, empleado_update: EmpleadoUpdate):
    """
    Actualiza los datos de un empleado existente.

    Args:
        cc (str): Número de cédula del empleado a actualizar.
        empleado_update (EmpleadoUpdate): Objeto con los datos a actualizar.

    Returns:
        dict: Mensaje de éxito.
    """
    try:
        # Buscar al empleado por su número de cédula
        empleado = conn.execute(empleados_model.select().where(empleados_model.c.cc == cc)).first()
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")

        # Crear un diccionario de los campos a actualizar
        update_data = empleado_update.dict(exclude_unset=True)

        # Actualizar los datos en la base de datos
        conn.execute(
            empleados_model.update()
            .where(empleados_model.c.cc == cc)
            .values(**update_data)
        )
        conn.commit()
        return {"message": "Empleado actualizado exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al actualizar el empleado: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar el empleado")

# Endpoint para eliminar un empleado
@empleados.delete("/empleados/{cc}")
def eliminar_empleado(cc: str):
    """
    Elimina un empleado de la base de datos.

    Args:
        cc (str): Número de cédula del empleado a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        # Buscar al empleado por su número de cédula
        empleado = conn.execute(empleados_model.select().where(empleados_model.c.cc == cc)).first()
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")

        # Eliminar el empleado de la base de datos
        conn.execute(empleados_model.delete().where(empleados_model.c.cc == cc))
        conn.commit()
        return {"message": "Empleado eliminado exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al eliminar el empleado: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar el empleado")
