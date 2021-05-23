class Cloud:
    def __init__(self):
        self.cloudType = ""
        self.cloudStorage = ""
        self.authentication = ""

    def getInfo(self):
        return self.cloudType + ' ' + self.cloudStorage + ' ' + self.authentication

class CloudBuilder:
    def __init__(self):
        self.cloud = Cloud()

    def setCloudType(self, cloudType):
        self.cloud.cloudType = cloudType
        return self

    def setCloudStorage(self, storage):
        self.cloud.cloudStorage = storage
        return self

    def setAuthentication(self, auth):
        self.cloud.authentication = auth
        return self

    def getResult(self):
        return self.cloud



class Director():
    @staticmethod
    def construct():
        return CloudBuilder().setCloudType('AWS').setCloudStorage('SSD').setAuthentication('TOKEN').getResult()

cloud = Director.construct()
print(cloud.getInfo())