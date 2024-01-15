#!/usr/bin/env python3
"""
    Module of basic_async_syntax
"""

import asyncio
import random


async def wait_random(max_delay: float = 10):
    """
        Async Function that returns a random delay number
    """
    rn = random.uniform(0, max_delay)
    await asyncio.sleep(rn)

    return rn
