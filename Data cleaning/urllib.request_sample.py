import urllib.request
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

url = 'http://fanyi.youdao.com'
response = urllib.request.urlopen(url)
print('response type: ', type(response))
print('response status code: ', response.getcode())
print('response encoding: ', response.getheader('Content-type'))
print('request url: ', response.geturl())
body = response.read().decode('utf-8')
print('response body: ', body)