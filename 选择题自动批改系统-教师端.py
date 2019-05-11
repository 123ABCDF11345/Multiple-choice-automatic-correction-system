#coding=utf-8
def jiaoshikongzhitai():
	shurutishi="按1进入题目修改，按2进入答案修改，按3显示分数，"
	shurutishi2="按4改密码，按5查看关于作者的信息"
	kongzhitaijianru=input(shurutishi+shurutishi2)
	kongzhitaijianru=int(kongzhitaijianru)
	if kongzhitaijianru==1:
		timu1=input("请输入第一个题目")
		filename="timu1.txt"
		with open(filename,"a")as file_object:
			file_object.write(timu1)
		timu2=input("请输入第二个题目")
		filename="timu2.txt"
		with open(filename,"a")as file_object:
			file_object.write(timu2)
		timu3=input("请输入第三个题目")
		filename="timu3.txt"
		with open(filename,"a")as file_object:
			file_object.write(timu3)
		timu4=input("请输入第四个题目")
		filename="timu4.txt"
		with open(filename,"a")as file_object:
			file_object.write(timu4)
		timu5=input("请输入第五个题目")
		filename="timu5.txt"
		with open(filename,"a")as file_object:
			file_object.write(timu5)
		print("已完成所有题目修改，已经进入主菜单。！！！现在不可以进行考试，答案还未录入！！！")
		jiaoshikongzhitai()
	elif kongzhitaijianru==2:
		daan1=input("请输入第一个题目的答案")
		filename="daan1.txt"
		with open(filename,"a")as file_object:
			file_object.write(daan1)
		daan2=input("请输入第2个题目的答案")
		filename="daan2.txt"
		with open(filename,"a")as file_object:
			file_object.write(daan2)
		daan3=input("请输入第3个题目的答案")
		filename="daan3.txt"
		with open(filename,"a")as file_object:
			file_object.write(daan3)
		daan4=input("请输入第4个题目的答案")
		filename="daan4.txt"
		with open(filename,"a")as file_object:
			file_object.write(daan4)
		daan5=input("请输入第5个题目的答案")
		filename="daan5.txt"
		with open(filename,"a")as file_object:
			file_object.write(daan5)
		print("所有答案已经录入完毕，可以进行考试。考试方法：关闭教师端，启动学生端 ")
		print("注意：不得删除同文件夹下的任何txt文件")
		print("作者友情提醒您：考试并不能反映一个学生的成绩水平，请勿擅作主张")
		print("即将返回主菜单")
		jiaoshikongzhitai()
	elif kongzhitaijianru==3:
		print("先行说明：本功能只有在已经进行过至少一次学生端考试时可以使用！")
		print("否则可能报错或者没有输出")
		filename='chengji.txt'
		with open(filename)as file_object:
			for line in file_object:
				print(line)
		print("输出完成！已经返回主菜单")
		jiaoshikongzhitai()
	elif kongzhitaijianru==4:
		zidingyimima=input("请输入您的新密码")
		filename="mima.txt"
		with open(filename,"w")as file_object:
			file_object.write(zidingyimima)
		print("密码更改完成，请牢记"+zidingyimima)
		jiaoshikongzhitai()
	elif kongzhitaijianru==5:
		print("本程序由汪俊择编写")
		print("隐私申明：本程序不会收集任何数据至网络。")
		print("本程序不会与其他程序（除记事本，学生端）进行主动访问")
		print("免责申明：本程序的建立初衷是搭建智能考试计划的一部分，如有人将")
		print("作其他用途，作者不负任何责任，一切责任由当事人自行承担")
		print("汪俊择保留对此程序及学生端程序的解释权和所有权")
		print("作者有权随时更改程序源码/停止公开源码/更新作者相关的申明")
		print("©版权所有，侵版必究  2019 汪俊择 123ABCDF11345")
		print("作者联系方式：邮箱2542594900@qq.com  GitHub：123ABCDF11345")
		print("即将返回主菜单")
		jiaoshikongzhitai()
	else:
		print("无效的指令")
		print("©版权所有，侵版必究  2019 汪俊择 123ABCDF11345")
		jiaoshikongzhitai()
print("本程序需要配合学生端使用！")
print("本程序需要在源码所在的目录创建一个叫“mima.txt”的文件方可运行！")
print("强烈建议您使用GitHub上下载的文件，自动提供基本文件！")
filename="mima.txt"
with open(filename)as file_object:
	mima=file_object.read()
	print("给从GitHub下载的用户：初始密码为0000")
	jianrumima=input("请输入密码，密码长度1-8位，无密码回车进入系统  不知道密码？直接回车试试")
	jianrumima=int(jianrumima)
	mima=int(mima)
	if jianrumima==mima:
		jiaoshikongzhitai()
	else:
		print("密码错误")



#程序结束  ©版权所有，侵版必究  2019 汪俊择 123ABCDF11345

		




		


