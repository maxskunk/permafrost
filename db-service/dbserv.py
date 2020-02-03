import os
import sqlite3
import urllib.request
import aiohttp_cors
from aiohttp import web
import asyncio


con = sqlite3.connect('/home/pi/Cooler/permafrost_db.db')
c = con.cursor()

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


@asyncio.coroutine
def handler(request):
    return web.Response(
        text="Hello!",
        headers={
            "X-Custom-Server-Header": "Custom data",
        })


@asyncio.coroutine
def getTemp(request):
    t = ('desired_temp',)
    c.execute('SELECT value FROM config WHERE key=?', t)
    test = str(c.fetchone()[0])
    return web.Response(text=test)
    c.close()
    return web.Response(
        text=test,
        headers={
            "X-Custom-Server-Header": "Custom data",
            "Access-Control-Allow-Origin": "http://localhost:4200"
        })


@asyncio.coroutine
def getActualTemp(request):
    t = ('actual_temp',)
    c.execute('SELECT value FROM config WHERE key=?', t)
    test = str(c.fetchone()[0])
    return web.Response(text=test)
    c.close()
    return web.Response(
        text=test,
        headers={
            "X-Custom-Server-Header": "Custom data",
            "Access-Control-Allow-Origin": "http://localhost:4200"
        })


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
cors = aiohttp_cors.setup(app)


# app.add_routes([web.get('/readTemp/', readTemp),
#                 web.get('/setTemp/{newTemp}', setTemp)])

resource = cors.add(app.router.add_resource("/hello"))

route = cors.add(
    resource.add_route("GET", handler), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    })

resource = cors.add(app.router.add_resource("/getTemp"))
route = cors.add(
    resource.add_route("GET", getTemp), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    })
resource = cors.add(app.router.add_resource("/getActualTemp"))
route = cors.add(
    resource.add_route("GET", getActualTemp), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    })

resource = cors.add(app.router.add_resource("/setTemp/{newTemp}"))
route = cors.add(
    resource.add_route("GET", setTemp), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    })
# cors.add(route, {
#     "http://client.example.org":
#     aiohttp_cors.ResourceOptions(
#         expose_headers="*",
#         allow_headers="*"),
# })

web.run_app(app, port=2222)
