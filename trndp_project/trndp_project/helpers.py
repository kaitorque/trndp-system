import base64
import datetime
def encrypt(data):
    return str(base64.urlsafe_b64encode(data.encode("utf-8")), "utf-8")

def decrypt(data):
    return str(base64.urlsafe_b64decode(data), "utf-8")

def checkEmpty(input):
    error = []
    for x in input:
        if x.value ==  "":
            error.append(x.name+" cannot be empty.")
    return error

def checkDigit(input):
    error = []
    for x in input:
        try:
            int(x.value)
        except ValueError:
            error.append(x.name+" is not an integer.")
    return error

def dictfetchall(cursor):
    #"Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    #"Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    return data[0]

def cLink(n):
    n['link'] = encrypt("id="+str(n['id']))
    return n

def formatDate(n):
    n['format_date'] = "{:%d-%m-%Y %I:%M %p}".format(n['date'])
    return n
