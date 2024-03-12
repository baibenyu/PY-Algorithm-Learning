# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/8 14:39'

def GetReal():
    number = eval(input("please  input  a  number:").strip())
    return number


def GetString():
    string = input("please  input  a  string:").strip()
    return string


def main():
    number = GetReal()
    string = GetString()
    print(number)
    print(string)


main()
