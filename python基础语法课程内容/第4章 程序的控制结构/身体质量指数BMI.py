#BMI3.py
import time
height, weight = eval(input("请输入身高（cm）和体重（kg），并用逗号隔开："))
bmi = weight / pow(height/100,2)
print("BMI数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat ="偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat ="正常", "正常"
elif 24 <= bmi < 25:
    who, nat ="正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat ="偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat ="偏胖", "肥胖"
elif bmi >30:
    who, nat ="肥胖", "肥胖"
print("您的BMI指标为：(国际标准){0},(国内标准){1}".format(who,nat))
time.sleep(1)