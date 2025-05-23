from tkinter import *
import os
from tkinter import messagebox


win = Tk()
win.title("pyinstaller打包助手")
win.geometry("800x400+400+400")
win.minsize(800,400)

# 新建整型变量
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
# 设置三个复选框控件，使用variable参数来接收变量
check1 = Checkbutton(win, text="创建一个单独的可执行文件",font=('微软雅黑', 10,'bold'),variable = CheckVar1,onvalue=1,offvalue=0)
check2 = Checkbutton(win, text="不显示控制台窗口",font=('微软雅黑', 10,'bold'),variable = CheckVar2,onvalue=1,offvalue=0)
check3 = Checkbutton(win, text="指定可执行文件的图标",font=('微软雅黑', 10,'bold'),variable = CheckVar3,onvalue=1,offvalue=0)
check4 = Checkbutton(win, text="为文件添加信息",font=('微软雅黑', 10,'bold'),variable = CheckVar4,onvalue=1,offvalue=0)
#放置
check1.place(relx=0.02,rely=0.15)
check2.place(relx=0.02,rely=0.22)
check3.place(relx=0.02,rely=0.29)
check4.place(relx=0.02,rely=0.36)
# 定义执行函数
def xuan_ze():
    # 没有填写文件路径
    if len(e1.get()) == 0 or len(e1.get()) == 1 or len(e1.get()) == 2:
        messagebox.showinfo("错误", "文件路径错误")
    # 选择的情况下没有填写路径或路径字符少/错误
    else:
        if CheckVar3.get() == 1 and len(e2.get()) == 0 :
            messagebox.showinfo("错误","图标路径为空")
        elif CheckVar3.get() == 1 and len(e2.get()) == 1 :
            messagebox.showinfo("错误","图标路径错误")
        elif CheckVar3.get() == 1 and len(e2.get()) == 2 :
            messagebox.showinfo("错误","图标路径错误")
        elif CheckVar3.get() == 1 and len(e2.get()) == 3 :
            messagebox.showinfo("错误","图标路径错误")
        elif CheckVar4.get() == 1 and len(e3.get()) == 0 :
            messagebox.showinfo("错误","信息路径为空")
        elif CheckVar4.get() == 1 and len(e3.get()) == 1 :
            messagebox.showinfo("错误","信息路径错误")
        elif CheckVar4.get() == 1 and len(e3.get()) == 2 :
            messagebox.showinfo("错误","信息路径错误")
        elif CheckVar4.get() == 1 and len(e3.get()) == 3 :
            messagebox.showinfo("错误","信息路径错误")
        #都通过的情况下显示一个确认弹窗
        else:
            s1 = "创建一个单独的可执行文件" if CheckVar1.get() == 1 else ""
            s2 = "不显示控制台窗口" if CheckVar2.get() == 1 else ""
            s3 = "指定可执行文件的图标" if CheckVar3.get() == 1 else ""
            s4 = "为文件添加信息" if CheckVar4.get() == 1 else ""
            r = messagebox.askokcancel("确认", "您选择了%s %s %s %s\n是否开始打包\n打包过程中可能会有些卡，打包完成就没事了" % (s1, s2, s3, s4))
            #若选择确认
            if r:
                ok_da_bao()
            #若选择取消
            else:
                pass

#若已经选择好，开始打包
def ok_da_bao():
    # 获取用户输入
    file = e1.get()
    file_t = e2.get()
    file_x = e3.get()
    # 对用户输入进行处理
    parent_dir = os.path.dirname(file)   # 获取文件的父目录
    filename = os.path.basename(file)   #获取目录最后一级文件名
    #将命令与用户选项对应
    f1 = "-F" if CheckVar1.get() == 1 else ""
    f2 = "-w" if CheckVar2.get() == 1 else ""
    f3 = "-i" if CheckVar3.get() == 1 else ""
    f4 = "--version-file=" if CheckVar4.get() == 1 else ""
    #列出所有可能
    if CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 0:
        i = rf'pyinstaller "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 1 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f3} {file_t} "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 1 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f3} {file_t} "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1 and CheckVar3.get() == 0 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f2} "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1 and CheckVar3.get() == 0 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f2} "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f3} {file_t} {f2} "{filename}"'
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f3} {file_t} {f2} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 0 and CheckVar3.get() == 1 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f3} {file_t} {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 0 and CheckVar3.get() == 1 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f3} {file_t} {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 0 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f2} {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 0 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f2} {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 0:
        i = rf'pyinstaller {f3} {file_t} {f2} {f1} "{filename}"'
    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 1 and CheckVar4.get() == 1:
        i = rf'pyinstaller {f4}{file_x} {f3} {file_t} {f2} {f1} "{filename}"'
    # 开始执行
    messagebox.showinfo("打包","即将开始打包，可能会有些卡，打包完成就没事了")
    os.system(fr"cd /d {parent_dir} & {i}")
    var1.set(f"打包完成，输出目录{parent_dir}\\dist\\")

def pyinstaller_ok():
    # 判断是否安装pyinstaller
    f_ = 0
    result = os.popen(r'cd /d I:\tool\python\Python3.10.6-64\Scripts & pip list')
    res = result.read()
    for line in res.splitlines():
        if "pyinstaller" in line:
            f_ = 1
        else:
            pass
    if f_ == 1:
        var1.set("已安装pyinstaller，现在可以进行打包了")
    else:
        r = messagebox.askokcancel("错误","您未安装pyinstaller，\n本程序基于pyinstaller，\n是否安装pyinstaller")
        # 若选择确认
        if r:
            messagebox.showinfo("即将安装","安装过程中可能程序未响应\n安装完成就好了")
            os.system(r"cd /d I:\tool\python\Python3.10.6-64\Scripts & pip install pyinstaller")
            var1.set("安装完成，现在可以进行打包了")
        # 若选择取消
        else:
            messagebox.showinfo("很抱歉","本程序基于pyinstaller\n若无pyinstaller将无法正常运行")
            try:
                win.destroy()
                win.quit()
                win.quit()
                win.quit()
            except:
                pass


var1 = StringVar()
pyinstaller_ok()
#布置界面
e1 = Entry(win)
e1.place(relx=0.19,rely=0.05,relheight=0.07,relwidth=0.75)
e2 = Entry(win)
e2.place(relx=0.32,rely=0.29,relheight=0.07,relwidth=0.55)
e3 = Entry(win)
e3.place(relx=0.32,rely=0.36,relheight=0.07,relwidth=0.55)

l1 = Label(win,text="文件路径:",font=('微软雅黑', 15,'bold'))
l1.place(relx=0.02,rely=0.05,relheight=0.07,relwidth=0.15)
l2 = Label(win,text="图标路径:",font=('微软雅黑', 10,'bold'))
l2.place(relx=0.22,rely=0.29,relheight=0.07,relwidth=0.1)
l3 = Label(win,text="信息路径:",font=('微软雅黑', 10,'bold'))
l3.place(relx=0.22,rely=0.36,relheight=0.07,relwidth=0.1)

la = Label(win,textvariable = var1,font=('微软雅黑', 15,'bold'))
la.place(relx=0.05,rely=0.85,relheight=0.1,relwidth=0.8)
lb = Label(win,text="路径请不要加引号(\"\")",font=('微软雅黑', 15,'bold'))
lb.place(relx=0.05,rely=0.7,relheight=0.1,relwidth=0.8)

b1 = Button(win,text="选好了",bg='#BEBEBE',command=xuan_ze)
b1.place(relx=0.02,rely=0.43,relheight=0.07,relwidth=0.07)

win.mainloop()