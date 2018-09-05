import requests
from pyquery import PyQuery
file = open(r'/Python项目/爬去Github上的最火项目/github_project.txt', 'w', encoding='utf-8') 
def GetGitHub():
    url = "https://github.com/trending/python"
    r = requests.get(url)
    for i in PyQuery(r.content)(".repo-list>li"):
        repo_url = "https://github.com"+PyQuery(i).find(".mb-1 a").attr("href")
        name = PyQuery(i).find(".mb-1 a").text()
        star = PyQuery(i).find("a.mr-3").text()
        data = "项目："+name+' '"星星数："+star+' '"项目地址："+repo_url
        file.write(str(data) + '\n')
        print("项目："+name,"星星数："+star,"项目地址："+repo_url)

GetGitHub()