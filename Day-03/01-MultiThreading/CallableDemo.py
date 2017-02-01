class Callable(object):
    def __init__(self, name=''):
        self.name = name
        
    def __call__(self):
        print('my name is ', self.name)

c1 = Callable(name='c1')
c2 = Callable(name='c2')

c1()
c2()