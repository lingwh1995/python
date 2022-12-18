# Python中的自定义异常、手动抛出异常、捕获自定义异常


print('Python中的自定义异常、手动抛出异常、捕获自定义异常')


# 判断手机号是否有非法字符串的异常,没有具体逻辑,不要使用这个异常进行测试
class PhoneNumberNotDigitException(Exception):
    pass


# 判断手机号位数是否合法的异常
class PhoneNumberLengthException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


# 手动抛出自定义异常
def test_phone_number():
    phone_number = input('请输入一个11位的手机号:')
    if not phone_number.isdigit():
        raise PhoneNumberNotDigitException()
    elif len(phone_number) != 11:
        raise PhoneNumberLengthException('手机号位数不对...')
    return phone_number


# 捕获自定义异常
def get_phone_number():
    try:
        phone_number = test_phone_number()
    except (PhoneNumberNotDigitException, PhoneNumberLengthException) as e:
        print(e)
    else:
        print('用户输入的手机号码是:', phone_number)


# 测试自定义异常
get_phone_number()