from fastapi import APIRouter

from source.tasks.domain.entities import TaskId, Task
from source.tasks.application import create_task


router = APIRouter()

@router.post('/')
async def create_task_controller():
    task = await create_task(Task(title='Hola Mundo'))
    return task
