from group_by_category import group_by_category

def main():
    testing_list = [
                        {"name": "Apple", "category": "Fruit"},
                        {"name": "Carrot", "category": "Vegetable"},
                        {"name": "Banana", "category": "Fruit"}
                    ]

    print(group_by_category(testing_list))

main()