import re
import time
import json
import requests


headers = {
	"Host":"app.bilibili.com",
	"Accept":"*/*",
	"Connectiom":"keep-alive",
	"Cookie":"sid=8volmold",
	"Accept-Language":"zh-cn",
	"User-Agent":"bili-universal/6880 CFNetwork/902.2 Darwin/17.7.0",
	"Buvid":"515d8c137a45ff9e8f614a54d7df2958",
	"Accept-Encoding":"gzip"
}

url = "https://app.bilibili.com/x/v2/search?actionKey=appkey&appkey=27eb53fc9058f8c3&build=6880&device=phone&duration=0&from_source=apphistory_search&highlight=1&keyword=Python&mobi_app=iphone&order=default&platform=ios&pn={}&ps=20"

for i in range(1,2):
	requests_url = url.format(i)#构建rul
	time.sleep(1)#防止频率过高
	print("第{}页".format(i) + "\n")

	response = requests.get(url=requests_url,headers=headers)
	print("response.status_code : " + str(response.status_code))

	if response.status_code == 200:#判断是否得到返回
		print(response.content)
		print(response.text)
		datas = json.loads(response.content).get("data").get("item")
		if len(datas) == 0:#如果获取的数据中没有数据，结束
			break
		print("datas :" + str(datas))
		for data in datas:
			print("len(datas) : " + str(len(datas)))
			for i in range(0,len(datas)):
				# 增加一个异常处理，防止没有数据的时候程序出错停止
				try:
					herf = datas[i]['uri']
					title = datas[i]['title']
					views = datas[i]['play']
					author = datas[i]['author']
					#print("datas : " + str(datas))
					print('herf:' + herf)
					print('title:' + title)
					print('views:' + str(views))
					print('author:' + author)
				except :
					print("有异常-----------------------------------------------------------------------------")
