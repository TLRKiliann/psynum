#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests

payload = {'key1': 'value1', 'key2': 'value2'}
rg = requests.get('https://api.github.com/events', data=payload)
print("---GET URL :---")
print(rg.url)
print("---GET + Headers-Content-Type :---")
print(rg.headers['content-type'])
#print(rg.headers)
print("---Encoding :---")
print(rg.encoding)
#print(rg.text)
#print(rg.content)
#print(rg.json())
print("---Raw :---")
print(rg.raw)
print("---Requests GET :---")
print(rg)
print("---GET finished---")
print("-------------")

rp = requests.post('https://api.github.com/events/post', data={"key":"value"})
print(rp.url)
print(rp)
print(rp.headers['content-type'])
print("post finished")
print("-------------")

r = requests.put('https://api.github.com/events/put', data = {'key':'value'})
print(r.url)
print(r)
print(r.headers['content-type'])
print("put finished")
print("-------------")

rd = requests.delete('https://api.github.com/events/delete')
print(rd.url)
print(rd)
print(rd.headers['content-type'])
print("delete finished")
print("-------------")

rh = requests.head('https://api.github.com/events/get')
print(rh.url)
print(rh)
print(rh.headers['content-type'])
print("head finished")
print("-------------")

ro = requests.options('https://api.github.com/events/get')
print(ro.url)
print(ro)
print(ro.history)
print("options finished")
print("-------------")
