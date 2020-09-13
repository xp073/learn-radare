import logging, os, r2pipe, threading

class RadareSession():
    def __init__(self, dir, sm, id):
        self.sm = sm
        self.id = id
        try:
            self.__pipe = r2pipe.open(dir)
            self.sm.logger.info(f"New session ({self.id}) created opening {dir}.")
        except Exception as e:
            self.sm.logger.exception(f"Couldn't create new session ({self.id}) opening {dir} bc {e}")


    def execute(self, cmd):
        self.sm.logger.info(f"Session ({self.id}) executing {cmd}.")
        #TODO: sterilize the command
        try:
            return self.__pipe.cmd(cmd)
        except Exception as e:
            self.sm.logger.exception(f"Session ({self.id}) couldn't execute {cmd} bc {e}")

    def __del__(self):
        self.sm.logger.info(f"Session ({self.id}) executing {cmd}.")
        del self.__pipe

class SessionManager():
    def __init__(self, radare_path):

        os.environ['PATH'] = os.environ['PATH'] + f";{radare_path}"
        self.__sessions = {}
        self.maxid = 0
        self.logger = logging.getLogger("SessionManager")
        self.logger.info(f"New session manager created.")

    def create_radare_session(self, dir):
        id = self.maxid
        self.__sessions[id] = RadareSession(dir, self, id)
        self.maxid += 1
        return id

    def end_radare_session(self, id):
        self.logger.info(f"Session ({id}) is trying to be closed.")
        try:
            del self.__sessions[id]
            self.logger.info(f"Session ({id}) is closed.")
            return True
        except Exception as e:
            self.logger.exception(f"Session ({id}) has failed to be closed bc {e}")
            return False
        self.__sessions[id]

    def __getitem__(self, key): # SessionManager[key]
        # Raise TypeError if key is not a known type
        # Raise KeyError if key is not in the dictionary
        if not (key in list(self.__sessions.keys())):
            self.logger.exception(f"Requested session ({key}) is not present in dictionary.")
            raise KeyError("ID is not in sessions.")
        return self.__sessions[key]

    def __setitem__(self, key):
        raise Exception("Not allowed to set session manager sessions. Use create_radare_session.")

    def __delitem__(self, key):
        del self.__sessions[key]

sm = SessionManager("D:\\h\\openradare\\openradare\\radare2-install\\bin")
