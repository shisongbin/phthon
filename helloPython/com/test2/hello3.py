int_nums = 1
"""
Create on 2018/11/28
作者:施松彬
"""
while int_nums < 10:
    print(int_nums)
    int_nums += 1

array_str = ["a", "b", "c"]

for item in array_str:
    print(item)

for idx, item in enumerate(array_str):
    print("位置:" + str(idx) + "值:" + item)

# else 是循环体正常结束的时候展现
print("=======================================================")
for idx, item in enumerate(array_str):
    print("位置:" + str(idx) + "值:" + item)
else:
    print("循环体结束")

for idx, item in enumerate(array_str):
    print("位置:" + str(idx) + "值:" + item)
    if (idx == 1):
        break
else:
    print("循环体结束")

str = "helloworld"

print(str[1:2])

# 元组
tuple_a = (1, 2, "v", "2", "e")
print(tuple_a[1:5:2])
# 元组拆包
ele_a, ele_b, *ele_others = tuple_a
print(ele_a)
print(ele_others)

# 元祖 和 列表区别，元组是不可以被修改的
array_students = ["张三", "李四", "王五"]
array_students.append("赵六")
print(array_students)
array_students.insert(0, "王二")
print(array_students)
array_students[0] = "王二二"
print(array_students)
array_students.remove("王二二")
print(array_students)
array_students.pop(0)
print(array_students)
print(array_students.index('王五'[0:3]))
print(array_students.count('王五'))
array_students_copy = array_students.copy();
array_students_copy.reverse()
print(array_students_copy)
array_students_copy.clear();
print(array_students_copy)

# 数组推导式
print("================================")
array_n = []
for x in range(10):
    if x % 2 == 0:
        array_n.append(x ** 2)
print(array_n)

array_n = [x ** 2 for x in range(10) if x % 2 == 0]
print(array_n)

# 不可变集合
set_a = frozenset({"啊", "v", 1})
print(type(set_a))

# 字典
dict_a = {1: "张三", 2: "李四", 3: "王五"}
for k, v in dict_a.items():
    print(k, v)
