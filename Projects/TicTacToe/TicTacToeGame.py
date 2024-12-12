import random


class TicTacToeGame:
    def __init__(self, size: int = 0, rule: int = 0):
        while rule > size or size < 3 or rule < 3:
            size = int(input('Неверно заданы размеры и правила, введите размер поля: '))
            rule = int(input('Введите правило победы: '))
        self.size = size
        self.rule = rule
        self.points = ['\u00B7' for _ in range(self.size * self.size)]
        if random.randint(1, 2) == 1:
            self.side_flag = 'X'
        else:
            self.side_flag = 'O'
        self._start()

    def show(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(self.points[i * self.size + j], end=' ')
            print()

    def _get_point(self, x: int, y: int) -> str:
        return self.points[y * self.size + x]

    def _check_from_point(self, x: int, y: int) -> bool:
        def count_in_direction(dx: int, dy: int) -> int:
            count = 0
            nx, ny = x, y
            while 0 <= nx < self.size and 0 <= ny < self.size and self._get_point(nx, ny) == self.side_flag:
                count += 1
                nx += dx
                ny += dy
            return count - 1  # Потому что первая точка, которая будет посчитана это точка старта

        horizontal = 1 + count_in_direction(1, 0) + count_in_direction(-1, 0)
        if horizontal >= self.rule:
            return True

        vertical = 1 + count_in_direction(0, 1) + count_in_direction(0, -1)
        if vertical >= self.rule:
            return True

        diagonal_lr = 1 + count_in_direction(1, 1) + count_in_direction(-1, -1)
        if diagonal_lr >= self.rule:
            return True

        diagonal_rl = 1 + count_in_direction(-1, 1) + count_in_direction(1, -1)
        if diagonal_rl >= self.rule:
            return True

        return False

    def _start(self) -> None:
        for _ in range(self.size * self.size):
            self.show()
            print(f"Ход '{self.side_flag}': Введите координату хода: ")
            x, y = map(lambda n: int(n) - 1, input().split())
            while x < 0 or y < 0 or x > self.size - 1 or y > self.size - 1 or self.points[
                y * self.size + x] != '\u00B7':
                print(f"Ход '{self.side_flag}': Неверная координата: ")
                x, y = map(lambda n: int(n) - 1, input().split())
            self.points[y * self.size + x] = self.side_flag
            if self._check_from_point(x, y):
                print(f"'{self.side_flag}' ПОБЕДИЛ")
                break
            if self.side_flag == 'X':
                self.side_flag = 'O'
            else:
                self.side_flag = 'X'
