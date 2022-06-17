#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import re

our_url = "https://getpocket.com/explore/item/a-simple-formula-for-changing-our-behavior?utm_source=pocket-newtab"


def get_html(elem, elem2, url):
    """
    Get the contents of an element from a given URL.
    :param elem: The element name to get.
    :param elem2: The element name to get (see below).
    :param url: The URL to get the element from.
    
    """
    text = urllib.request.urlopen(url)
    html = text.read().decode('utf-8')
    return re.findall('<{0}>(.+)<{1}>'.format(elem, elem2), html)


print(get_html('div class="facebook-share"', '/svg', our_url))