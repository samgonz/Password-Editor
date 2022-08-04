import getpass

"""
This program will ask for your username and password. 
It will then confirm if the password and username provided have authority. 
It will print verified once the password is correct else it will ask for you to enter your password again.
"""
# The passwords for this program will be in a dictionary.
database = {"superman": "louislane", "batman": "parentless", "flash": "fastestman"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")

# Loops through the dictionary using username and password provided. 
# If it matches both username and password you will get "Verified" as a response.
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")