# -*- coding: utf-8 -*-
# @Time    : 2021-03-21
# @Author  : yibo
# @FileName: zoomeye_get_url_without_api.py


import requests
from urllib.parse import quote


def main():
    # 要搜索的字段
    cookies_use = open('access_token.txt', 'r').read().strip(' ').strip('/n')
    cookies_use = str(cookies_use)
    if cookies_use:
        pass
    else:
        print('请将cookies填入accexx_token文件')
    # print(cookies_use)
    header_config = {
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept": "application / json, text / plain, * / *",
        "Accept - Encoding": "gzip, deflate",
        "Cube-Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImUxYjNmNTczM2M3MiIsImVtYWlsIjoiNDA5MTYyMDc1QHFxLmNvbSIsImV4cCI6MTYxNjM4MTMzOC4wfQ.mVRr7cIpUuTlE3dhd5QuMAmd8O6Z0AJdayijoJEGyMU",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        "Referer": "https: // www.zoomeye.org /",
        "Cookie": cookies_use
    }

    # 设置每页显示条数，默认为20,可以设置10，20，50
    page_size_config = 20

    search_key_input = input('[*] 请输入搜索词：')
    page_start = input('[*] 请输入起始页面：')
    page_stop = input('[*] 请输入截止页面：')
    search_key_encode = quote(search_key_input)
    print()

    # 存储文件
    doc_result = open('result.txt', 'a+')

    ii = 0  # 总数据量
    # 页码范围内抓取
    for page_num in range(int(page_start), int(page_stop) + 1):

        html = requests.get(
            url="https://www.zoomeye.org/search?q=" + search_key_encode + '&page=' + str(page_num) + '&pageSize=' + str(
                page_size_config), headers=header_config).json()

        # 抓取页内数据
        data_json = html['matches']
        data_limit = len(data_json)

        re_duplicates = set()
        # 去重

        for i in range(0, data_limit):

            ip = data_json[i]['ip']
            port = data_json[i]['portinfo']['port']
            service = data_json[i]['portinfo']['service']
            data_source = service + '://' + str(ip) + ':' + str(port)
            if data_source not in re_duplicates:
                re_duplicates.add(data_source)
                print('[+]' + data_source)
                doc_result.write(data_source + '\n')
                i += 1
            else:
                pass

        print()
        ii = ii + i
        print('[!] 第' + str(page_num) + '页抓取完毕  共抓取数据' + str(i) + '条\n')
        page_num += 1
    doc_result.close()
    print('-------抓取完毕------共抓取数据' + str(ii) + '条------' + '\n' * 2)


def logo():
    print(r'''
        __________                    ___________             
        \____    /____   ____   _____ \_   _____/__.__. ____  
          /     //  _ \ /  _ \ /     \ |    __)<   |  |/ __ \ 
         /     /(  <_> |  <_> )  Y Y  \|        \___  \  ___/ 
        /_______ \____/ \____/|__|_|  /_______  / ____|\___  >
                \/                  \/        \/\/         \/ 

    ''')


if __name__ == '__main__':
    logo()
    main()
