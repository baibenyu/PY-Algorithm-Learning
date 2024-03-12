import easygui as e
import sys

list1 = list(e.multenterbox('带*的为必填项','账号中心',fields = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-maile']))
while list1[0] == '' or list1[1] == '' or list1[3] == '' or list1[5] == '':
    list1=list(e.multenterbox('带*的为必填项,请填写完整!', '账号中心', fields = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', 'E-maile']))
print(list1)
