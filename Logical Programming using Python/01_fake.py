#Faker module
from faker import Faker
fake=Faker()
print(fake.name())
print(fake.email())
print(fake.address())
print(fake.country())