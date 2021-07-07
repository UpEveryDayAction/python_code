def handler(func, *args):
    return func(*args)

def func1(hoge):
    return hoge

def func2(hoge, huga):
    return hoge,huga

func_dic = {"func1":func1, "func2":func2}

hoge = 1
huga = 2
result1 = handler(func_dic["func1"],hoge)
result2 = handler(func_dic["func2"],hoge, huga)
print(result1)
print(*result2) #アンパックされる