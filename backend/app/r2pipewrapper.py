import r2pipe

class RadareSession():
    def __init__(self, id):
        self.id = id
        pass # TODO: initiate the session with r2pipe

    def __del__(self):
        pass # TODO: close the radare session

class SessionManager():
    def __init__(self, radare_path):
        #TODO: create dictionary of radare sessions
        pass
    def create_radare_session(self):
        pass # return id
    def end_radare_session(self, id):
        pass # return true or false

    def __getitem__(self, key): # SessionManager[key]
        # Raise TypeError if key is not a known type
        # Raise KeyError if key is not in the dictionary
        pass

    def __setitem__(self, key):
        raise Exception("Not allowed to set session manager sessions. Use create_radare_session.")

    def __delitem__(self, key):
        # call the del method of the appropriate radare session
        pass
