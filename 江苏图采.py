# coding=gbk
# -*- coding:uft-8 -*-
# 江苏图采

import requests
import warnings
import os


def main():
    url = 'https://jstxcj.91job.org.cn/v2/camera/upload'
    headers = {
        'Host': 'jstxcj.91job.org.cn',
        'Authorization': f'Bearer {tk}',
        'referer': 'https://servicewechat.com/wx9b3c613f1ddbf8c1/34/page-frame.html',
        'xweb_xhr': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6919',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'zh-CN,zh'
    }
    files = {'file': open('img.jpg', 'rb')}
    res = requests.post(url, headers=headers, files=files, verify=False, timeout=(20, 20)).text
    print('上传成功 >>>')
    print(res)
    print('-' * 30)
    url = 'https://jstxcj.91job.org.cn/v2/camera/crop'
    res = requests.get(url, headers=headers, verify=False, timeout=(20, 20)).text
    print('裁剪成功 >>>')
    print(res)


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    os.environ['NO_PROXY'] = 'jstxcj.91job.org.cn'
    print('-' * 30)
    print('需要准备两张jpg图片，一张图采二维码，一张自己的照片')
    print('分别命名code.jpg和img.jpg并且放在本工具同级文件夹')
    tk = input('请输入token(ey开头的，带三个点的jwt)并按回车: ')
    print('-' * 30)
    try:
        main()
    except Exception as e:
        print('error:', e)
    print('-' * 30)
    input('完成 >>>')
