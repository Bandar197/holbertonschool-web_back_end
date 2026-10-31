#!/usr/bin/env python3
"""Measure execution time for parallel asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Return the elapsed time for four concurrent comprehensions."""
    start = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start
