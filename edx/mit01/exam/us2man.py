def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
             '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    num = int(us_num)
    if num > 10:
        if num < 20:
            return 'shi '+trans[us_num[1]]
        else:
            unit = trans[us_num[1]]
            if unit == 'ling':
                return trans[us_num[0]]+' shi'
            else:
                return trans[us_num[0]]+' shi '+unit
    else:
        return trans[us_num]
for i in range(100):
    print(convert_to_mandarin(str(i)))
    