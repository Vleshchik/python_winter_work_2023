class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
a = Node(1)
b = Node(22)
a.next_node = b
c = Node(333)
b.next_node = c
x = a
while x.next_node != None:
    x = x.next_node
    print(x.value)

#2
import math
def __init__(self, x, y):
    self.x = x
    self.y = y

Point = type('Point', (), {'__init__':__init__})

p = Point(1, 2)

def __str__(self):
    return str((self.x, self.y))
Point.__str__ = __str__

lst = [(0,0),(1,1),(2,2),(1,3)]
point_list = []
for i in lst:
    point_list.append(Point(i[0],i[1]))
for i in point_list:
    print(i)

def distance(self, other):
    res = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
    return math.sqrt(res)
Point.distance = distance
print(Point.distance(point_list[0],point_list[1]))
for i in point_list:
    for j in point_list:
        if Point.distance(i, j) > 2:
            print(i, j, Point.distance(i, j))

#3
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next_node = c
b.next_node = d
c.next_node = b
d.next_node = e
count = 1
#x = Node('x')
#x.next_node = a
#y = x
y = a
print(y.value, count)
while y.next_node != None:
    count += 1
    y = y.next_node
    print(y.value, count)
print(count)
#4
class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)
    def __str__(self):
        res = 'AnyClass:'
        for k, v in self.__dict__.items():
            res += ' '+str(k)+':'+str(v)+', '
        return res.strip(', ')
    def __repr__(self):
        res = 'AnyClass('
        for k, v in self.__dict__.items():
            res += str(k)+'='+str(v)+', '
        return res.rstrip(', ')+')'


a1 = AnyClass(a = 1, b = 123, x = 77)
a2 = AnyClass()
a3 = AnyClass(k = 'sdfsdfssdf')

print(str(a1))
print(repr(a1))
print(str(a2))
print(repr(a2))
#5
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Topic(Base):

    __tablename__ = 'topic'
    __tableargs__ = {
        'comment': 'Темы цитат'
    }

    topic_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(128), comment='Наименование темы')
    description = Column(Text, comment='Описание темы')

    def __repr__(self):
        return f'{self.topic_id} {self.name} {self.description}'


class Author(Base):

    __tablename__ = 'author'
    __tableargs__ = {
        'comment': 'Авторы цитат'
    }

    author_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(128), comment='Имя автора')
    birth_date = Column(Date, comment='Дата рождения автора')
    country = Column(String(128), comment='Страна рождения автора')

    def __repr__(self):
        return f'{self.author_id} {self.name} {self.birth_date} {self.country}'


class Quote(Base):

    __tablename__ = 'quote'
    __tableargs__ = {
        'comment': 'Цитаты'
    }

    quote_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    text = Column(Text, comment='Текст цитаты')
    created_at = Column(DateTime, comment='Дата и время создания цитаты')
    author_id = Column(Integer,  ForeignKey('author.author_id'), comment='Автор цитаты')
    topic_id = Column(Integer, ForeignKey('topic.topic_id'), comment='Тема цитаты')
    author = relationship('Author', backref='quote_author', lazy='subquery')
    topic = relationship('Topic', backref='quote_topic', lazy='subquery')

    def __repr__(self):
        return f'{self.text} {self.created_at} {self.author_id} {self.topic_id}'

engine = create_engine('postgresql://user:password@host:port/db_name')
Base.metadata.create_all(engine)