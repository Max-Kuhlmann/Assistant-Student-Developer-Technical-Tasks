from group_by_category import group_by_category

def main():
    testing_list_1 = [
                        {"name": "Apple", "category": "Fruit"},
                        {"name": "Carrot", "category": "Vegetable"},
                        {"name": "Banana", "category": "Fruit"}
                    ]
    testing_list_2 = [
                        {"eman": "Apple", "yrogetac": "Fruit"},
                        {},
                        {"name": "Banana", "category": "Fruit"}
                    ]

    print(group_by_category(testing_list_1))
    print(group_by_category(testing_list_2))

main()