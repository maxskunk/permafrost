import os
import sqlite3
import urllib.request
from aiohttp import web


con = sqlite3.connect('permafrost_db.db')
c = con.cursor()

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


async def handle(request):
    name = request.match_info.get('name')
    text = "Hello, " + name
    return web.Response(text=text)


async def readTemp(request):
    # name = request.match_info.get('name')
    t = ('desired_temp',)
    c.execute('SELECT value FROM config WHERE key=?', t)
    test = str(c.fetchone()[0])
    return web.Response(text=test)
    c.close()


async def setTemp(request):
    temp = request.match_info.get('newTemp')
    t = (temp, 'desired_temp',)
    c.execute("UPDATE config SET value = ? WHERE key=?", t)
    con.commit()
    return web.Response(text=temp)
    c.close()


app = web.Application()
app.add_routes([web.get('/readTemp/', readTemp),
                web.get('/setTemp/{newTemp}', setTemp)])

web.run_app(app, port=2222)
