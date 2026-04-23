def group_by_category(items: list[dict]) -> dict:
    return_dict = {}
    
    for entry in items:
        name = entry["name"]
        category = entry["category"]
        if category in return_dict.keys():
            return_dict[category].append(name)
        else:
            return_dict[category] = [name]
    
    return return_dict