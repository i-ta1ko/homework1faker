import csv
import datetime

def load_data():
    with open('data.csv', 'r') as file:
        return list(csv.DictReader(file))

def total_accounts_per_plan(accounts):
    total_accounts = {}
    for account in accounts:
        if account['plan'] in total_accounts:
            total_accounts[account['plan']] += 1
        else:
            total_accounts[account['plan']] = 1
    for plan, count in total_accounts.items():
        print(f"{plan.capitalize()}: {count}")

def find_free_accounts_with_more_than_3_months(accounts):
    three = datetime.date.today() - datetime.timedelta(days=90)
    print("Free accounts with more than 3 months to login:")
    for account in accounts:
        if account['plan'] == 'free':
            last_login_date = datetime.datetime.strptime(account['last_login_date'], "%Y-%m-%d").date()
            if last_login_date < three:
                print(f"Id: {account['id']}, Username: {account['username']}, Last Login Date: {account['last_login_date']},")

def find_expired_basic_and_full_accounts(accounts):
    print("Basic and Full accounts that are expired:")
    for account in accounts:
        if account['plan'] in ['basic', 'full']:
            expire_date = account['expire_date']
            if expire_date and datetime.datetime.strptime(expire_date, "%Y-%m-%d").date() < datetime.date.today():
                print(f"Id: {account['id']}, Plan: {account['plan']}, Username: {account['username']}, Last Login Date: {account['last_login_date']}, Expire Date: {account['expire_date']}")

if __name__ == "__main__":
    accounts = load_data()

    while True:
        print("\nMenu:")
        print("1. Print total accounts per plan")
        print("2. Find free accounts with more than 3 months to login")
        print("3. Find basic and full accounts that are expired")
        print("4. Exit")    
        choice = input("Select an option: ")
        if choice == "1":
            total_accounts_per_plan(accounts)
        elif choice == "2":
            find_free_accounts_with_more_than_3_months(accounts)
        elif choice == "3":
            find_expired_basic_and_full_accounts(accounts)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")