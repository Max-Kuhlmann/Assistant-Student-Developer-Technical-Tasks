def group_by_category(items: list[dict]) -> dict:
    "Sorts list of dict objects by category key."
    return_dict = {}
    
    for entry in items:
        name = entry["name"]
        category = entry["category"]
        """If statement executes if category is already represented
        and else executes if category is not yet in return_dict.
        """
        if category in return_dict.keys():
            return_dict[category].append(name)
        else:
            return_dict[category] = [name]
    
    return return_dict