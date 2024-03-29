#!/usr/bin/env python3
""" Getting the start index and the end index """
import typing
from typing import Tuple
from typing import Dict, Union, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returning a tuple of the start index and the end index """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    my_tuple = (start_index, end_index)
    return my_tuple


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
        """ Returning a page given the page and page_sizes """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        s_index, e_index = index_range(page, page_size)
        if s_index >= len(dataset):
            return []
        return self.dataset()[s_index:e_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """ Returning a page with given details (Hypermedia pagination) """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
                'page_size': len(dataset),
                'page': page,
                'data': dataset,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
