from fastapi import APIRouter

from source.tasks.domain.entities import TaskId


router = APIRouter()

@router.post('/')
async def create_task():
    print(TaskId(value='605bf2d687d5cbb60108bde1'))
    return {'test': 'hola'}
