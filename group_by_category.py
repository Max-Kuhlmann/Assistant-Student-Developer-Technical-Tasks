def group_by_category(items: list[dict]) -> dict:
    "Sorts list of dict objects by category key."
    return_dict = {}
    incorrect_dicts = 0

    for entry in items:
        try:
            name = entry["name"]
            category = entry["category"]
            """If statement executes if category is already represented
            and else executes if category is not yet in return_dict.
            """
            if category in return_dict.keys():
                return_dict[category].append(name)
            else:
                return_dict[category] = [name]
        except KeyError or UnboundLocalError:
            incorrect_dicts += 1
        
    
    if incorrect_dicts != 0:
        print(f"There was {incorrect_dicts} incorrectly formatted dict(s).")
    
    return return_dict