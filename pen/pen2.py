import requests

headers = {
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
}

class Pen():
    def __init__(self):
        self.res1 = requests.get('https://zuanbot.com/',headers=headers)
        self.cookies = self.res1.cookies
        
    def start(self, leven:int):
        """通过网络接口进行开喷
        args:
            leven: 喷的等级(1,2) 1是温柔模式
        """ 
        if leven == 1:
            res2 = requests.get('https://zuanbot.com/api.php?level=min&lang=zh_cn',headers=headers, cookies=self.cookies)
        else :
            res2 = requests.get('https://zuanbot.com/api.php?level=min&lang=zh_cn',headers=headers, cookies=self.cookies)
        if '2020 ' in res2.text:
            return ''
        return res2.text

if __name__ == '__main__':
    a = Pen()
    for i in range(100):
        x = a.start(0)        
        print(x)

