#!/usr/bin/env python3
"""Module for simple_helper_function.py"""
import csv
import math
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page within the specified page size

        Args:
            page(int) to check
            page_size(int) to check

        Returns:
            a list
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        data: List = self.dataset()
        if start_idx > len(data):
            return[]

        return data[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves information about a page.
        """
        data = self.get_page(page, page_size)
        start_idx, end_idx = index_range(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)
        new_data = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end_idx < len(self.dataset()) else None,
            'prev_page': page - 1 if start_idx > 0 else None,
            'total_pages': total_pages
        }
        return new_data
