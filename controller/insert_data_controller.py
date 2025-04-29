import faker

from crud import insert_table as it
from database.connect import create_connection, database


def generate_fake_data() -> tuple():
    NUMBER_STUDENTS = 30
    NUMBER_TEACHERS = 4
    NUMBER_GRADES = 20

    fake_students = []
    fake_groups = [('Група А',), ('Група Б',), ('Група В',)]
    fake_teachers = []
    fake_subjects = [('Математика', 1), ('Фізика', 2), ('Хімія',3), ('Історія',4), ('Біологія',1), ('Література', 2)]
    fake_grades = []

    fake_data = faker.Faker()

    for _ in range(NUMBER_STUDENTS):
        fake_students.append((fake_data.first_name(),
                              fake_data.last_name(),
                              fake_data.random_int(1, 3)
                              ))

    for _ in range(NUMBER_TEACHERS):
        fake_teachers.append((fake_data.first_name(),
                              fake_data.last_name()
                              ))
    for student_id in range(1, NUMBER_STUDENTS + 1):

        for _ in range(NUMBER_GRADES):
            fake_grades.append((fake_data.random_int(1, 12),
                                student_id,
                                fake_data.random_int(1, 6),
                                fake_data.random_int(1, 4)
                                ))

    return fake_students, fake_groups, fake_teachers, fake_subjects, fake_grades


def insert_data_to_db(fake_student, fake_group, fake_teachers, fake_subjects, fake_grades):
    with create_connection(database) as conn:
        if conn is not None:
            it.insert_groups(conn, fake_group)
            it.insert_teachers(conn, fake_teachers)
            it.insert_subjects(conn, fake_subjects)
            it.insert_students(conn, fake_student)
            it.insert_grades(conn, fake_grades)


