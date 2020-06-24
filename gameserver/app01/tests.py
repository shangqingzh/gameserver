from django.test import TestCase

# Create your tests here.

import requests, json




# post提交客户端号 分数
def postClientidScore(clientid,clientname, score):
    formdata = {
        "clientid": clientid,
        "clientname": clientname,
        "score": score
    }

    url = "http://127.0.0.1:8000/postPlayerScore"

    headers = {
        "User-Agent": ""}

    response = requests.post(url, data=formdata)
    # 如果是json文件可以直接显示
    if response.json()['status'] == 'ok':
        print('提交记录{}'.format(i), '客户端号{}  分数{}   提交成功'.format(clientid, score))
    else:
        print('提交记录{}'.format(i), '客户端号{}  分数{}   提交失败'.format(clientid, score))
    return '提交成功'



# 获取用户排名
def getListsort(clientid, start_rank, stop_rank):
    url = "http://127.0.0.1:8000/getPlayerSort?clientid={}&start_rank={}&stop_rank={}".format(clientid, start_rank, stop_rank)
    response = requests.get(url)
    print(response.json()['msg'])

    if int(start_rank) == int(stop_rank) == 0:
        for oneplaysort in response.json()['msg']['allplayersort']:
            #print(oneplaysort)
            print('排名{}  客户端名称:{}  分数{}'.format(oneplaysort['ranking'], oneplaysort['clientname'], oneplaysort['score']))

        oneself = response.json()['msg']['oneplayersort'][0]
        print('本人排名{}  客户端名称:{}  分数{}'.format(oneself['ranking'], oneself['clientname'], oneself['score']))

    if len(response.json()['msg']['allplayersort']) != 0:
        print('您查询的排名如下：')
        for oneplaysort in response.json()['msg']['inputplayersort']:

            print('排名{}  客户端名称:{}  分数{}'.format(oneplaysort['ranking'], oneplaysort['clientname'], oneplaysort['score']))





import random
if __name__ == "__main__":
    while True:
        print('=========请输入选项==========')
        print('1:手动提交分数', '2:随机提交分数')
        print('3:手动查询排行', '4:默认查询排行')
        print('5:查询指定名次')
        print('0:退出')
        choice = input("请输入选项:")
        if int(choice) == 1:
            clientid = input("请输入客户端号")
            score = input("请输入分数")
            if 1 < int(score) < 100000:
                print('提交成功')
                postClientidScore(clientid, '客户端{}'.format(clientid), score)
            else:
                print('分数不在正常范围内')

        if int(choice) == 2:
            # 生成随机客户端号  分数
            clientidlist = random.sample(range(1, 15), 10)
            scorelist = random.sample(range(1, 100000), 10)
            # 提交十次
            for i in range(1, 11):
                clientid = random.choice(clientidlist)
                score = random.choice(scorelist)
                postClientidScore(clientid, '客户端{}'.format(clientid), score)

        if int(choice) == 3:
            clientid = input("请输入个人客户端号")
            # 获取排行榜
            getListsort(clientid, 0, 0)

        if int(choice) == 4:
            # 获取排行榜
            getListsort(5, 0, 0)

        if int(choice) == 5:
            start_rank = input("请输入开始名次")
            stop_rank = input("请输入结束名次")
            if int(start_rank) < int(stop_rank):
                print('正在获取名次。。。')
                getListsort(5, int(start_rank), int(stop_rank))
            else:
                print('请输入正确名次')

        if int(choice) == 0:
            break







