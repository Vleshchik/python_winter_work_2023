#1
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
a = Node(1111)
b = Node(22)
c = Node(3)
d = Node(444)
e = Node(55)
a.next_node = c
b.next_node = d
c.next_node = b
d.next_node = e
count = 1

max = a.value
y = a
while y.next_node != None:
    if max < y.value:
        max = y.value
    y = y.next_node
print(max)
#2
x = 'Используя стек, напечатайте эту строку в обратном порядке.'
l = list(x)
for i in range(len(l)):
    print(l.pop(), end='')
"""
def rev(s):
    l = list(s)
    l_rev = []
    for i in range(len(s)):
        l_rev.append(l.pop())
    return ''.join(l_rev)
print(rev(x))
"""
#3
s = []
def push_s(i):
    if not s:
        s.append([])
        s[-1].append(i)
    else:
        if len(s[-1]) < 10:
            s[-1].append(i)

        else:
            s.append([])
            s[-1].append(i)
def pop_s():
    if not s:
        return 'Тарелок нет'
    else:
        if len(s[-1]) > 1:
            return s[-1].pop()
        else:
            x = s[-1].pop()
            s.pop()
            return x
for i in range(1, 15):
    push_s(i)
    print(s)
for i in range(10):
    i = pop_s()
    print(i)
    print(s)
#4
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
if __name__ == '__main__':
    app.run(debug=True)