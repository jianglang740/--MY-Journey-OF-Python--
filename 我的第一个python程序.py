balance = eval(input("请输入账户余额："))
if balance < 0:
    print("账户余额不能为负值")
else:
     annualInterestRate = eval(input("请输入年利率："))
     interest= balance *(annualInterestRate /1200)
     for i in range(1,13):
        balance = balance + interest
        print("第{:2d}个月余额为：{:.2f}".format(i,balance))