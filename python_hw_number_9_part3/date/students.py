import dataclasses


@dataclasses.dataclass
class Student:
    fill_name: str
    email: str
    current_address: str
    permanent_address: str


people = Student(
    fill_name='Петров Петр Иванович',
    email='Petr@mail.ru',
    current_address='Тестовый проезд д.1000',
    permanent_address='Тестовый проезд д.454'
)
