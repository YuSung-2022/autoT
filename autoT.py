import os.path
import shutil

src = ""
des = ""
with open("config.txt", encoding="utf-8") as f:
    for ln in f:
        s = ln.split('"')
        if s[0].find("src") != -1:
            src = s[1]
        elif s[0].find("des") != -1:
            des = s[1]
print(f"資源目錄：{src}")
print(f"目標目錄：{des}")

level = 0
loc = src
fix = []
his = []
select_point = []
while level >= 0:
    print('-----------------------------------------------')
    print(f"當前目錄為：{loc}")

    # 取得下層目錄
    dirs = os.listdir(loc)

    # 判斷是否位於最底層
    if(dirs[0].find(".json") != -1):
        
        # 已經在最底層，列出選單
        print(f" 0.回到上層")
        print(f" 1.選擇並回到上層")
        
        # 選擇
        print(f"請輸入相對應的代號： ")
        select = int(input())
        
        # 執行已選動作
        print(f"已選擇：{select}")
        if select == 0:
            level -= 1
            fix.pop()
            loc = src
            for i in fix:
                loc += '\\'
                loc += i
        elif select == 1:
            his.append(loc)
            for i in dirs:
                if i[-4:] != ".txt":
                    select_point.append(loc + "\\" + i)
            level -= 1
            fix.pop()
            loc = src
            for i in fix:
                loc += '\\'
                loc += i
        else:
            print("無效輸入，請重試")
    
    else:
        # 不在最底層，列出選單
        if level == 0:
            print(f" 0.結束並生成")
        else:
            print(f" 0.回到上層")
        index = 1
        for i in dirs:
            print(f"{index:>2}.{i}")
            index += 1

        # 選擇
        print(f"請輸入相對應的代號(0~{len(dirs)})： ")
        select = int(input())
        
        # 執行已選動作
        print(f"已選擇：{select}")
        if select == 0:
            level -= 1
            if fix != []:
                fix.pop()
            loc = src
            for i in fix:
                loc += '\\'
                loc += i
        elif select <= len(dirs):
            level += 1
            fix.append(dirs[select - 1])
            loc = src
            for i in fix:
                loc += '\\'
                loc += i
        else:
            print("無效輸入，請重試")
# print(his)
# print(select_point)

try:
    os.mkdir(des)
except FileExistsError:
    shutil.rmtree(des)
    os.mkdir(des)

index = 0
for p in select_point:
    index += 1
    shutil.copyfile(p, f"{des}/{index:04d}.json")
print(f"傳送文件已生成，共{index}個點")
input("結束")