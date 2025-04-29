from sqlite3 import Error


def get_top_students_by_average_grade(conn):

    sql = """
        SELECT s.first_name, s.last_name, ROUND(AVG(g.grade), 2) AS avg_grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        GROUP BY s.id
        ORDER BY avg_grade DESC
        LIMIT 5
    """

    curr = conn.cursor()
    try:
        curr.execute(sql)
    except Error as e:
        print(e)

    return curr.fetchall()


def get_top_student_by_subjects(conn, subject):

    sql = """
        SELECT a.*
        FROM
            (SELECT ROUND(AVG(g.grade)) as grade, s.first_name, s.last_name, s2.name
            FROM grades g
            LEFT JOIN students s on g.student_id = s.id
            LEFT JOIN subjects s2 on g.subject_id = s2.id
            GROUP BY s.first_name, s.last_name) a
        WHERE a.name = (?)
        ORDER BY a.grade DESC
        LIMIT 1
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (subject,))
    except Error as e:
        print(e)

    return curr.fetchone()


def get_top_group_by_subjects(conn, subject):

    sql = """
        SELECT gr.name AS group_name, ROUND(AVG(g.grade), 2) AS avg_grade, s2.name
        FROM grades g
        LEFT JOIN students s ON g.student_id = s.id
        LEFT JOIN groups gr ON s.group_id = gr.id
        LEFT JOIN subjects s2 on g.subject_id = s2.id
        WHERE s2.name = (?)
        GROUP BY gr.id
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (subject,))
    except Error as e:
        print(e)

    return curr.fetchall()


def get_average_grade(conn):

    sql = """
        SELECT ROUND(AVG(grade), 2) AS avg_grade
        FROM grades
    """

    curr = conn.cursor()
    try:
        curr.execute(sql)
    except Error as e:
        print(e)

    return curr.fetchone()


def get_subjects_by_teacher(conn, teacher_id):

    sql = """
        SELECT t.first_name, t.last_name, s.name 
        FROM subjects s 
        LEFT JOIN teachers t on s.teacher_id = t.id
        WHERE t.id = (?)
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (teacher_id,))
    except Error as e:
        print(e)

    return curr.fetchall()


def get_students_by_group(conn, group):

    sql = """
        select s.first_name, s.last_name, g.name 
        from students s
        LEFT JOIN groups g on s.group_id = g.id 
        WHERE g.name = (?)
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (group,))
    except Error as e:
        print(e)

    return curr.fetchall()


def get_grade_by_student(conn, group, subject):

    sql = """
        SELECT g.grade, s.first_name, s.last_name, g2.name as group_name, s2.name as subject_name
        FROM grades g
        LEFT JOIN students s on g.student_id = s.id
        LEFT JOIN groups g2 on s.group_id = g2.id
        LEFT JOIN subjects s2 on g.subject_id = s2.id
        WHERE g2.name = (?) AND s2.name = (?)
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (group, subject))
    except Error as e:
        print(e)

    return curr.fetchall()


def get_average_grade_by_subject(conn, teacher_id):

    sql = """
        SELECT ROUND(AVG(g.grade), 2) AS avg_grade, t.first_name, t.last_name
        FROM grades g
        LEFT JOIN teachers t on g.teacher_id = t.id 
        WHERE t.id = (?)
        GROUP BY t.id
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (teacher_id,))
    except Error as e:
        print(e)

    return curr.fetchone()


def get_subject_by_student(conn, subject):

    sql = """
        SELECT s2.name, s.first_name, s.last_name 
        FROM grades g
        LEFT JOIN students s on g.student_id = s.id
        LEFT JOIN subjects s2 on g.subject_id = s2.id
        WHERE s2.name = (?)
    """

    curr = conn.cursor()
    try:
        curr.execute(sql, (subject,))
    except Error as e:
        print(e)

    return curr.fetchall()


def get_subject_by_student_and_teacher(conn, student_id, teacher_id):

    sql = """
        select DISTINCT s.name as subject_name
        from grades g
        LEFT JOIN subjects s ON g.subject_id = s.id
        where g.student_id = (?) and g.teacher_id = (?)
    """
    curr = conn.cursor()
    try:
        curr.execute(sql, (student_id, teacher_id))
    except Error as e:
        print(e)

    return curr.fetchall()

