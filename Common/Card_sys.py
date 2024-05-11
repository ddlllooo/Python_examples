# -------------
# 名片管理系统
# -------------
import os

file_name = 'Card_Nan.txt'  # 保存文档名


# 菜单
def mean():
    print('----------------------------')
    print('\t 欢迎使用名片管理系统\n')
    print('\t 1.添加名片')
    print('\t 2.删除名片')
    print('\t 3.修改名片')
    print('\t 4.显示全部名片')
    print('\t 5.查询名片')
    print('\t 6.退出系统')
    print('----------------------------')


# 保存数据
def save_data(lis):
    try:
        card_data = open(file_name, 'a', encoding='utf-8')
    except:
        card_data = open(file_name, 'w', encoding='utf-8')
    for item in lis:
        card_data.write(str(item) + '\n')


# 添加名片
def insert_card():
    all_list = []
    while True:
        name = input('输入姓名：')
        if not name:
            break
        try:
            qq = int(input('输入QQ号：'))
            wechat = int(input('输入微信号：'))
            phone = int(input('输入手机号：'))
            address = str(input('输入地址：'))
        except:
            print('输入错误，请重新输入')
            continue
        Card = {'Name': name, 'QQ': qq, 'Wechat': wechat, 'Phone': phone, 'Address': address}
        all_list.append(Card)
        chiose = input("是否继续输入？  yes/no\n")
        if chiose == 'yes':
            continue
        else:
            break
    save_data(all_list)
    print('录入完毕')


# 删除名片
def del_card():
    while True:
        Card_name = input('输入删除者的姓名：')
        if Card_name != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as f:
                    card_all = f.readlines()
            else:
                card_all = []
            point = False
            if card_all:
                with open(file_name, 'w', encoding='utf-8') as fi:
                    di = {}
                    for item in card_all:
                        di = dict(eval(item))
                        if di['Name'] != Card_name:
                            fi.write(str(di) + '\n')
                        else:
                            point = True
                    if point:
                        print(f'姓名为{Card_name}的名片已删除')
                    else:
                        print(f'姓名为{Card_name}的名片未找到')
            else:
                print('该名片不存在')
                break
            see_all()
            chiose = input('是否继续删除操作? yes/no\n')
            if chiose == 'yes':
                continue
            else:
                break


# 显示格式
def show_card(lst):
    if len(lst) == 0:
        print('未查询到任何信息')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
    print(format_title.format('姓名', 'QQ', '微信', '手机号码', '地址'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('Name'),
                                 item.get('QQ'),
                                 item.get('Wechat'),
                                 item.get('Phone'),
                                 item.get('Address'),
                                 ))


# 查看所有名片
def see_all():
    card_all = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as fi:
            ca_all = fi.readlines()
            for item in ca_all:
                card_all.append(eval(item))
            if card_all:
                show_card(card_all)
    else:
        print('暂未保存数据!!!')


# 修改名片
def re_change():
    see_all()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as fi:
            card_all = fi.readlines()
    else:
        return
    card_name = input('输入需要修改的信息的姓名：')
    with open(file_name, 'w', encoding='utf-8') as f:
        for item in card_all:
            di = dict(eval(item))
            if di['Name'] == card_name:
                print('已找到此人的名片，请进行修改\n')
                while True:
                    try:
                        di['QQ'] = input('请输入qq号')
                        di['Wechat'] = input('请输入微信号')
                        di['Phone'] = input('请输入手机号')
                        di['Address'] = input('请输入地址')
                    except:
                        print('您的输入错误，请重新输入!!!!!!!')
                    else:
                        break
                f.write(str(di) + '\n')
                print('修改成功！')
            else:
                f.write(str(di) + '\n')
        chiose = input('是否继续进行修改？  yes/no\n')
        if chiose == 'yes':
            re_change()


# 查询名片
def search():
    card_go = []
    while True:
        name = ''
        if os.path.exists(file_name):
            name = input('请输入姓名')
        with open(file_name, 'r', encoding='utf-8') as f:
            card_all = f.readlines()
            for item in card_all:
                di = dict(eval(item))
                if di != '':
                    if di['Name'] == name:
                        card_go.append(di)
        show_card(card_go)
        card_go.clear()
        chioce = input('是否继续查询？ yes/no\n')
        if chioce == 'yes':
            continue
        else:
            break


def main():
    while True:
        mean()
        chiose = int(input('请选择功能'))
        if chiose in [1, 2, 3, 4, 5, 6]:
            if chiose == 6:
                rechiose = input('是否确定退出系统? yes/no\n')
                if rechiose == 'yes':
                    print('成功退出')
                    break
                else:
                    continue
            elif chiose == 1:
                insert_card()
            elif chiose == 2:
                del_card()
            elif chiose == 3:
                re_change()
            elif chiose == 4:
                see_all()
            elif chiose == 5:
                search()


if __name__ == '__main__':
    main()
