def group_by_category(items: list[dict]) -> dict:
    return_dict = {}
    
    for entry in items:
        category = entry["category"]
        if category in return_dict.keys():
            return_dict[category].append(entry["name"])
        else:
            return_dict[category] = [entry["name"]]
    
    return return_dict