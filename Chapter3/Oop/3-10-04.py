# 子类扩充父类功能的案例
# Person 有 work 的函数，Teacher 也有 work 的函数，但 Teacher 的工作需要讲课
class Person:
    name = 'NoName'
    age = 0
    __score = 0  # 考试成绩是秘密，只有自己知道
    _petname = 'sec'  # 小名，是受保护的，子类可以用，单不能公用

    def sleep(self):
        print('Sleeping......')
        return None

    def work(self):
        print('make some money')
        return None


# 父类卸载括号中
class Teacher(Person):
    teacher_id = '9527'
    name = 'dana'

    def make_test(self):
        print('attention')
        pass

    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Person.work(self)
        super().work()
        self.make_test()


t = Teacher()
t.work()
'''
make some money
make some money
attention
'''
