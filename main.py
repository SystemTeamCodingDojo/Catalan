from file_io_tool import read_lists_from_file, write_list_to_file, char_list_to_int_list
import random


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


def generate_queue(n):
    if type(n) is not int or n < 0:
        return None

    queue = []
    nr_of_0s = 0
    nr_of_1s = 0

    def add(element):
        nonlocal nr_of_0s
        nonlocal nr_of_1s
        nonlocal queue
        queue.append(element)
        if 0 == element :
            nr_of_0s += 1
        else:
            nr_of_1s += 1

    random.seed()
    while nr_of_0s + nr_of_1s < 2*n:
        if nr_of_0s == nr_of_1s:
            add(0)
        elif nr_of_0s == n:
            add(1)
        else:
            if random.choice([0, 1]) == 0:
                add(0)
            else:
                add(1)
    
    return queue


def draw_island(island):
    picture = []
    level = 0
    space_cnt = 0
    for c in island:
        if '\\' == c :
            level -= 1
        if level > len(picture) - 1 :
            picture.append('')
        picture[level] += ((space_cnt - len(picture[level])) * ' ') + c
        if '/' == c:
            level += 1
        space_cnt += 1
    
    picture.reverse()
    for line in picture:
        print(line)
   

"""
Some explanation/hint for the solution
Lets name the number of islands C_0 if it is related to 0 unit wide island, C_1 for 1 unit wide, C_n the number of n unit wide, and so on...
On representative islend for C_5 can look like this:

                    /\ 
                   /  \  /\ 
                  /    \/  \ 
We can cut this here --><-- where it touches the sea level
So if we group all the 5 unit wide islands according to where the can be cut smaller islands, then
C_5 = sum(C_i * C_(4-i)) where i goes  from 0 to 4
"""
def number_of_islands(n):
    if 0 == n:
        return 1
    sum = 0
    for i in range (n):
        sum += number_of_islands(i) * number_of_islands(n-1-i)
    return sum


def main():
    for n in range(100):
        print(number_of_islands(n)) 

if __name__ == "__main__":
    main()