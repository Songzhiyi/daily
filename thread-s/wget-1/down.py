#!/usr/bin/env python3
import sys
import ssl
import urllib.request


def report(count, blockSize, totalSize):
    '''下载进度显示'''
    downloadedSize = count * blockSize
    percent = int(downloadedSize * 100 / totalSize)
    sys.stdout.write(f"\rDownloaded: {downloadedSize} bytes, Total: {totalSize} bytes, {percent} % complete")
    sys.stdout.flush()


if __name__ == '__main__':
    # 不加这个的话可能会出现 SSL 验证错误
    ssl._create_default_https_context = ssl._create_unverified_context

    opener = urllib.request.build_opener()

    # 请求头
    opener.addheaders = [
        ('Host', 'upos-hz-mirrorks3.acgvideo.com'),
        ('Connection' ,'keep-alive'),
        ('Origin', 'https://www.bilibili.com'),
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'),
        ('Accept', '*/*'),
        ('Referer', 'https://www.bilibili.com/video/av14177279/?spm_id_from=333.9.technology_fun.13'),
        ('Accept-Encoding','gzip, deflate, sdch, br'),
        ('Accept-Language', 'zh-CN,zh;q=0.8'),
        ('Range','bytes=0-'),
    ]
    urllib.request.install_opener(opener)

    # 此处的 URL 就是 Firefox 开发者工具获取的视频请求的 URL，根据实际填写
    url = 'https://upos-hz-mirrorks3.acgvideo.com/upgcxcode/19/17/23141719/23141719-1-80.flv?e=ig8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNC8xNEVE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IMvXBvEuENvNCI'

    urllib.request.urlretrieve(url, filename='test.flv', reporthook=report)