import async_solipsism
import pytest
from aiohttp import web


@pytest.fixture
def loop(mocker):
    mocker.patch(
        "aiohttp.test_utils.get_port_socket",
        lambda host, port: async_solipsism.ListenSocket((host, port)),
    )
    as_loop = async_solipsism.EventLoop()
    yield as_loop
    as_loop.close()


async def test_integration(
    aiohttp_client,  # noqa: F811 # pylint: disable=redefined-outer-name
):
    app = web.Application()
    client = await aiohttp_client(app, server_kwargs={"port": 80})
    resp = await client.post("/hey", json={})
    assert resp.status == 404
