import time
import json
def xueshengkongzhitai():
    renshu=1
    filename="renshu.txt"
    with open(filename)as file_object:
        shezhirenshu=file_object.read()
        shezhirenshu=int(shezhirenshu)
        chengji={}
        while renshu<=shezhirenshu:
            name=input("请输入您的姓名  提示：本姓名将会录入成绩！")
            
            fenshu=0
            cishu=0
            print("即将开始考试")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            time.sleep(2)
            time_start=time.time()
            print("计时器已经启动。")
            filename="timu1.txt"
            with open(filename)as file_object:
                timu1=file_object.read()
            print("请阅读第一道题并完成选择！")
            print(timu1)
            zidaan1=input("请输入答案（例如A）")
            filename="daan1.txt"
            with open(filename)as file_object:
                daan1=file_object.read()
                if daan1==zidaan1:
                    fenshu+=20
            print()
            print()
            filename="timu2.txt"
            with open(filename)as file_object:
                timu2=file_object.read()
                print("请阅读第二道题并完成选择！")
                print(timu2)
            zidaan2=input("请输入答案（例如A）")
            filename="daan2.txt"
            with open(filename)as file_object:
                daan2=file_object.read()
                if daan2==zidaan2:
                    fenshu+=20
            print()
            print()
            filename="timu3.txt"
            with open(filename)as file_object:
                timu3=file_object.read()
                print("请阅读第三道题并完成选择！")
                print(timu3)
            zidaan3=input("请输入答案（例如A）")
            filename="daan3.txt"
            with open(filename)as file_object:
                daan3=file_object.read()
                if daan3==zidaan3:
                    fenshu+=20
            print()
            print()
            filename="timu4.txt"
            with open(filename)as file_object:
                timu4=file_object.read()
                print("请阅读第四道题并完成选择！")
                print(timu4)
            zidaan4=input("请输入答案（例如A）")
            filename="daan4.txt"
            with open(filename)as file_object:
                daan4=file_object.read()
                if daan4==zidaan4:
                    fenshu+=20
            print()
            print()
            filename="timu5.txt"
            with open(filename)as file_object:
                timu5=file_object.read()
                print("请阅读第二道题并完成选择！")
                print(timu5)
            zidaan5=input("请输入答案（例如A）")
            filename="daan5.txt"
            with open(filename)as file_object:
                daan5=file_object.read()
                if daan5==zidaan5:
                    fenshu+=20
                    
            time_end=time.time()
            print("恭喜你，全部作答完成，那么，你的分数是——")
            print(fenshu)
            fenshu=str(fenshu)
            chengji[name]=fenshu
            print(name,"以",fenshu,"的分数完成考试，数据已经上传至教师端")
            print('本次考试用时：（秒）',time_end-time_start)
            print("您的考试已完成，请勿关闭程序，请让下一位同学进行考试，10秒后进行下一场考试！！")
            print(chengji)
            time.sleep(10)
            while cishu<51:
                cishu+=1 
                print("")
            renshu+=1   
        print("所有人考试已经结束，请老师启动教师端查看分数！")
        filename="chengji.json"
        with open(filename,"w")as file_object:
            json.dump(chengji,file_object)      

print("欢迎进入学生端！请确认题目和答案已经录入完成，方可进行考试")
cishu=0
renshu=0
xueshengkongzhitai()
