# coding: utf-8
from random import randint,choices,sample
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
st1=words.split('\n')
def poem():

    n=randint(5,10)
    
    for i in range(n):
        m=randint(3,6)
        sentence=sample(st1, m)
        print(" ".join(sentence))
poem()
