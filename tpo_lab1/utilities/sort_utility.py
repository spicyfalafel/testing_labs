def is_sorted(lst):
    it = iter(lst)
    try:
        prev = next(it)
    except StopIteration:
        return True
    for x in it:
        if prev > x:  # For reverse, use <
            return False
        prev = x
    return True