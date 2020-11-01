import tidalapi

class Jukebox:
    def __init__(self):
        print("Jukebox initializing")
        self.session  = None
        self.username = None
        self.password = None
        self.credentials = "credentials.txt"
        
    def signin(self):
        # Read username and password from credentials file
        file = open(self.credentials, 'r')
        credentials = file.readlines()
        self.username = credentials[0]
        self.password = credentials[1]
        
        # Create tidal session and login
        self.session = tidalapi.Session()
        self.session.login(self.username, self.password)
