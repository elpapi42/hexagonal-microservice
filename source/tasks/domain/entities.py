from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId


def generate_objectid():
    """Returns ObjectId as str."""
    return str(ObjectId())

class TaskId(BaseModel):
    """
    Id of a Task.

    Despites the TaskId value represents an ObjectId,
    we will threat it in our domain as an string.
    It will be parsed to ObjectId on the repos.
    We will check the supplied string is valid.
    """
    value:str = Field(default_factory=generate_objectid)

    @validator('value')
    def valid_objectid(cls, v):
        try:
            ObjectId(v)
        except:
            raise ValueError('Invalid ObjectId. Supplied str must complain with ObjectId Standard')

        return v

class TaskStatus(str, Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

class Task(BaseModel):
    id:TaskId
    title:str
    description:Optional[str] = ''
    status:TaskStatus = TaskStatus.PENDING
