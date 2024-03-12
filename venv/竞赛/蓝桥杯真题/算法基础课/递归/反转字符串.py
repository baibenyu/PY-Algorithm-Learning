# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 19:30'

import time

start = time.clock()


def reverse_string(string: str, index):
    if index == 0:
        return string[index]
    else:
        return string[index] + reverse_string(string[:index], index - 1)


print(reverse_string("asdfghjkl", 8))
end = time.clock()
print(end - start)
