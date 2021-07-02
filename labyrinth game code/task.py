class Task:
    def __init__(self, task, answer):
        self.task = task
        self.answer = answer

    def get_task(self):
        return "Your task is: {}".format(self.task)

    def get_answer(self):
        return "The correct answer is: {}".format(self.answer)
