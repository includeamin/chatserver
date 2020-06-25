from pydantic import BaseModel


class PaginationModel(BaseModel):
    limit: int
    skip: int
