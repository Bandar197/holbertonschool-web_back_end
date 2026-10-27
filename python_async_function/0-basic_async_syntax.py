#!/usr/bin/env python3
"""This module uses asynchronous programming and random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """The function waits a random number of seconds."""
    bandar = random.uniform(0, max_delay)
    await asyncio.sleep(bandar)

    return bandar
