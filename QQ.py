import zipfile
import os
 

#################################################  可1個參數 or 2個參數
def Achive_Folder_To_ZIP(sFilePath, dest = ""):
    """
    input : Folder path and name
    output: using zipfile to ZIP folder
    """
    if (dest == ""):
        zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')
    else:
        zf = zipfile.ZipFile(dest, mode='w')
 

    os.chdir(sFilePath)

    #print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            #print aFile
            zf.write(aFile)
    zf.close()

    name = os.path.basename( sFilePath ) 

    # if (sFilePath)

    print("move "+PPCC+  "\\"+name+".zip  "+PP)
    os.system("move "+PPCC+  "\\"+name+".zip  "+PP)
 
 
if __name__ == "__main__":
    import os,sys 
    # os.chdir( os.path.dirname(sys.argv[0]) )
    ## .....................................
    if len(sys.argv)==2:
        ############################ .............................................
        # sFilePath = sFilePath.replace("/","\\")
        sFilePath  = sys.argv[1].replace("/","\\")
        if sFilePath[0] == "." and  len(sFilePath)==1:
            OK=True
        else:
            OK=False
        print(OK)

      

        ### 假設 只有.
        if len(sFilePath)==1 and (sFilePath[0] == "."):
            sFilePath = os.getcwd()


        if  sFilePath[len(sFilePath)-1] == "\\":
            os.system('mshta vbscript:msgbox("請刪除最後的斜線! not!!",64,"提示")(window.close)')
            os._exit(0)
        if  (sFilePath[0] == "."):
            ### 刪除一個  ../
            if  sFilePath.find("\\")!=-1:
                QQ=sFilePath.split("\\")
                QQ.pop(0)
                QQ="\\".join(QQ)
                ### 刪除二個  ../
                QQX=QQ
                if QQX.find("\\")!=-1:
                    QQ=QQX.split("\\")
                    QQ.pop(0)
                    QQ="\\".join(QQ)
                ### ................
                QQ="\\"+QQ
            else:
                QQ=""
                # print(QQ)
                # if os.path.basename(QQ).find(".") != -1:
                #     name = os.path.basename(QQ)
                #     QQ   = os.path.dirname(QQ)
            # if  sFilePath[len(sFilePath)-1] == "\\":
            #     os.system('mshta vbscript:msgbox("請刪除最後的斜線! not!!",64,"提示")(window.close)')
            #     os._exit(0)
                # QQA=QQ.split("\\")
                # QQA.pop(len(QQA)-1)
                # QQ="\\".join(QQA)
        else:
            QQ=""
        ############## .........................................................
        PP=os.getcwd() 
        ################################ 這邊只有處理一層  ../ 多層沒有
        if    (sFilePath[0] == "."):
            CC = os.getcwd()   ## 這個是執行的位置  不是檔案的位置 目錄路徑
            if ( len(sFilePath)>3 and sFilePath[1] == "."):  ## 表示2個點
                os.chdir("../")
                CC = os.getcwd()   ## 這個是執行的位置  不是檔案的位置 目錄路徑
                PPCC =  os.getcwd() 
                os.chdir(PP)
                if ( len(sFilePath)>6 and sFilePath[4] == "."):  ## 表示2個點
                    os.chdir("../")
                    os.chdir("../")
                    CC = os.getcwd()   ## 這個是執行的位置  不是檔案的位置 目錄路徑
                    PPCC =  os.getcwd() 
                    os.chdir(PP)
            else:
                PPCC =  PP

        elif  sFilePath.find(":")!=-1  :  ##and len(sFilePath) != sFilePath.find(":")+1:
            if sFilePath.split(":")[0].find("\\")==-1  and sFilePath.split(":")[0].find(".")==-1 and len(sFilePath.split(":")[0])==1: 
                CC =  sFilePath
                print(CC +" !+!")
                PPCC = os.path.dirname(CC)
                print(PPCC +" !+!")
                name = os.path.basename(CC)
                print(name +" !+!")
                   
            else:
                CC =""
            # ...............
            # PPCC =  PP  ###　會覆蓋Ｃ碟　#不建議
        else:
            ## 不是C: 也沒有.
            CC = PP+"\\"+sFilePath
            if CC[len(CC)-1]=="\\":
                CC=[i for i in CC if not i==len(CC)-1]
            # ...............
            PPCC =  PP
        ############ ..........................................................
        # print(os.getcwd())
        # print(CC+QQ)
        ############# .........................................................
        # ############ ..........................................................
        # print(os.getcwd())
        # print(CC+QQ)
        sFilePath = CC+QQ
        # input(sFilePath)

        if OK:
            XX = os.getcwd()
            PPCC = os.path.dirname(XX)
            name = os.path.basename(XX)
            sFilePath = XX

        QQAA = PP              ### 短
        print(QQAA+" !QQAA!")
        QQBB = sFilePath       ### 長
        print(QQBB+" !QQBB!")
        ########################## 短為主 當長低於短 會提示
        if QQAA.find(QQBB)==0:
            os.system('mshta vbscript:msgbox("請指定子目錄!!禁止使用上層 not!!",64,"提示")(window.close)')
            os._exit(0)


        print( sFilePath +"  !!!" )
        Achive_Folder_To_ZIP( sFilePath  )
        ############# ...............................................




    ## A
    # Achive_Folder_To_ZIP(r"C:\Users\moon\Desktop\BAT\BINLIB\專用ICO")
    ## B
    # Achive_Folder_To_ZIP(r"C:\Users\moon\Desktop\BAT\BINLIB\專用ICO", r"OK.zip")




    ### 自己壓縮自己 容量不對