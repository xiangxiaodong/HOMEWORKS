import time
import requests
import BeautifulSoup

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

for i in range(1,51):#实际是1-50，取不到50
	#分析url，构造url
	request_url =  "http://search.bilibili.com/all?keyword=Python&page={}".format(i)
	time.sleep(1)
	print("第{}页".format(i) + "\n")

	response = requests.get(url=request_url,headers=headers)
	if response.status_code ==  200:#加判断
		html = response.text
		soup = BeautifulSoup(html,"lxml")

		#items = soup.find_all("li",)

