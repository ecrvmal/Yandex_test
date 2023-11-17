def symbols(value):
    num = 1
    while True:
        if value < 10:
            return num
        num += 1
        value = value // 10

def max_digit(symbols):
    result = 10 ** symbols - 1
    return result

def reversed_long_digit(value, digits):
    now_digits = symbols(value)
    result = 0
    while True:
        if value < 10:
            result = result * 10 + value
            break
        result_digit = value % 10
        result = result *10 + result_digit
        value = value // 10
    extra_digits = digits - now_digits
    result = 10 ** extra_digits * result
    return result




def main():
    line = input(" please enter hours minutes: ")
    line_list = line.split(" ")
    line_list1 = [int(x) for x in line_list]
    hours = line_list1[0]
    minutes = line_list1[1]
    # print(hours, minutes)

    counter = 0
    if hours <= minutes:
        # print(f'hours {hours}, minutes : {minutes}')
        _symbols = symbols(minutes)
        for i in range(0, hours):
            # print (f'i: {i}')
            long_reversed_digit = reversed_long_digit(i, _symbols)
            if long_reversed_digit <minutes:
                # print (f'i {i}  long_digit : {long_reversed_digit}  minutes : {minutes}' )
                counter +=1

    if hours > minutes:
        # print(f'hours {hours}, minutes : {minutes}')
        _symbols = symbols(hours)
        for i in range(0, minutes):
            long_reversed_digit = reversed_long_digit(i, _symbols)
            if long_reversed_digit <hours:
                # print (f'i {i}  long_digit : {long_reversed_digit}  minutes : {minutes}' )
                counter +=1

    counter = counter % (10 ** 9 + 7)
    print(counter)


if __name__ == "__main__":
    # print(symbols(112))
    # print(reversed_digit(12345))
    # print(reversed_long_digit(10, 4))
    main()






