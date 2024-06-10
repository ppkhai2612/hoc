'''
Viết chương trình kiểm tra mật khẩu có hợp lệ hay không
Mật khẩu hợp lệ khi:
- Chứa ít nhất 8 ký tự
- Chứa ít nhất 1 chữ hoa, 1 chữ số và 1 ký tự đặc biệt
- Không chứa 3 chữ số liên tiếp
Khi user nhập mật khẩu không hợp lệ phải thông báo cho user biết họ bị lỗi gì
Khi user nhập mật khẩu hợp lệ thì in ra "Mật khẩu hợp lệ"
'''

while True:
    # Prompt user nhập mật khẩu
    password = input("Enter password: ")

    # Check pass có đủ 8 ký tự không
    if len(password) < 8:
        print("Mật khẩu phải chứa ít nhất 8 ký tự")
        continue

    # Check pass có chứa ít nhất 1 chữ hoa, 1 chữ số và 1 ký tự đặc biệt không
    check_upper = False
    check_digit = False
    check_special_character = False
    for i in password:
        if i.isupper():
            check_upper = True
        elif i.isdigit():
            check_digit = True
        elif not i.isalnum():
            check_special_character = True

    if check_upper == False:
        print("Mật khẩu phải chứa ít nhất 1 chữ hoa")
        continue
    elif check_digit == False:
        print("Mật khẩu phải chứa ít nhất 1 chữ số")
        continue
    elif check_special_character == False:
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt")
        continue

    # Check pass có 3 chữ số liền kề hay không
    check_adjacent_digits = True
    for i in range(len(password) - 2):
        if password[i].isdigit() and password[i + 1].isdigit() and password[i + 2].isdigit():
            print("Mật khẩu không chứa 3 chữ số liên tiếp")
            check_adjacent_digits = False
            break

    # Check pass hợp lệ
    if check_upper == True and check_digit == True and check_special_character == True and check_adjacent_digits == True:
        print("Mật khẩu hợp lệ")
        break