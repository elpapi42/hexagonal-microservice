from source.tasks.domain.entities import Task, TaskId


class TaskRepository():
    async def save(self, task:Task) -> Task:
        raise NotImplementedError('Implement save in TaskRepository child')

    async def fetch(self, id:TaskId) -> Task:
        raise NotImplementedError('Implement fetch in TaskRepository child')
