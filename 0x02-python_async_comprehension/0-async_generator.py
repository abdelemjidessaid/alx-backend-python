#!/usr/bin/env python3
"""
    Module of async_generator
"""
import random
import asyncio


async def async_generator() -> None:
    """
        Function that every 1 second it yields a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
