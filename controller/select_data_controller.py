from crud import select_table as st
from database.connect import create_connection, database


def get_data(
        number_sql: int,
        subject: str = 'Хімія',
        teacher_id: int = 2,
        group: str = 'Група Б',
        student_id: int = 13
):
    with create_connection(database) as conn:
        if conn is not None:
            if number_sql == 1:
                return st.get_top_students_by_average_grade(conn)
            elif number_sql == 2:
                return st.get_top_student_by_subjects(conn, subject)
            elif number_sql == 3:
                return st.get_top_group_by_subjects(conn, subject)
            elif number_sql == 4:
                return st.get_average_grade(conn)
            elif number_sql == 5:
                return st.get_subjects_by_teacher(conn, teacher_id)
            elif number_sql == 6:
                return st.get_students_by_group(conn, group)
            elif number_sql == 7:
                return st.get_grade_by_student(conn, group, subject)
            elif number_sql == 8:
                return st.get_average_grade_by_subject(conn, teacher_id)
            elif number_sql == 9:
                return st.get_subject_by_student(conn, subject)
            elif number_sql == 10:
                return st.get_subject_by_student_and_teacher(conn, student_id, teacher_id)
            else:
                print(f"Вказано невірний номер {number_sql}")
