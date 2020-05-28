
def operationAdd(a, b):

    max_num_length = max(len(a), len(b))

    # 存放最终的结果　
    sum = [0] * (max_num_length + 1)

    # 把两个数的位数设置一致　前面用0补充
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b

    # 运算加法
    for i in range(max_num_length):
        int_a = int(a[-i-1])
        int_b = int(b[-i-1])

        digit = (int_a + int_b + sum[-i-1]) % 10
        ten_digit = int((int_a + int_b + sum[-i-1]) / 10)

        sum[-i-1] = digit              # 00123456789
        sum[-i-2] = ten_digit              # 98765432111



    # 将整形的列表变为字符型的列表　方便下一步将函数的返回值变为字符型
    sum = list(map(str, sum))

    #　前面是0的话去0操作
    if sum[0] == "0":
        return "".join(sum)[1:]
    else:
        return "".join(sum)

# 大数加法
if __name__ == '__main__':

    a = str(123456789)
    b = str(98765432111)
    print(operationAdd(a, b))



