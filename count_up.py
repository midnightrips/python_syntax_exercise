def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    current_num = start
    print(current_num)
    while current_num != stop:
        current_num = current_num + 1
        print(current_num)

count_up(5, 7)        
