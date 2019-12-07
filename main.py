from file_io_tool import read_lists_from_file, write_list_to_file, char_list_to_int_list


def is_queue_correct(queue):

    if len(queue) % 2 != 0:
        return False
    else:
        max_nr_of_0s = len(queue) / 2
    nr_of_0s = 0
    
    for element in queue:
        if 0 == element:
            nr_of_0s += 1
        else:
            nr_of_0s -= 1
        
        if nr_of_0s < 0 or nr_of_0s > max_nr_of_0s:
            return False
    
    if nr_of_0s != 0:
        return False
    
    return True


def main():
    lots_of_queue = read_lists_from_file("input_ex1.txt")
    results = []
    for one_queue in lots_of_queue:
        results.append(is_queue_correct(list(map(int,one_queue))))
    write_list_to_file("output_ex1.txt", results)
    
if __name__ == "__main__":
    main()