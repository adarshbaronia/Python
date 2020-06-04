import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con= connector.connect(
                            host='localhost',
                            port='3306',
                            user='root',
                            password = 'sql20',
                            database = 'pythontest'
                            )
        query = 'create table if not exists user(userID int primary key, username varchar(200), phone varchar(200))'

        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self, userid, username, phone):
        query = "insert into user(userID, username, phone) values({},'{}', '{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")

    #fetch all
    def fetch_all(self):
        query  = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserID: ", row[0])
            print("User name: ", row[1])
            print("User Phone: ", row[2])
            print()

    def fetch_one(self, id):
        query = "select * from user where userID = {}".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User name: ", row[1])
            print()

    #update
    def update_user(self, id, name, ph):
        query="update user set username='{}', phone='{}' where userID={}".format(name, ph, id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
