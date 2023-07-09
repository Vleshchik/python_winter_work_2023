class Foo(object):
    bar = True
Foo1 = type('Foo1', (), {'bar': True})
Foo1Child = type('Foo1Child', (Foo1,), {})

def echo_bar(self):
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
#print(hasattr(FooChild, 'echo_bar'))
my_foo = FooChild()
my_foo.bar = '123'
my_foo.echo_bar()




