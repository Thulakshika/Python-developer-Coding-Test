## Ordering a list in the increasing number order
def sort_dict_by_values(d: dict):
    sort_items = sorted(d.items(), key=lambda x: x[1])
    sorted_dict = {name: number for name, number in sort_items}
    return sorted_dict

print(sort_dict_by_values({"a": 2, "b": 1, "c": 3}))