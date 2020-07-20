def save_items_in_bag(items, bag_capacity):
    remaining_capacity = bag_capacity
    bag = []
    total_value = 0
    # Sort by value
    sorted_keys = {item["value"]:key for key,item in items.items()}
    
    # Save by capacity
    for key in sorted_keys.values():        
        if items[key]["weight"] <= remaining_capacity:
            bag.append(key)
            remaining_capacity = remaining_capacity - items[key]["weight"]
            total_value += items[key]["value"]
    return [bag, total_value]


if __name__ == "__main__":
    items = {
        "apple":{"weight":0.1, "value":5},
        "candy":{"weight":5, "value":1},
        "computer":{"weight":15, "value":555},
        "pen":{"weight":0.5, "value":350},
        "screen":{"weight":25, "value":15000},
        "tablet":{"weight":9, "value":15},
        "refrigerator":{"weight":30, "value":5000},
        "book":{"weight":8, "value":1340},
        "fan":{"weight":19, "value":1000},
    }
    bag_capacity = 25

    print(save_items_in_bag(items, bag_capacity))
    