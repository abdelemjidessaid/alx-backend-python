#!/usr/bin/env python3
"""
    Module of measure_runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Function that measures the time of execution
    """
    start = time.time()
    t1 = asyncio.create_task(async_comprehension())
    t2 = asyncio.create_task(async_comprehension())
    t3 = asyncio.create_task(async_comprehension())
    t4 = asyncio.create_task(async_comprehension())

    await asyncio.gather(t1, t2, t3, t4)

    result = time.time() - start
    return result
