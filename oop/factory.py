from abc import ABC , abstractmethod

class AbstractClassCloud(ABC):
    @abstractmethod
    def getCloudType(self):
        pass


class CloudFactory():
    def getCloudInstance(self, cloudType):
        if cloudType == 'AWS':
            return AWS()
        elif cloudType == 'GCP':
            return GCP()

class AWS(AbstractClassCloud):
    def getCloudType(self):
        return "AWS"

class GCP(AbstractClassCloud):
    def getCloudType(self):
        return "GCP"


cloud = CloudFactory()
aws = cloud.getCloudInstance('AWS')
gcp = cloud.getCloudInstance('GCP')

print(gcp.getCloudType())