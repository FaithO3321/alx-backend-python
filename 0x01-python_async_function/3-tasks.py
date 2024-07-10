#!/usr/bin/env python3
"""Module for task_wait_random function."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task
    for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A Task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))