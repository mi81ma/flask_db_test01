# Udemy
# python コンストラクタとデストラクタ
# https://www.udemy.com/python-beginner/learn/v4/t/lecture/8379834?start=0

class Person(object):

    # コンストラクタ: 初期化の際に呼ばれる関数
    def __init__(self, name):
        self.name = name
        print(self.name)



    def say_something(self):
        print('hello')
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)


    # デストラクタ: クラスのインスタンスが使われなくなった時に呼ばれる関数
    def __del__(self):
        print('good bye')


person = Person('Mike')
person.say_something()

print("----------------------------------------") #この後にデストラクタが呼ばれる

# インスタンスを明示的に削除する時にも、デストラクタが呼ばれる
del person

print("----------------------------------------")