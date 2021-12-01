import getpass
database = {"ujjwal.lamsal" : "876363" , "python.class" : "656521"}
username = input("enter your username : ")
password = input("enter your passwword : ")
for ele in database.keys():
    if username == ele :
        while password != database.get(ele):
            password = getpass.getpass("enter your password again")
        break
print("verified")

