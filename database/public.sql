CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(40) NOT NULL,
	group_id INT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (group_id) REFERENCES groups (id)
		ON DELETE SET NULL
	)


CREATE TABLE groups(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name text NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	)


CREATE TABLE teachers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	)


CREATE TABLE subjects(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name text NOT NULL,
	teacher_id INT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (teacher_id) REFERENCES teachers (id)
		ON DELETE SET NULL
	)


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
		on delete set null
	foreign key (teacher_id) references teachers (id)
		on delete set null
	)