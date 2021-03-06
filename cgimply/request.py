"""
    Облегчение доступа к POST, GET данным запроса
"""


import cgi
from .env import ENV


# Данные, отправленные методом POST
post = cgi.FieldStorage()
POST = {name:post.getlist(name) for name in post.keys()}


# Данные, отправленные методом GET
GET = {}
for data in ENV["QUERY_STRING"].split("&"):
    name, value = data.split("=")
    if name not in GET:
        GET[name] = [value]
    else:
        GET[name].append(value)
