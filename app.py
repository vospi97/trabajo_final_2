from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future import select
from config.db import engine

# Importar tablas desde los modelos
from models.empleado import empleados
from models.contrato import contratos
from models.departamento import departamentos
from models.evaluacion_desempeno import evaluacion_desempeno
from models.periodo_facturacion import periodo_facturacion
from models.registro_asistencia import registro_asistencia
from models.registro_nomina import registro_nomina

# Crear instancia de FastAPI
app = FastAPI()

# Configurar Jinja2Templates para buscar en la carpeta "templates" del directorio raíz
templates = Jinja2Templates(directory="templates")

# Configurar StaticFiles para servir archivos estáticos desde la carpeta "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir routers con prefijos y tags para mejor organización

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ruta de inicio
@app.get("/", tags=["Home"], response_class=HTMLResponse)
async def read_root():
    """
    Retorna la página de inicio en formato HTML.

    Returns:
        HTMLResponse: Página de inicio.
    """
    return FileResponse("templates/index.html")

# Ruta para obtener empleados y renderizar HTML
@app.get("/empleados", response_class=HTMLResponse)
async def get_empleados(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de empleados en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de empleados.
    """
    query = select(empleados)
    result = db.execute(query)
    empleados_data = result.fetchall()
    return templates.TemplateResponse("empleados.html", {"request": request, "empleados": empleados_data})

# Ruta para obtener contratos y renderizar HTML
@app.get("/contratos", response_class=HTMLResponse)
async def get_contratos(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de contratos en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de contratos.
    """
    query = select(contratos)
    result = db.execute(query)
    contratos_data = result.fetchall()
    return templates.TemplateResponse("contratos.html", {"request": request, "contratos": contratos_data})

# Ruta para obtener departamentos y renderizar HTML
@app.get("/departamentos", response_class=HTMLResponse)
async def get_departamentos(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de departamentos en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de departamentos.
    """
    query = select(departamentos)
    result = db.execute(query)
    departamentos_data = result.fetchall()
    return templates.TemplateResponse("departamentos.html", {"request": request, "departamentos": departamentos_data})

# Ruta para obtener evaluación de desempeño y renderizar HTML
@app.get("/evaluacion-desempeno", response_class=HTMLResponse)
async def get_evaluacion_desempeno(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de evaluaciones de desempeño en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de evaluaciones de desempeño.
    """
    query = select(evaluacion_desempeno)
    result = db.execute(query)
    evaluacion_desempeno_data = result.fetchall()
    return templates.TemplateResponse("evaluacion_desempeno.html", {"request": request, "evaluacion_desempeno": evaluacion_desempeno_data})

# Ruta para obtener periodo de facturación y renderizar HTML
@app.get("/periodo-facturacion", response_class=HTMLResponse)
async def get_periodo_facturacion(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de periodos de facturación en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de periodos de facturación.
    """
    query = select(periodo_facturacion)
    result = db.execute(query)
    periodo_facturacion_data = result.fetchall()
    return templates.TemplateResponse("periodo_facturacion.html", {"request": request, "periodo_facturacion": periodo_facturacion_data})

# Ruta para obtener registro de asistencia y renderizar HTML
@app.get("/registro-asistencia", response_class=HTMLResponse)
async def get_registro_asistencia(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de registros de asistencia en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de registros de asistencia.
    """
    query = select(registro_asistencia)
    result = db.execute(query)
    registro_asistencia_data = result.fetchall()
    return templates.TemplateResponse("registro_asistencia.html", {"request": request, "registro_asistencia": registro_asistencia_data})

# Ruta para obtener registro de nómina y renderizar HTML
@app.get("/registro-nomina", response_class=HTMLResponse)
async def get_registro_nomina(request: Request, db: Session = Depends(lambda: SessionLocal())):
    """
    Retorna una lista de registros de nómina en formato HTML.

    Args:
        request: El objeto Request de FastAPI.
        db: La sesión de base de datos.
    
    Returns:
        HTMLResponse: Respuesta HTML que muestra la lista de registros de nómina.
    """
    query = select(registro_nomina)
    result = db.execute(query)
    registro_nomina_data = result.fetchall()
    return templates.TemplateResponse("registro_nomina.html", {"request": request, "registro_nomina": registro_nomina_data})
