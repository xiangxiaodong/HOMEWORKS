import time
import requests
from bs4 import BeautifulSoup

#request_url = "https://search.bilibili.com/all?keyword=Python&from_source=banner_search&spm_id_from=333.334.banner_link.1&page={}"

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

for i in range(1, 51):  # 实际是1-50，取不到50
	# 分析url，构造url
	request_url = "http://search.bilibili.com/all?keyword=Python&page={}".format(i)  # 匹配{}里的数字
	time.sleep(1)
	print("第{}页".format(i) + "\n")

	response = requests.get(url=request_url, headers=headers)
	if response.status_code == 200:  # 加判断
		html = response.text
		soup = BeautifulSoup(html, "lxml")#需要先安装lxml解析库

		#print(soup.prettify())

		items = soup.find_all("li", {'class': 'video matrix'})  # 查找标签为li，且属性为video matrix的元素
		for item in items:
			href = item.find('a').get('href').replace('//','')
			title = item.find('a', {'class': 'title'}).get('title')
			views = item.find('span', {'class': 'so-icon watch-num'}).get_text().strip()  # 去掉空格
			create_time = item.find('span', {'class': 'so-icon time'}).get_text().strip()
			author = item.find('a', {'class': 'up-name'}).get_text()
			print(href, title, views, create_time, author)
