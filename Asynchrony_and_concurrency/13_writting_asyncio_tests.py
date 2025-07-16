# we need to define test cases for the asyncio tasks
# @pytest.mark.asyncio decorator is used to mark the test function as an asyncio coroutine
# inside ,we can call and await the coroutine functions defined in the main code
# we can use pytest assert to check the expected output of the tasks
# Testing protocols and network communication can be done using Asyncio streaming and mocking
# Test casses send data to the server, server, reads response and checks if the data is correct
# the server is closed after the test is done
# Tests fixtures are used to set up the environment for the tests
# pip install pytest
# pip install pytest-asyncio
# pytest-asyncio is a plugin for pytest that provides support for asyncio coroutines in tests
# pytest-asyncio allows us to write tests that use asyncio coroutines and event loops
# pytest-asyncio provides a marker to mark the test function as an asyncio coroutine
# pytest-asyncio also provides a fixture to get the event loop for the test function
import asyncio
import pytest


# ------------------------------------------------------------------------------
# Async function simulating a network call or I/O-bound operation.
# In real applications, this could be an API request, database fetch, etc.
# ------------------------------------------------------------------------------


async def fetch_data():
    """
    Simulate an asynchronous data-fetching operation.

    Returns:
        dict: Simulated response with data and status.
    """
    await asyncio.sleep(1)  # Simulate network delay
    return {"data": 123, "status": "success"}


# ------------------------------------------------------------------------------
# Unit test for the fetch_data coroutine using pytest-asyncio.
# ------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_data():
    """
    Test the fetch_data function to ensure it returns the expected result.

    This test uses pytest-asyncio to support asynchronous testing.
    """
    # Act
    result = await fetch_data()

    # Assert
    expected = {"data": 123, "status": "success"}
    assert result == expected, "Returned data does not match expected result"
