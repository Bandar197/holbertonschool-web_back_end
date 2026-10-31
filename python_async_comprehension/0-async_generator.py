#!/usr/bin/env python3
"""Provide an asynchronous generator of random floating-point values."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random values, waiting one second before each value."""
    generated = 0
    while generated < 10:
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        generated += 1
        yield number
