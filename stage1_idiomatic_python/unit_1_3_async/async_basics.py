# Unit 1.3 — Async / asyncio
# Write your solution here.
import asyncio


async def fetch_simulated(url: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"response from {url}"


async def fetch_all(urls: list[str]) -> list[str]:
    tasks = [
        asyncio.create_task(
            fetch_simulated(url, 0.1)
        )
        for url in urls
    ]

    result = await asyncio.gather(*tasks)
    return result


async def main() -> None:
    urls = [
        "www.url_001.com",
        "www.url_002.com",
        "www.url_003.com",
        "www.url_004.com",
        "www.url_005.com",
        "www.url_006.com",
    ]
    print(await fetch_all(urls))


if __name__ == "__main__":
    asyncio.run(main())