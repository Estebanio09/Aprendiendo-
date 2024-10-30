# API: Interfaz de programación de aplicaciones, conjunto de reglas para que los programas se puedan comunicar
# REST: para transferir la información o recursos
from typing import List, Optional
import uuid
import fastapi
from pydantic import BaseModel


app = fastapi.FastAPI()


class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int


# simular base de datos
cursos_db = []


# CRUD: Read (lectura) GET ALL: Leeremos todos los cursos que estén en la db
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return cursos_db


## CRUD: Create (escribir) POST: agregaremos un nuevo curso a nuestra base de datos
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())  # usamos uuid para crear un id único
    cursos_db.append(curso)
    return curso


# CRUD: Read (lectura) GET (individual): Leeremos el curso que coincida con el ID que pidamos
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # con NEXT tomamos la primera coincidencia de la lista devuelta
    if curso is None:
        raise fastapi.HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


# CRUD: update (Actualizar/Modificar) PUT: Modificaremos un recuso que coincida con el ID que mandemos
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado:Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise fastapi.HTTPException(status_code=404, detail="Curso no encontrado")
    curso_actualizado.id = curso_id
    _index = cursos_db.index(curso) # Buscamos el índice exacto donde está el curso en nuestra lista 
    cursos_db[_index] = curso_actualizado
    return curso_actualizado

# CRUD: Delete (borrado/baja) DELETE: Eliminaremos un recurso que coincida con el ID que mandemos 

@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str,):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise fastapi.HTTPException(status_code=404, detail="Curso no encontrado")
    cursos_db.remove(curso)
    return curso 