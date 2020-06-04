from dbhelper import DBHelper


def main():
    db=DBHelper()
    while True:
        print("***Welcome to the App***")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display")
        print("Press 3 to display one user")
        print("Press 4 to update user")
        print("Press 5 to exit.")
        print()
        try:
            choice=int(input())
            if(choice ==1):
                #insert
                uid = int(input("Enter user id: "))
                username = input("Enter user name: ")
                userphone = input("Enter user phone: ")
                db.insert_user(uid, username, userphone)
            elif choice == 2:
                #display
                db.fetch_all()
            elif choice == 3:
                #update
                uid = int(input("Enter user id: "))
                db.fetch_one(uid)
            elif choice == 4:
                #update
                uid = int(input("Enter existing user id: "))
                username = input("Enter new user name: ")
                userphone = input("Enter new user phone: ")
                db.update_user(uid, username, userphone)
            elif choice == 5:
                break 
                #exit
            else:
                print("Invalid input ! Good Bye..")
        except Exception as e:
            print(e)
            print("Invalid details ! Good Bye..")

if __name__ == "__main__":
    main()
