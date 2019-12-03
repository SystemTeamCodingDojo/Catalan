def read_lists_from_file(file_name):
    with open(file_name) as source:
        source = open(file_name, "r")
    lines = source.readlines()
    data_list = []
    for line in lines:
        data_list.append(list(line[:-1]))
    return data_list


def write_list_to_file(file_name, data_list):
    if 0 == len(data_list):
        print("Empty list - no file has been written.")
        return
    
    simple_list = type( data_list[0] ) != type(list())
     
    with open(file_name, "w") as target:
        for line in data_list:
            if simple_list:
                target.write(str(line)+'\n')
            else:
                target.write(''.join(map(str, line))+'\n')
      

def main():


if __name__ == "__main__":
    main()