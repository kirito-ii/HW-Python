from sqlalchemy import create_engine, text

db_connection_string = 'postgresql://postgres:123@localhost:5432/QA'

db = create_engine(db_connection_string)

def test_db_connection():
    names = db.table_names()
    assert names[0] == 'subject'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from users").fetchall()
    row1 = rows[0]

    assert row1["user_id"] == 42568
    assert row1["user_email"] == "igorpetrov@mail.ru"

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from users where user_id = :users_id")
    rows = db.execute(sql_statement, users_id=42568 ).fetchall()

    assert len(rows) == 1
    assert rows[0]["user_email"] == "igorpetrov@mail.ru"

def test_insert():
        db = create_engine(db_connection_string)
        sql = text("insert into users(\"user_email\") values (:new_user)")
        rows = db.execute(sql, new_user='SkyPro@mail.com')

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update users set user_id = :id, subject_id = :sub where user_email = :mail")
    rows = db.execute(sql, id = 9, mail = 'SkyPro@mail.com', sub = 3)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from users where user_id = :id")
    rows = db.execute(sql, id = 9)