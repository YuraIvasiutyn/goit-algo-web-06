from crud.create_table import create_tables
from controller.insert_data_controller import generate_fake_data, insert_data_to_db
from controller.select_data_controller import get_data


def create_and_insert_table():
    create_tables()
    print("Таблиці створено")

    fake_students, fake_groups, fake_teachers, fake_subjects, fake_grades = generate_fake_data()
    insert_data_to_db(fake_students, fake_groups, fake_teachers, fake_subjects, fake_grades)


if __name__ == "__main__":
    create_and_insert_table()

    while True:
        number = input("Подай номер запиту: (1-10) ")
        if number.lower() == 'exit':
            break
        print(get_data(int(number)))





