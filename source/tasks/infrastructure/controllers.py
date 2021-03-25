from fastapi import APIRouter

from source.tasks.domain.entities import TaskId, Task


router = APIRouter()

@router.post('/')
async def create_task():
    print(Task(title='Hola Mundo'))
    return {'test': 'hola'}
