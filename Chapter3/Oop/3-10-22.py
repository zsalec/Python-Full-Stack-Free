# 抽象类的实现
import abc


# 声明一个类并且指定当前类的元素
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    #@abc.abstractclassmethod
    @classmethod
    def drink(cls):
        pass

    # 定义静态抽象方法
    #@abc.abstractstaticmethod
    @staticmethod
    def play():
        pass

    def sleep(self):
        pass
