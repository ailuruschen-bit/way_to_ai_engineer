import time

import pytest

from async_basics import fetch_all

urls = [
    "www.url_001.com",
    "www.url_002.com",
    "www.url_003.com",
    "www.url_004.com",
    "www.url_005.com",
    "www.url_006.com",
]


@pytest.mark.asyncio
async def test_fetch_all() -> None:
    start = time.perf_counter()
    result_list = await fetch_all(urls)
    elapsed = time.perf_counter() - start

    # test the result value and order
    assert result_list == [
        "response from www.url_001.com",
        "response from www.url_002.com",
        "response from www.url_003.com",
        "response from www.url_004.com",
        "response from www.url_005.com",
        "response from www.url_006.com",
    ]
    # test the elapsed time
    assert elapsed < 0.25