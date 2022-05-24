from datetime import date, time
from pydantic import BaseModel, Field
from typing import Union

class PacienteBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    apaterno: Union[str, None] = None
    amaterno: Union[str, None] = None
    edad : Union[int, None] = Field(..., gt=0)
    peso : Union[float, None] = Field(..., gt=0)
    telefono : Union[str, None] = Field(..., max_length=10)
    email : Union[str, None] = None

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int

    class Config:
        orm_mode = True

class CitaBase(BaseModel):
    fecha : Union[date, None] = None
    hora : Union[time, None] = None

class CitaCreate(CitaBase):
    id_paciente: int
    pass

class Cita(CitaBase):
    id: int
    paciente: Paciente


    class Config:
        orm_mode = True
