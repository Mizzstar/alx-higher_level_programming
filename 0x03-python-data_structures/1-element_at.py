#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrivr an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list[idx])
