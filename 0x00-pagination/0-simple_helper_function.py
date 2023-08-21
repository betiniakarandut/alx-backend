#!/usr/bin/env python3
"""Module for simple_helper_function.py"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two

    Args:
        page(int) - page number
        page_size(int) - page size

    Returns:
        A tuple
    """
    end_index: int = 0
    for page_num in range(page):
        start_index: int = page_num * page_size
        end_index += page_size
    return(start_index, end_index)

# test
# res = index_range(1, 7)
# print(type(res))
# print(res)

# res = index_range(page=3, page_size=15)
# print(type(res))
# print(res)
