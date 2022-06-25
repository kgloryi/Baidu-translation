import requests
import random
import json,os,time

class Translation():

    def __init__(self,API_Key,Secret_Key,API_IP):
        self.API_Key = API_Key
        self.Secret_Key = Secret_Key
        self.API_IP = API_IP
        
    def access_token(self):
        host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}".format(self.API_Key,self.Secret_Key)
        response = requests.get(host)
        return response.json()["access_token"] #获取接口需要的token

    def option(self):
        dictionary ={}
        while True:
            print("""
        Translation Function Configuration^^（翻译功能配置）

1.Material configuration（素材配置）
2.Language configuration（语言配置）
3.Load the translation（加载翻译）
4.back（返回）
        """)
            Chooseoption = input("please input use options:")
            if(Chooseoption == "1" or Chooseoption == "2" or Chooseoption == "3" or Chooseoption == "4"):
                if(Chooseoption == "1"):
                    while True:
                        print("\n")
                        m = input("你可以向我提供一段话，或者是一个文本文档，当然也可以是一组文本文档（你必须要向我提供一组文本文档的绝对路径，也可以是相对路径!）:")
                        if(os.path.isfile(m) or os.path.isdir(m)):
                            dictionary["Material"] = m
                            break
                        elif(m != ""):
                            dictionary["Material"] = m
                            break
                        else:
                            print("\n")
                            print("请确认输入,系统未找到文件或路径,请确认资源是否存在!")
                    os.system("CLS")
                elif(Chooseoption == "2"):
                    while True:
                        print("""
语种列表:https://ai.baidu.com/ai-doc/MT/4kqryjku9
""")
                        m = input("请输入被翻译的语种代码:")
                        k = input("请输入要翻译的语种代码:")
                        if(m != "" or k != ""):
                            dictionary["src"] = m
                            dictionary["dst"] = k
                            break
                        else:
                            print("请确认你的输入!")
                    os.system("CLS")
                elif(Chooseoption == "3"):
                    if(dictionary["Material"] != ""and dictionary["src"] != "" and dictionary["dst"] != ""):
                        access_token = self.access_token()
                        url = self.API_IP+access_token
                        headers = {'Content-Type': 'application/json'}
                        term_ids = ""
                        savadata = open(os.getcwd()+"\\data\\translationdatabase.txt","w+")
                        if(os.path.isfile(dictionary["Material"])):
                            datas = open(dictionary["Material"],"r+").read().strip().split("\n")
                            for x in datas:
                                payload = {'q': x, 'from': dictionary["src"], 'to': dictionary["dst"], 'termIds' : term_ids}
                                r = requests.post(url, params=payload, headers=headers)
                                result = r.json()
                                print("\n"+result["result"]["trans_result"][0]["src"]+"翻译=>"+result["result"]["trans_result"][0]["dst"])
                                savadata.write(result["result"]["trans_result"][0]["src"]+"翻译=>"+result["result"]["trans_result"][0]["dst"]+"\n")
                            print("\n"+"结果保存在了data/translationdatabase.txt目录里")
                            time.sleep(3)
                            savadata.close()
                            os.system("CLS")
                        elif(os.path.isdir(dictionary["Material"])):
                            datas = os.listdir(dictionary["Material"])
                            for x in range(len(datas)):
                                datas[x] = dictionary["Material"]+"\\"+datas[x]
                            for x in datas:
                                datass = open(x,"r+").read().strip().split("\n")
                                for t in datass:
                                    payload = {'q': t, 'from': dictionary["src"], 'to': dictionary["dst"], 'termIds' : term_ids}
                                    r = requests.post(url, params=payload, headers=headers)
                                    time.sleep(1)
                                    result = r.json()
                                    print("\n"+result["result"]["trans_result"][0]["src"]+"翻译=>"+result["result"]["trans_result"][0]["dst"])
                                    savadata.write(result["result"]["trans_result"][0]["src"]+"翻译=>"+result["result"]["trans_result"][0]["dst"]+"\n")
                            print("\n结果都保存在了data/translationdatabase.txt目录里")
                            time.sleep(3)
                            savadata.close()
                            os.system("CLS")
                        else:
                            payload = {'q': dictionary["Material"], 'from': dictionary["src"], 'to': dictionary["dst"], 'termIds' : term_ids}
                            r = requests.post(url, params=payload, headers=headers)
                            result = r.json()
                            print("\n"+result["result"]["trans_result"][0]["src"]+"翻译=>"+result["result"]["trans_result"][0]["dst"])
                            savadata.write(result["result"]["trans_result"][0]["src"]+"翻译=>"+result["result"]["trans_result"][0]["dst"]+"\n")
                            print("\n结果都保存在了data/translationdatabase.txt目录里")
                            time.sleep(3)
                            savadata.close()
                            os.system("CLS")
                    else:
                        print("Please configure the material first, then the language, and finally load the translation.（请先配置材料，再配置语言，最后加载翻译。）")
                        time.sleep(2)
                        os.system("CLS")
                elif(Chooseoption == "4"):
                    return "back"
            else:
                print("\n")
                print("Please configure the material first, then the language, and finally load the translation.（请先配置材料，再配置语言，最后加载翻译。）")
                time.sleep(2)
                os.system("CLS")
    def main(self):
        userchoose = self.option()
        return userchoose
