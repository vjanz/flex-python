from factory import Factory, faker

from app.schemas import UserCreate


class UserCreateFactory(Factory):
    class Meta:
        model = UserCreate

    password = faker.Faker("password")
    name = faker.Faker("name")
    full_name = faker.Faker("name")
    email = faker.Faker("email")
