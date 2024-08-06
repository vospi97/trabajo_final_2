from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from config.db import conn
from models.registro_nomina import registro_nomina as registro_nomina_model
from schemas.registro_nomina import RegistroNomina, RegistroNominaUpdate

# Crear instancia de APIRouter
registro_nomina = APIRouter()

# Endpoint para obtener todos los registros de nómina
@registro_nomina.get("/registro_nomina")
def get_registro_nomina():
    """
    Retorna la lista de todos los registros de nómina.

    Returns:
        list: Lista de registros de nómina.
    """
    try:
        result = conn.execute(registro_nomina_model.select()).fetchall()
        registros_list = [dict(row._mapping) for row in result]
        return registros_list
    except SQLAlchemyError as e:
        print(f"Error al obtener registros de nómina: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener registros de nómina")

# Endpoint para crear un nuevo registro de nómina
@registro_nomina.post("/registro_nomina")
def nuevo_registro_nomina(registro: RegistroNomina):
    """
    Crea un nuevo registro de nómina en la base de datos.

    Args:
        registro (RegistroNomina): Objeto registro con los datos a insertar.

    Returns:
        dict: Mensaje de éxito y ID del registro creado.
    """
    new_registro = {
        "id_contrato": registro.id_contrato,
        "fecha_pago": registro.fecha_pago,
        "salario_base": registro.salario_base,
        "deducciones": registro.deducciones,
        "salario_neto": registro.salario_neto,
        "id_periodo": registro.id_periodo
    }

    try:
        result = conn.execute(registro_nomina_model.insert().values(new_registro))
        conn.commit()  # Confirmar la transacción
        return {"message": "Registro de nómina creado exitosamente", "id": result.inserted_primary_key[0]}
    except SQLAlchemyError as e:
        conn.rollback()  # Deshacer la transacción en caso de error
        print(f"Error al crear el registro de nómina: {e}")
        raise HTTPException(status_code=400, detail="Error al crear el registro de nómina")

# Endpoint para actualizar un registro de nómina existente
@registro_nomina.put("/registro_nomina/{id_nomina}")
def actualizar_registro_nomina(id_nomina: int, registro_update: RegistroNominaUpdate):
    """
    Actualiza los datos de un registro de nómina existente.

    Args:
        id_nomina (int): ID del registro de nómina a actualizar.
        registro_update (RegistroNominaUpdate): Objeto con los datos a actualizar.

    Returns:
        dict: Mensaje de éxito.
    """
    try:
        # Buscar el registro de nómina por su ID
        registro = conn.execute(registro_nomina_model.select().where(registro_nomina_model.c.id_nomina == id_nomina)).first()
        if not registro:
            raise HTTPException(status_code=404, detail="Registro de nómina no encontrado")

        # Crear un diccionario de los campos a actualizar
        update_data = registro_update.dict(exclude_unset=True)

        # Actualizar los datos en la base de datos
        conn.execute(
            registro_nomina_model.update()
            .where(registro_nomina_model.c.id_nomina == id_nomina)
            .values(**update_data)
        )
        conn.commit()
        return {"message": "Registro de nómina actualizado exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al actualizar el registro de nómina: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar el registro de nómina")

# Endpoint para eliminar un registro de nómina
@registro_nomina.delete("/registro_nomina/{id_nomina}")
def eliminar_registro_nomina(id_nomina: int):
    """
    Elimina un registro de nómina de la base de datos.

    Args:
        id_nomina (int): ID del registro de nómina a eliminar.

    Returns:
        dict: Mensaje de éxito o error.
    """
    try:
        # Buscar el registro de nómina por su ID
        registro = conn.execute(registro_nomina_model.select().where(registro_nomina_model.c.id_nomina == id_nomina)).first()
        if not registro:
            raise HTTPException(status_code=404, detail="Registro de nómina no encontrado")

        # Eliminar el registro de nómina de la base de datos
        conn.execute(registro_nomina_model.delete().where(registro_nomina_model.c.id_nomina == id_nomina))
        conn.commit()
        return {"message": "Registro de nómina eliminado exitosamente"}
    except SQLAlchemyError as e:
        conn.rollback()
        print(f"Error al eliminar el registro de nómina: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar el registro de nómina")
