#!/usr/bin/env python3
"""
    Module of basic_async_syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Async Function that returns a random delay number
    """
    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)

    return time
