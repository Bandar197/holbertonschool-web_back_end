#!/usr/bin/env python3
"""Create asynchronous tasks for random delays."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio task for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
