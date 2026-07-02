from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    employee_ids = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    employee_ids.insert_at_end(101)
    employee_ids.insert_at_end(102)
    employee_ids.insert_at_end(103)
    employee_ids.insert_at_front(100)

    # 3) Display the list to verify insertion
    print("Employee roster:")
    employee_ids.display()

    # 4) Call recursive_sum and print the result
    print(f"Sum of all IDs: {employee_ids.recursive_sum()}")

    # 5) Call recursive_search with a target and print result
    target = 102
    found = employee_ids.recursive_search(target)
    print(f"Is ID {target} in the roster? {found}")

    not_found_target = 999
    not_found = employee_ids.recursive_search(not_found_target)
    print(f"Is ID {not_found_target} in the roster? {not_found}")

    # 6) Call recursive_reverse, then display the reversed list
    employee_ids.recursive_reverse()
    print("Reversed roster:")
    employee_ids.display()

#