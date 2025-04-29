from sqlite3 import Error

from database.connect import create_connection, database


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def create_tables():
    sql_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            group_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (group_id) REFERENCES groups (id)
                ON DELETE SET NULL
            );
        """

    sql_groups_table = """
        CREATE TABLE IF NOT EXISTS groups(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """

    sql_teachers_table = """
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """

    sql_subjects_table = """
        CREATE TABLE IF NOT EXISTS subjects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            teacher_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
                ON DELETE SET NULL
            );
        """

    sql_grades_table = """
        create table grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade INT not null,
            student_id INT,
            subject_id INT,
            teacher_id INT,
            created_at TIMESTAMP default CURRENT_TIMESTAMP,
            foreign key (student_id) references students (id)
                on delete set null,
            foreign key (subject_id) references subjects (id)
                on delete set null,
            foreign key (teacher_id) references teachers (id)
		        on delete set null
            );
        """

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_students_table)
            create_table(conn, sql_groups_table)
            create_table(conn, sql_teachers_table)
            create_table(conn, sql_subjects_table)
            create_table(conn, sql_grades_table)
        else:
            print("Error! cannot create the database connection.")