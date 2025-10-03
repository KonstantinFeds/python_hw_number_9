import dataclasses


@dataclasses.dataclass()
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    date_of_bith: dict
    hobbies: str
    mobile_number: str
    subjects: str
    picture: str
    address: str
    state: str
    city: str

student = User(

    first_name="Иван",
    last_name="Иванов",
    email="IIvanon23@gmai.com",
    gender='Male',
    date_of_bith = {"day":15,"month": "May", "year": 1940},
    hobbies = 'Sports',
    mobile_number='1234567891',
    subjects='Maths',
    picture='фото.jpg',
    address = 'Улица Пушкина, дом Колотушкина',
    state='Uttar Pradesh',
    city='Agra'
)





