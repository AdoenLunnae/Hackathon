# !/usr/bin/env python
# -*- coding:utf-8 -*-


def is_date(date):
    lst = date.split('/')
    if lst.len() == 2:
        if lst[0].len <= 2 & lst[1].len <= 2:
            return lst[0].isdigit() & lst[1].isdigit()
