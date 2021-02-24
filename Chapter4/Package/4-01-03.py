# 借助于 importlib 包可以实现导入以数字开头的模块名称
import importlib

# 相当于导入了一个叫 4_01_01 的模块，并把导入的模块赋值给了 tuling
tuling = importlib.import_module('4-01-01')

stu = tuling.Student()
stu.say()  # My name is NoName
