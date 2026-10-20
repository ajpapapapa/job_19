import requests

r = requests.get('https://job.incruit.com/jobdb_list/searchjob.asp?rgn2=13&rgn2=11')
print(r.status_code)

#request 요청인데 위의 사이트가서 get 했다. 