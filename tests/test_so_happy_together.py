import async_solipsism
import pytest
from aiohttp import web


@pytest.fixture
def event_loop():
    loop = async_solipsism.EventLoop()
    yield loop
    loop.close()


@pytest.fixture
def fake_client(
    event_loop,  # noqa: F811 # pylint: disable=redefined-outer-name
    aiohttp_client,
):
    app = web.Application()
    return event_loop.run_until_complete(aiohttp_client(app))


async def test_integration(
    fake_client,  # noqa: F811 # pylint: disable=redefined-outer-name
):
    resp = await fake_client.post("/hey", json={})
    assert resp.status == 404
