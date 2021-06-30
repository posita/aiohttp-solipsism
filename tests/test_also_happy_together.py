import asyncio

from aiohttp import web
from aiotools.timer import VirtualClock


async def hey(
    request: web.Request,  # pylint: disable=unused-argument
):
    await asyncio.sleep(5.0)
    return web.json_response({"you": "get off of my cloud"})


async def test_integration(aiohttp_client):
    app = web.Application()
    app.router.add_get("/hey", hey)
    vclock = VirtualClock()

    with vclock.patch_loop():
        client = await aiohttp_client(app)
        resp = await client.get("/hey")
        assert resp.status == 200
        resp_json = await resp.json()
        assert resp_json == {"you": "get off of my cloud"}
