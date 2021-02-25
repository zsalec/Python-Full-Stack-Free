# 自己组装一个类
class A:
    pass


def say(self):
    print('Saying...(function)')
    return None


class B:
    def say(self):
        print('Saying...(class B)')
        return None


say(9)  # Saying...(function)

A.say = say
a = A()
a.say()  # Saying...(function)

b = B()
b.say()  # Saying...(class B)
