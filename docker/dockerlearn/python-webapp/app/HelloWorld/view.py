# editing view.py file
from django.http import HttpResponse
from datetime import datetime
import os
import socket
import psycopg2

def home(request):
    pg_user = os.getenv('POSTGRES_USER')
    pg_pass = os.getenv('POSTGRES_PASSWORD')
    pg_db = os.getenv('POSTGRES_DB')
    pg_host = os.getenv('POSTGRES_HOST')
    conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pass)

    cur = conn.cursor()
    path = request.path
    client = get_client_ip(request)
    host = socket.gethostname()
    dt = datetime.utcnow().isoformat()
    sql = """INSERT INTO requests(requested_at, ip, host, path)
             VALUES(%s, %s, %s, %s);"""
    cur.execute(sql, (dt, client, host, path))
    conn.commit()
    cur.close()

    cur = conn.cursor()
    sql = 'SELECT requested_at, ip, host, path from requests ' + \
        'order by requested_at desc limit 25;'
    cur.execute(sql)

    entries = cur.fetchall()
    result = ""
    for entry in entries:
        result += "<span>path: " + entry[3] + "</span><br/>"
        result += "<span>client: " + entry[1] + "</span><br/>"
        result += "<span>host: " + entry[2] + "</span><br/>"
        result += "<span>datetime: " + entry[0] + "</span><br/>"
        result += "<br/>"


    cur.close()
    conn.commit()

    #entry = "<span>path: " + request.path + "</span><br/>" + \
    #    "<span>client: " + get_client_ip(request) + "</span><br/>" + \
    #    "<span>host: " + socket.gethostname() + "</span><br/>" + \
    #   "datetime: " + datetime.utcnow().isoformat() + "</span><br/>" + \
    #    "<br/>"

    #if not os.path.exists("/tmp"):
    #    os.makedirs("/tmp")

    conn.close()

    #append_copy = open(filename, "r")
    #original_text = append_copy.read()
    #append_copy.close()

    #full_text = entry + original_text

    #append_copy = open(filename, "w")
    #append_copy.write(full_text)
    #append_copy.close()

    #return HttpResponse(full_text)
    return HttpResponse(result)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip