from typing import Annotated
from pydantic import Field, PositiveFloat

from api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="Fulano", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="00000000000", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=97.5)]
    altura: Annotated[PositiveFloat, Field(description="altura do atleta", example=180.5)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M,F", max_length=1)]
