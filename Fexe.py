# wget ftp://192.168.0.1/test.txt 2>res.txt 1>&2


# wget https://vscode.cdn.azure.cn/stable/ff915844119ce9485abfe8aa9076ec76b5300ddd/VSCode-win32-x64-1.44.2.zip 2>VSCode-win32-x64-1.44.2.zip 1>&2




# wget https://vscode.cdn.azure.cn/stable/ff915844119ce9485abfe8aa9076ec76b5300ddd/VSCode-win32-x64-1.44.2.zip 2>VS.txt 1>&2


import os,sys
# print(sys.argv[0])
# print(len(sys.argv))
# ...................
if len(sys.argv)==2:  # 表示 有一個參數
    # print(sys.argv[1]+" 2>EXE.txt 1>&2")
    os.system(sys.argv[1]+" 2>EXE.txt 1>&2")
    # .......................
    # print(sys.path[0])
    # print(sys.argv[0])
    # .......................
    # os.chdir(sys.path[0])  ## 錯誤
    os.chdir(os.getcwd())   ## 這個是執行的位置  不是檔案的位置 目錄路徑
    # ......................
    f=open("EXE.txt","r")
    SS=f.readlines() # 陣列
    # print(type(SS))
    f.close()
    # .....................
    # print(len(SS))
    # ..........................................

    for i,b in enumerate(SS):
        # print(" # ")
        # print(b.find("'"+sys.argv[1]+"' 不是內部或外部命令、可執行的程式或批次檔。"))  # 建議從當行 第一個字元開始 判斷會==0
        # ..........................................
        if 0==b.find("'"+sys.argv[1]+"' 不是內部或外部命令、可執行的程式或批次檔。"):
            SS=False
        else:
            SS=True
        # if os.path.isfile("EXE.txt"):
        #     os.system("del EXE.txt")
        
    # ............. 初始化 ...........................
    # ................................................
    os.system("del EXE.txt")
    if os.path.isdir("True"):
        os.system("rmdir True")
    if os.path.isdir("False"):
        os.system("rmdir False")
    # ..............................................
      # ............ 初始化 ...........................

    
    # # wget 指令在 是產出一個空檔案
    if SS:
        # print("存在!!")
        os.system("mkdir True")
    else:
        os.system("mkdir False")
        os.system('mshta vbscript:msgbox("'+sys.argv[1]+'! not!!",64,"提示")(window.close)')
        os._exit(0)
        # print("not !!")
