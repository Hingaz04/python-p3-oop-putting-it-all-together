#!/usr/bin/env python3


class Book:

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to a new instance.'''
        book = Book(title="And Then There Were None",
                    page_count=272)
        assert isinstance(book, Book)
