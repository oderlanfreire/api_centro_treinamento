from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", examples="Fulano", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", examples="00000000000", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=97.5)]
    altura: Annotated[PositiveFloat, Field(description="altura do atleta", examples=180.5)]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples="M,F", max_length=1)]
