__author__ = 'tyroneswinnie'


class Storage(object):
    def __init__(self):
        self.pictures = 0  #the number of pictures in GB
        self.videos = 0  #the number of videos in GB
        self.documents = 0  #the number of documents in GB
        self.music = 0  #the number of music in GB
        self.apps = 0  #the number of all files stored in GB
        self.__remaining = 0  #total storage remaining




    @property
    def final_storage(self):
            self.__remaining = 50 - (self.pictures + self.videos + self.documents + self.music + self.apps)  #do the math for the remaining storage
            return self.__remaining

        #now I will set up my setter

    @final_storage.setter
    def final_storage(self, new_final_storage):
            pass  # not using my setter right now


