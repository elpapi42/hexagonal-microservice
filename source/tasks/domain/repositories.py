from source.tasks.domain.entities import Task, TaskId


class TaskRepository():
    async def save(self, task:Task) -> Task:
        raise NotImplementedError()
    
    async def fetch(self, id:TaskId) -> Task:
        raise NotImplementedError()
