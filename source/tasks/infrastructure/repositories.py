from bson.objectid import ObjectId

from source.tasks.domain.entities import Task, TaskId
from source.tasks.domain.repositories import TaskRepository
from source.mongo import db
from source.loggers import default_logger


class FakeTaskRepository(TaskRepository):
    """Useful for testing and mocking."""

    async def save(self, task:Task) -> Task:
        return task
    
    async def fetch(self, id:TaskId) -> Task:
        return Task(id=id, title='Hola Mundo from Repo')

class MongoTaskRepository(TaskRepository):
    """Operates over a MongoDB instance."""

    async def save(self, task:Task) -> Task:
        task_dict = task.dict()
        task_dict['_id'] = ObjectId(task.id.value)
        task_dict.pop('id')

        result = await db.tasks.insert_one(task_dict)

        assert str(result.inserted_id) == task.id.value

        default_logger.info(f'Task "{task.id.value}" created')

        return task
    
    async def fetch(self, id:TaskId) -> Task:
        return Task(id=id, title='Hola Mundo from Repo')
