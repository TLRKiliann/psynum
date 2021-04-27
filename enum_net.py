#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests


rg = requests.get('https://api.github.com/events')
print(rg.url)
print(rg)
print("get finished")
print("-------------")

rp = requests.post('https://httpbin.org/post', data={"key":"value"})
print(rp.url)
print(rp)
print("post finished")
print("-------------")

r = requests.put('https://httpbin.org/put', data = {'key':'value'})
print(r.url)
print(r)
print("put finished")
print("-------------")

rd = requests.delete('https://httpbin.org/delete')
print(rd.url)
print(rd)
print("delete finished")
print("-------------")

rh = requests.head('https://httpbin.org/get')
print(rh.url)
print(rh)
print("head finished")
print("-------------")

ro = requests.options('https://httpbin.org/get')
print(ro.url)
print(ro)
print("options finished")
print("-------------")
