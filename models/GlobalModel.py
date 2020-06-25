from pydantic import BaseModel


class GlobalResult(BaseModel):
    message: str
