import os,time
from aip import AipSpeech

class Voice():

    def __init__(self,APP_ID,API_KKY,SECRET_KEY):
        self.APP_ID = APP_ID
        self.API_KKY= API_KKY
        self.SECRET_KEY = SECRET_KEY

    def start(self):
        print("""
语种列表:https://ai.baidu.com/ai-doc/MT/4kqryjku9
""")
        voicetype = input("Please enter the voice generation type（请输入语音生成类型）:")
        client = AipSpeech(self.APP_ID, self.API_KKY, self.SECRET_KEY)
        dataread = open(os.getcwd()+"\\data\\translationdatabase.txt","r+").read().split("\n")
        for x in range(len(dataread)-1):
            fenge = dataread[x].split(">")[1] #翻译的结果
            result  = client.synthesis(fenge,voicetype, 1, {'vol': 5,})
            if not isinstance(result, dict): #开始分批生成语音
                with open(os.getcwd()+'/music/audio'+str(x)+'.mp3', 'wb') as f:
                    f.write(result)
            f.close()
        print("\nSpeech synthesis complete（语音合成完毕,请查看当前目录下的music目录）")
        time.sleep(3.5)
        return "back"
    def main(self):
        return self.start()
