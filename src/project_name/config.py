from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Segredos e paths de ambiente — lidos de variáveis de ambiente/.env."""

    database_url: str = ""
    data_dir: Path = Path("data")

    class Config:
        env_file = ".env"


class TrainConfig(BaseModel):
    """Configuração de um run de treino — carregada de configs/*.yaml."""

    learning_rate: float
    epochs: int
    seed: int = 42
