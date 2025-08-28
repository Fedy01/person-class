import random


class Student:
    university = 'BGU'
    all_ids = []

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.__person_id = None

    def get_info(self):
        return f'{self.name}, {self.lastname}, {self.age}'

    def set_last_name(self, other_last_name):
        self.lastname = other_last_name

    def set_atr(self, atr_name, atr_new_val):
        if atr_name == 'name':
            self.name = atr_new_val
        elif atr_name == 'lastname':
            self.lastname = atr_new_val
        elif atr_name == 'age':
            self.age = atr_new_val
        else:
            return 'нет такого атрибута'
        return 'все изменилось'

    def set_get_say_hi(self):
        return f'hi, my name is {self.name}'

    def get_random_id(self):
        while True:
            random_id = random.randint(1, 1000000)
            if random_id not in Student.all_ids:
                self.__person_id = random_id
                Student.all_ids.append(random_id)
                return self.__person_id

    def get_id(self):
        return self.__person_id


class Person(Student):
    def __init__(self, name, lastname, age, points=0, spec=None):
        super().__init__(name, lastname, age)
        self.points = points
        self.spec = spec

    def get_info(self):
        return (f'Name: {self.name} {self.lastname}, '
                f'Age: {self.age}, '
                f'Specialty: {self.spec}, '
                f'Points: {self.points}')

    def say_hi(self):
        return f'Hi, my name is {self.name}!'

    def set_points(self, points):
        self.points = points

    def set_spec(self, specialize):
        self.spec = specialize
        return self.spec

    def is_successful(self):
        return self.points > 74

    def _getFullName(self):
        return f'{self.name} {self.lastname}'


class Employee(Person):
    def __init__(self, name, lastname, age, position, salary, work_experience, points=0, spec=None):
        super().__init__(name, lastname, age, points, spec)
        self.position = position
        self.salary = salary
        self.work_experience = work_experience

    def get_info(self):
        return (f'Name: {self.name} {self.lastname}, '
                f'Age: {self.age}, '
                f'Position: {self.position}, '
                f'Salary: {self.salary}, '
                f'Experience: {self.work_experience}, '
                f'Specialty: {self.spec}, '
                f'Points: {self.points}')

    def get_sick_leave_perc(self):
        salary = float(self.salary.strip('$'))
        experience_years = int(self.work_experience.split()[0])

        if experience_years < 1:
            return salary * 0.6
        elif experience_years < 5:
            return salary * 0.5
        elif experience_years < 10:
            return salary * 0.4
        else:
            return salary * 0.3

    def changeAge(self, new_age):
        self.age = new_age
        return f'Age changed to {new_age}'


class Salary(Employee):
    def isRetiree(self):
        return self.age >= 65


if __name__ == "__main__":
    alice_student = Student('Alice', 'Camry', 18)
    mark_student = Student('Mark', 'Camer', 19)

    random_id_alice = alice_student.get_random_id()
    random_id_mark = mark_student.get_random_id()

    print("Student IDs:", Student.all_ids)
    print(alice_student.get_info())

    alice_person = Person('Alice', 'Camry', 18)
    alice_person.set_points(85)
    alice_person.set_spec('Computer Science')

    print(alice_person.get_info())
    print(f"Is successful: {alice_person.is_successful()}")
    print(f"Full name: {alice_person._getFullName()}")

    alice_employee = Employee('Alice', 'Camry', 18, 'Junior Developer', '800$', '2 years', 85, 'CS')
    print(alice_employee.get_info())
    print(f"Sick leave: ${alice_employee.get_sick_leave_perc():.2f}")

    older_employee = Salary('John', 'Doe', 70, 'Senior Developer', '2000$', '40 years', 90, 'CS')
    print(f"Is retiree: {older_employee.isRetiree()}")