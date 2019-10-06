#!/usr/bin/env python3
# reverse a string python3
import timeit


time_this = """
def reverse(text):
# text: string to reverse
    if len(text) is 0:
        return ""
    else:
        return reverse(text[1:]) + text[0]
"""

times = timeit.repeat(stmt=time_this, number=1000000, repeat=5)
print([i/1000000 for i in times])
