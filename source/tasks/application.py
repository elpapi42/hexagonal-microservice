from source.tasks.domain.entities import Task
from source.tasks.domain.repositories import TaskRepository

async def create_task(task:Task, repo:TaskRepository):
    task = await repo.save(task)
    return task
