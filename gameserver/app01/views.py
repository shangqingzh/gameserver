from django.shortcuts import render, HttpResponse
import json
from .models import PlayerScore
# Create your views here.


playerlist = []

# 上传客户端口号，玩家分数
def postPlayerScore(request):
    if request.method == "POST":
        clientid = request.POST.get("clientid")
        clientname = request.POST.get("clientname")
        score = request.POST.get("score")

        if clientid and score:
            if 1 < int(score) < 10000000:
                # 尝试根据客户端id查找，失败抛出异常，现在测试，改为注册
                try:
                    playerscore = PlayerScore.objects.get(clientid=clientid)
                    playerscore.score = score
                    playerscore.save()
                    return HttpResponse(json.dumps({'status': 'ok', 'msg': ''}),
                                        content_type="application/json")
                except:

                    playerscore = PlayerScore()
                    playerscore.clientid = clientid
                    playerscore.clientname = clientname
                    playerscore.score = score
                    playerscore.save()
                    return HttpResponse(json.dumps({'status': 'ok', 'msg': ''}),
                                        content_type="application/json")

    return HttpResponse(json.dumps({'status': 'error', 'msg': '请求方式错误'}),
                        content_type="application/json")


# 获取分数排行
def getPlayerSort(request):
    if request.method == "GET":
        requestid = request.GET.get("clientid")
        start_rank = request.GET.get("start_rank")
        stop_rank = request.GET.get("stop_rank")



        # 获取所有用户
        playerlist = PlayerScore.objects.all()
        playerlistsort = []
        for oneplayer in playerlist:
            oneplayermsg = {}
            oneplayermsg["clientid"] = oneplayer.clientid
            oneplayermsg["clientname"] = oneplayer.clientname
            oneplayermsg["score"] = oneplayer.score
            playerlistsort.append(oneplayermsg)

        # 所有用户根据分数排序
        playerlistsort = sorted(playerlistsort, key=lambda dict: dict["score"], reverse=True)

        oneplayersort = []
        inputplayersort = []
        # 将排名写入到用户字典内
        for oneplayer in playerlistsort:
            oneplayer['ranking'] = int(playerlistsort.index(oneplayer))+1

            # 查询个人的排名
            if int(oneplayer['clientid']) == int(requestid):
                oneplayermsg = {}
                oneplayermsg["clientid"] = oneplayer['clientid']
                oneplayermsg["clientname"] = oneplayer['clientname']
                oneplayermsg["score"] = oneplayer['score']
                oneplayermsg['ranking'] = int(playerlistsort.index(oneplayer)) + 1
                oneplayersort.append(oneplayermsg)



            if int(start_rank) != 0 and int(stop_rank) != 0:
                # 查询指定排名
                if int(start_rank) <= int(playerlistsort.index(oneplayer))+1 <= int(stop_rank):
                    oneplayermsg = {}
                    oneplayermsg["clientid"] = oneplayer['clientid']
                    oneplayermsg["clientname"] = oneplayer['clientname']
                    oneplayermsg["score"] = oneplayer['score']
                    oneplayermsg['ranking'] = int(playerlistsort.index(oneplayer)) + 1
                    inputplayersort.append(oneplayermsg)




        return HttpResponse(json.dumps({'status': 'ok', 'msg': {'allplayersort':playerlistsort, 'oneplayersort':oneplayersort, 'inputplayersort':inputplayersort}}),
                            content_type="application/json")





