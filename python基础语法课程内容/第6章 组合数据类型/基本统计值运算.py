#基本统计值问题
def getnum():
    nums = []
    inum = input("请输入数字(回车退出):")
    while inum != "":
        nums.append(eval(inum))
        inum = input("请继续输入数字(回车退出):")
    return nums
def mean(numners): #求平均值
    s = 0.0
    for num in numners:
        s += num
    return s/(len(numners))
def dev(numbers,mean): #计算方差
    sdev = 0.0
    for num in numbers:
        sdev += (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)  #为什么-1？
def median(numbers): #计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2+1])/2
    else:
        med = (numbers[size//2])
    return med

n = getnum()
m = mean(n)
print("平均值是:{}\n方差是:{:.2f}\n中位数是:{}".format(m,dev(n,m),median(n)))