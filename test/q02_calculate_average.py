def calculate_average(numbers):
    sumNum = sum(numbers)
    svrNum = sumNum/len(numbers)
    print(svrNum)
    print("{:.3f}".format(svrNum))

calculate_average([1,2,1])