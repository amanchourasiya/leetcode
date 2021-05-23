class Test:
    def test(self):
        self.a = 'a'
        self.test1()
        print(self.a)

    def test1(self):
        print('test1',self.a)
        self.a = 'b'
        print('test1', self.a)

t = Test()
t.test()