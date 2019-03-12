import re
import time
import requests

request_url = "https://search.bilibili.com/all?keyword=Python&from_source=banner_search&spm_id_from=333.334.banner_link.1&page={}"

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'finger=edc6ecda; buvid3=A3A829DB-C0C6-4A4F-B7D5-2BD1407EE7F06721infoc; LIVE_BUVID=AUTO5315316677538879; fts=1531668311; sid=i1gej45n',
	'Host': 'search.bilibili.com',
	'Referer': 'https://www.bilibili.com/',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

for i in range(1, 6):
	request_url = "https://search.bilibili.com/all?keyword=Python&page={}".format(i)
	print(request_url)
	time.sleep(1)
	print("第{}页".format(i) + "\n")

	response = requests.get(url=request_url, headers=headers)

	if response.status_code == 200:
		# html = response.content
		htmlText = response.text

		# 正则表达式
		str = '<li.*?video matrix.*?href="(.*?)".*?title="(.*?)".*?icon-playtime"></i>(.*?)</span>.*?icon-date"></i>(.*?)</span>.*?up-name">(.*?)</a>.*?</div>'
		#str = 'href="(.*?)"'
		pattern = re.compile(str,re.S)
		subjects = pattern.findall(htmlText)

		try:
			for sub in subjects:
				herf = sub[0].replace('//', '')  # 替换掉前面的//
				title = sub[1].strip()
				views = sub[2].strip()
				author = sub[3].strip()
				create_time = sub[4].strip()
				print(title, herf, views, author, create_time)
		except:
			print("有异常----------------------------")
