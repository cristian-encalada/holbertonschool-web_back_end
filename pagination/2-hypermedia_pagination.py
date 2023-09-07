#!/usr/bin/env python3
""" [1] Hypermedia pagination """
import csv
import math
from typing import List


def index_range(page, page_size):
    """ Return a tuple with start index and end indexes for pagination """
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return start_page, end_page


class Server:
    """Server class to paginate a database of popular baby names.
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
        """Retrieves a specific page from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        start, end = index_range(page, page_size)

        return data[start:end] if start < len(data) else []

    def get_hyper(self, page=1, page_size=10):
        """Function to handle hypermedia pagination
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        # calculate the total number of pages needed for pagination
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
