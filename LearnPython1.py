#! /usr/bin/python
# _*_ coding:UTF-8 _*_

import worker_data
import tkinter
from tkinter import ttk  # 导入内部包

try:
    work_list = worker_data.work_list
except Exception:
    work_list = list()

order_str = ""
order = 2
name, identify, worker_id, index_info = "", "", "", ""


# 姓名合法检测
def name_check(checkName) -> object:
    if not checkName:
        return "输入姓名无效,请重新输入!"
    return ""


# 身份证合法检测
def identify_check(checkIdentify):
    identify_list = list()
    for temp_dict in work_list:
        identify_list.append(temp_dict['identify'])

    if checkIdentify in identify_list:
        return "员工身份信息重复，请重新输入"

    if len(checkIdentify) != 18 or not (checkIdentify.isalnum()):
        return "输入身份信息无效，请重新输入"
    return ""


# 职员id合法检测
def id_check(checkId):
    id_list = list()
    for temp_id in work_list:
        id_list.append(temp_id['id'])

    if checkId in id_list:
        return "员工ID信息重复,请重新输入!"

    if len(checkId) != 5 or not (checkId.isalnum()):
        return "员工ID应为五位数数字,请重新输入!"
    return ""


# 职员管理系统窗口
def gui_show(info_list=[], insert=False):
    root = tkinter.Tk()
    root.title("职员管理系统")

    root.geometry("700x500+300+100")  # 固定窗口显示位置
    global order_str, order

    def print_selection():
        global order, order_str, name, identify, worker_id, index_info
        name = en1.get()
        identify = en2.get()
        worker_id = en3.get()
        index_info = en4.get()

        order_str = listbox1.get(listbox1.curselection())
        order = order_str[0]
        # 关闭窗口，等待窗口刷新
        root.destroy()

        # 职员信息录入
        if order == "1":
            gui_show(work_list, insert=True)

        # 显示所有职员信息
        elif order == "2":
            gui_show(work_list)

        # 根据传入索引查询符合查询条件的职员信息
        elif order == "3":
            # 输入检索条件（支持姓名、身份证号、职员ID）
            input_str = index_info
            # 定义一个变量query_list用于存储查询的职员信息
            query_list = list()
            # 遍历每个员工信息
            for dict_info in work_list:
                # 遍历每个员工信息中的每项数据
                # value为项目对应的值；比如项目“姓名”对应值“张三”
                for value in dict_info.values():
                    # 通过传入的检索条件匹配各个项目中的值
                    if input_str in value:
                        # value匹配正确，将该职员信息dict_info添加到查询结果列表query_list中
                        query_list.append(dict_info)
                        break
            if not query_list:
                order_str = "职员管理系统暂未收录该职工信息"

            # 将查询到的职员信息输出
            gui_show(query_list)

        elif order == "4":
            # 输入要删除的职员id
            input_str = index_info
            # 判断输入的职员编号是否为5位
            if len(input_str) != 5:
                print("员工ID应为5位")
                return
            # 遍历每位员工信息
            for dict_info in work_list:
                if input_str == dict_info["id"]:
                    # 将员工信息修改后重新写入文件(保存在磁盘中)用于永久保存
                    # 移除该职员信息
                    work_list.remove(dict_info)
                    order_str = "已成功删除职员编号为 {} 的职员！".format(input_str)
                    with open("work_data.py", "w", encoding="utf8") as f:
                        f.write("work_list = " + str(work_list))
                        break
            else:
                order_str = "职员管理系统暂未收录该职工信息！"
            gui_show(work_list)
        # 退出系统或错误指令
        else:
            exit()

    lab_name = tkinter.Label(root, text="姓名", anchor='e', height=1)
    lab_name.place(x=10, y=20)
    en1 = tkinter.Entry(root, show=None)
    en1.place(x=10, y=40, width=190, height=25)

    lab_identify = tkinter.Label(root, text="身份证号", anchor='e', height=1)
    lab_identify.place(x=10, y=80)
    en2 = tkinter.Entry(root, show=None)
    en2.place(x=10, y=100, width=190, height=25)

    lab_id = tkinter.Label(root, text="职员ID", anchor='e')
    lab_id.place(x=10, y=140)
    en3 = tkinter.Entry(root, show=None)
    en3.place(x=10, y=160, width=190, height=25)

    var = tkinter.StringVar(value=order_str)
    lab_index = tkinter.Label(root, bg="#6666FF", textvariable=var, width=30, height=2)
    en4 = tkinter.Entry(root, show=None, bg="#00FF66")
    en4.place(x=450, y=100, width=200, height=30)

    columns = ("姓名", "身份证号", "职员ID")
    # 创建表格
    tree = ttk.Treeview(root, show="headings", columns=columns)

    box_var = tkinter.StringVar()
    box_var.set([
        "1 - 信息录入",
        "2 - 查看所以职员信息",
        "3 - 根据索引查看职员信息",
        "4 - 根据职员ID删除职员信息",
        "0 - 退出系统"
    ])

    # 指令与提示信息展示框
    var = tkinter.StringVar(value=order_str)
    lab1 = tkinter.Label(root, bg="#6666FF", textvariable=var, width=30, height=2)
    lab1.pack()

    if insert:
        # 信息录入-添加对录入信息的合规检测，并保留输入框数据
        lab_name['text'] += name_check(name)
        en1.insert("end", name)
        lab_identify['text'] += identify_check(identify)
        en2.insert("end", identify)
        lab_id['text'] += id_check(worker_id)
        en3.insert("end", worker_id)

        # 职员姓名录入检测，检测到非法输入会提示错误并要求重新输入
        if not (name_check(name) + identify_check(identify) + id_check(worker_id)):
            work_list.append({"name": name, "identify": identify, "id": worker_id})
            with open("worker_data.py", "w", encoding="utf8") as f:
                f.write("work_list = " + str(work_list))

    # 设置初始选中状态
    listbox1 = tkinter.Listbox(root, listvariable=box_var, width=25)
    listbox1.select_set(int(order) - 1)
    listbox1.pack()

    # 确认框
    bt2 = tkinter.Button(root, bg="#FF9900", text="Enter", command=print_selection,
                         activebackground="gray", width="10")
    bt2.pack()

    # 设置数据展示属性，作用：只是为了表格内容居中
    # 设置表头展示属性,作用:只是为了显示标题的名称
    tree.heading("姓名", text="姓名")
    tree.heading("身份证号", text="身份证号")
    tree.heading("职员ID", text="职员ID")

    for work_dict in info_list:
        tree.insert("", 0, values=(work_dict['name'], work_dict['identify'], work_dict['id']))
    tree.pack()

    root.mainloop()


if __name__ == '__main__':
    gui_show()
