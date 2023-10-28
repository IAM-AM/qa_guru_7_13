from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_day: int
    date_of_birth_month: int
    date_of_birth_year: int
    subject: list
    hobby: list
    picture: str
    current_address: str
    state: str
    city: str
