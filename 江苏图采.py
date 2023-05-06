# coding=gbk
# -*- coding:uft-8 -*-
# 江苏图采

import requests
import warnings
import os


def main():
    url = 'https://jstxcj.91job.org.cn/code/upload'
    headers = {'User-Agent': 'joke'}
    files = {'file': open('code.jpg', 'rb')}
    res = requests.post(url, headers=headers, files=files, verify=False, timeout=(20, 20)).text
    code = res[1: -1]
    print('扫码成功 >>>')
    print(code)
    print('-' * 30)
    url = 'https://jstxcj.91job.org.cn/code/decode'
    data = {
        'code': code,
        'open_id': 'oTL_q5Frr6j3DdyFkHxt2i9XWacc'
    }
    res = requests.post(url, headers=headers, data=data, verify=False, timeout=(20, 20)).text
    token = res[1: -1]
    print(token)
    print('-' * 30)
    headers['Authorization'] = f'Bearer {token}'
    url = 'https://jstxcj.91job.org.cn/v2/camera/upload'
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
    print('需要准备两张jpg图片 一张图采二维码 一张自己的照片')
    print('分别命名code.jpg和img.jpg并且放在本工具同级文件夹')
    print('作者njtech的(打call) B站UP主<掐住橙喵喵的头>')
    print('代码公开无需担心隐私 可以到B站找源码和实现原理')
    print('请勿乱传照片 有老师审核的 禁止用于非法用途 后果自负')
    print('仅允许个人学习测试使用 严禁用于盈利 后果自负')
    print('-' * 30)
    try:
        main()
    except Exception as e:
        print('程序发生错误 请检查配置并重试或联系作者: ', e)
    print('-' * 30)
    input('完成 >>>')
