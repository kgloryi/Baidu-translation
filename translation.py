import os
from Switch import Switch

def option():
    while True:
        print("""
        Welcome to Baidu AI Translation^^（欢迎来到百度ai翻译）
        
1.Translation configuration（翻译配置）
2.Voice function（语音功能）
3.exit（退出）
    """)
        userchoose = input("please input use options:")
        if(userchoose == "1" or  userchoose == "2" or userchoose == "3"):
            if(userchoose == "3"):
                exit(0)
            else:
                return userchoose
        else:
            os.system("CLS")
            
def main():
    getoption = option()
    if(getoption == "1"):
        switch = Switch(getoption)
        os.system("CLS")
        if(switch.start()):
            os.system("CLS")
            main()
    elif(getoption == "2"):
        switch = Switch(getoption)
        os.system("CLS")
        if(switch.start()):
            os.system("CLS")
            main()
    else:
        exit(1)
if __name__ == "__main__":
    main()
