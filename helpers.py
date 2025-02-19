from faker import Faker

faker = Faker()


class InputData:

    name = faker.first_name()
    email = faker.email()
    password = faker.password()