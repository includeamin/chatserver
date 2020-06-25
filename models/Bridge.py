from fastapi import HTTPException
from pydantic import BaseModel, validator
from typing import List


class PersonalInfo(BaseModel):
    phone_number: str
    name: str
