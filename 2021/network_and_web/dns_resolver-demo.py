# coding=utf-8
# pip install dnsPython
import dns.resolver

domain = 'www.baidu.com'
A = dns.resolver.query(domain, 'A')
for answer in A.response.answer:
    for item in answer.items:
        print(item)
