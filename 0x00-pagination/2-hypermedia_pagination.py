#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
     return a tuple of size two containing a start index
     and an end index corresponding to the range of indexes
     to return in a list for those particular pagination parameters
    """
    begin = (page - 1) * page_size
    end = page_size + begin
    return (begin, end)


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
        """
        takes two integer arguments page with default value 1
        and page_size with default value 10.
        """
        assert type(page_size) == int and type(page) == int
        assert page > 0 and page_size > 0
        begin, end = index_range(page, page_size)
        dataset = self.dataset()
        return [] if begin > len(dataset) else dataset[begin:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        """
        data = self.get_page(page, page_size)
        begin, end = index_range(page, page_size)
        next_page = page + 1 if end < len(self.__dataset) else None
        prev_page = page - 1 if begin > 0 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
