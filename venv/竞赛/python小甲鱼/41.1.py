class C2F(float):
    "摄氏度转换为华氏度"
    def __new__(cls, arg=0.0):
        print(arg)#测试用语句
        return float.__new__(cls, arg * 1.8 + 32)

print(type(C2F(54)))
print(C2F(54))