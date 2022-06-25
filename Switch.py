from module.Translation_configuration import Translation
import os
from module.Voice_function import Voice

class Switch():

    def __init__(self,choose):
        self.choose = choose

    def option(self):
        print("""
        Baidu Key Configuration（百度机器翻译密钥配置）
""")
        API_Key = input("please input API_Key:")
        Secret_Key = input("please input Secret_Key:")
        API_IP = input("please input API_IP（机器翻译功能接口的域名）:")
        cache = open(os.getcwd()+"\\data\\machinecache.txt","w+")
        cache.write(API_Key+":"+Secret_Key+":"+API_IP)
        cache.close()
        return [API_Key,Secret_Key,API_IP]

    def checkcache(self):
        cache = open(os.getcwd()+"\\data\\machinecache.txt","r+",encoding="utf-8")
        duqucache = cache.read()
        cache.close()
        if(duqucache != ""):
            while True:
                checkuse = input("Whether to use the last Baidu AI configuration（是否使用上一次的百度ai配置）（Yes/No）:")
                if(checkuse == "Yes"):
                    fenge = duqucache.split(":")
                    return fenge
                elif(checkuse == "No"):
                    return "false"
                else:
                    os.system("CLS")
        else:
            return "false"

    def muscioption(self):
        print("""
        Baidu Key Configuration（百度语音合成密钥配置）
""")
        API_ID = input("please input API_ID:")
        API_Key = input("please input API_Key:")
        Secret_Key = input("please input Secret_Key:")
        cache = open(os.getcwd()+"\\data\\voicecache.txt","w+")
        cache.write(API_ID+":"+API_Key+":"+Secret_Key)
        cache.close()
        return [API_ID,API_Key,Secret_Key]
    
    def checkmusiccache(self):
        cache = open(os.getcwd()+"\\data\\voicecache.txt","r+",encoding="utf-8")
        duqucache = cache.read()
        cache.close()
        if(duqucache != ""):
            while True:
                checkuse = input("Whether to use the last Baidu AI configuration（是否使用上一次的百度ai配置）（Yes/No）:")
                if(checkuse == "Yes"):
                    fenge = duqucache.split(":")
                    return fenge
                elif(checkuse == "No"):
                    return "false"
                else:
                    os.system("CLS")
        else:
            return "false"
        
    def start(self):
        if(self.choose == "1"):
            checkhuoqu = self.checkcache()
            if(checkhuoqu == "false"):
                settingoption = self.option()
                translation = Translation(settingoption[0],settingoption[1],settingoption[2])
                os.system("CLS")
            else:
                settingoption = checkhuoqu
                os.system("CLS")
                translation = Translation(settingoption[0],settingoption[1],settingoption[2]+":"+settingoption[3])
            return translation.main()
        
        elif(self.choose == "2"):
            checkhuoqu = self.checkmusiccache()
            if(checkhuoqu == "false"):
                settingoption = self.muscioption()
                voice = Voice(settingoption[0],settingoption[1],settingoption[2])
                os.system("CLS")
            else:
                settingoption = checkhuoqu
                os.system("CLS")
                voice = Voice(settingoption[0],settingoption[1],settingoption[2])
            return voice.main()
        
        else:
            pass
