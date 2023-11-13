import dataclasses
from time import time


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    password: str
    zipcode: str
    phone_number: str
    country: str
    address1: str
    city: str


def create_customer_with_new_email():
    return User(
        first_name='John',
        last_name='Doe',
        email=str(time()) + '@test.com',
        gender='male',
        password='123456',
        zipcode='12345',
        phone_number='8800111111',
        country='United States',
        address1='42 Best street, suite 1',
        city='Dallas',
    )


registered_customer = User(
    first_name='Joe',
    last_name='Bloggs',
    email='test@111test.com',
    gender='female',
    password='123456Aa',
    zipcode='33333',
    phone_number='123456789',
    country='United States',
    address1='42 Best street, suite 1',
    city='Dallas',
)
