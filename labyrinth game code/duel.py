from random import randint


class Duel:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.task = self.player.labyrinth.tasks[randint(0, len(self.player.labyrinth.tasks)-1)]
        self.winner = None
        self.loser = None

    def ask_question(self):
        return self.monster.introduce_yourself() + self.task.get_task()

    def check_answer(self, answer):
        if answer == self.task.answer:
            self.winner = self.player
            self.loser = self.monster
            return "Your answer is correct."
        else:
            self.loser = self.player
            self.winner = self.monster
            return "You are loser! \n" + self.task.get_answer()

    def give_prize(self):
        player_lvl = self.player.level
        if self.winner == self.player:
            self.player.level += self.monster.level
            self.player.current_chamber.monster = None
        else:
            if self.player.level - self.monster.level > 0:
                self.player.level -= self.monster.level
                self.monster.level += self.player.level
            else:
                self.player.level = 1
                self.monster.level += self.player.level
        return "{} your level was changed: {} -> {} \n".format(self.player.name, player_lvl, self.player.level)