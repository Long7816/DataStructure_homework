dict_1 = {}

while True:  
    option = input('請選擇操作選項（a.註冊, b.登入, c.退出）? ').strip().lower()
    
    if option == 'a':
        account = input('請輸入帳號：').strip()
        if account in dict_1:
            print('帳號已存在，請重新輸入！')
        else:
            password = input('請輸入密碼：').strip()
            dict_1[account] = password
            print('註冊成功！')

    elif option == 'b':
        while True:
            account = input('請輸入帳號：（按"q"退回主選單）').strip()
            if account not in dict_1:
                print('此帳號未註冊，請重新輸入帳號！')
            elif account.lower() == 'q':
                break
            else:
                while True:
                    password = input(f'請輸入密碼：（按"q"退回主選單）').strip()
                    if password == dict_1[account]:
                        print(f'登入成功！')
                        break
                    elif password.lower() == 'q':
                        break
                    else:
                        print('密碼輸入錯誤，請重新輸入密碼，')
            if password == dict_1[account]:
                break
        if password == dict_1[account]:
            break

    elif option == 'c':
        print('系統已退出！')
        break
        
    else:
        print('輸入錯誤，請輸入 a, b 或 c！')
