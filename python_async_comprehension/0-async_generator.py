#!/usr/bin/env python3
"""This module generates random numbers asynchronously."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield ten random numbers with a one-second delay each."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
