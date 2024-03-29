#!/usr/bin/env python3
""" Getting the start index and the end index """
import typing
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returning a tuple of the start index and the end index """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    my_tuple = (start_index, end_index)
    return my_tuple
