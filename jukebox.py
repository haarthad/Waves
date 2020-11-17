import tidalapi
import os.path


class Jukebox:
    def __init__(self):
        print("Jukebox initializing")
        self.session  = None
        self.username = None
        self.password = None
        self.credentials = "credentials.txt"

    def setup(self):
        if not os.path.isfile(self.credentials):
            print("Tidal credentials not found")
            self.username = input("Enter your email address: ")
            self.password = input("Enter your password: ")

            writer = open(self.credentials, "w")
            writer.write(self.username+"\n")
            writer.write(self.password+"\n")
        else:
            print("Tidal credentials found")
        
    def signin(self):
        # Read username and password from credentials file
        file = open(self.credentials, 'r')
        credentials = file.readlines()
        self.username = credentials[0]
        self.password = credentials[1]
        
        # Create tidal session and login
        self.session = tidalapi.Session()
        self.session.login(self.username, self.password)
