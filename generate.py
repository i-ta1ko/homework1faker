from faker import Faker
import csv
import random

fake = Faker()

def generate_data():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'plan', 'username', 'last_login_date', 'expire_date'])
        for i in range(1000):
            plan = random.choice(['free', 'basic', 'full'])
            if plan == 'free':
                expire_date = ''
            else:
                expire_date = fake.date_this_decade()
            writer.writerow([i + 1, plan, fake.user_name(), fake.date_this_decade(), expire_date])

generate_data()