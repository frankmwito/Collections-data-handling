# Flatten a Nested ist
"""Given nested_list = [1, [2, [3, 4], 5], 6], flatten it into [1, 2, 3, 4, 5, 6]."""

def flatten_list():
    """Recursively flattens a nested list."""
    nested_list = [1, [2, [3, 4], 5], 6]
    flat_list = []
    for item in nested_list:
        if item == int:
            flat_list.append(item)
        else:
            print("item is not an integer")
    return flat_list
if __name__ == "__main__":
    result = flatten_list()
    print(result)