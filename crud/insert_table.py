from sqlite3 import Error


def insert_students(conn, students):

    sql = """
        INSERT INTO students(first_name, last_name, group_id)
        VALUES(?,?,?);
        """
    cur = conn.cursor()
    try:
        cur.executemany(sql, students)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def insert_groups(conn, groups):

    sql = """
        INSERT INTO groups(name)
        VALUES(?);
        """
    cur = conn.cursor()
    try:
        cur.executemany(sql, groups)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def insert_teachers(conn, teachers):

    sql = """
        INSERT INTO teachers(first_name, last_name)
        VALUES(?,?);
        """
    cur = conn.cursor()
    try:
        cur.executemany(sql, teachers)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def insert_subjects(conn, subjects):

    sql = """
        INSERT INTO subjects(name, teacher_id)
        VALUES(?,?);
        """
    cur = conn.cursor()
    try:
        cur.executemany(sql, subjects)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def insert_grades(conn, grades):

    sql = """
        INSERT INTO grades(grade, student_id, subject_id, teacher_id)
        VALUES(?,?,?,?);
        """
    cur = conn.cursor()
    try:
        cur.executemany(sql, grades)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

