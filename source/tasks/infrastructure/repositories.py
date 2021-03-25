from source.tasks.domain.entities import Task, TaskId
from source.tasks.domain.repositories import TaskRepository


class FakeTaskRepository(TaskRepository):
    """Useful for testing and mocking."""
    async def save(self, task:Task) -> Task:
        return task
    
    async def fetch(self, id:TaskId) -> Task:
        return Task(id=id, title='Hola Mundo from Repo')
