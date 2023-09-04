#!/usr/bin/env python3
""" [0] Simple helper function """


def index_range(page, page_size):
    """ Return a tuple with start index and end indexes for pagination """
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return start_page, end_page
