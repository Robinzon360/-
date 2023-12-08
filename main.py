class Entity():
    def __init__(self, cat):
        self.cat = cat

    def __str__(self):
        return f'Сущность: {self.cat}'


class Employee():
    def __init__(self, employee: list[str]):
        self.employee = employee[0]
        self.company = employee[1]

    def __str__(self):
        return f'{self.employee} работает в {self.company}'


if __name__ == '__main__':
    cat = Entity('Сугроб')
    print(cat)

    employee = Employee(['Петя', 'Foxford'])
    print(employee)
