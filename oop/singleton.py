instance = None

class Singleton:
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Singleton()
            return instance
        else:
            return instance

inst1 = Singleton.getInstance()
inst2 = Singleton.getInstance()

print(id(inst1))
print(id(inst2))


