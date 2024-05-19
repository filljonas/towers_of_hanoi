def f_rec(h, fr, to, aux):
    if h == 0:
        return []
    else:
        return f_rec(h - 1, fr, aux, to) + [(fr, to)] + f_rec(h - 1, aux, to, fr)


def f_it(h):
    moves = []
    # Initialize stacks
    A = list(range(1, h + 1))
    B = []
    C = []
    i = 0
    while len(C) < h:
        # Finding: given two stacks x and y, only one move (either x -> y or y -> x) is possible, but not both
        # Algorithm:
        #     Step 1: move between A and C, Step 2: move between A and B, Step 3: move between B and C (if h is uneven)
        #             move between A and B, Step 2: move between A and C, Step 3: move between B and C (if h is even)
        #     Repeat until stack C is full
        if (h % 2 == 1 and i % 3 == 0) or (h % 2 == 0 and i % 3 == 1):
            fr_list, fr_stack = A, 'A'
            to_list, to_stack = C, 'C'
        elif (h % 2 == 1 and i % 3 == 1) or (h % 2 == 0 and i % 3 == 0):
            fr_list, fr_stack = A, 'A'
            to_list, to_stack = B, 'B'
        else:
            fr_list, fr_stack = B, 'B'
            to_list, to_stack = C, 'C'
        if len(fr_list) > 0 and (len(to_list) == 0 or fr_list[-1] > to_list[-1]):
            last_elem = fr_list.pop()
            to_list.append(last_elem)
            moves.append((fr_stack, to_stack))
        else:
            last_elem = to_list.pop()
            fr_list.append(last_elem)
            moves.append((to_stack, fr_stack))
        i += 1
    return moves


if __name__ == '__main__':
    moves = f_rec(5, 'A', 'C', 'B')
    moves = f_it(5)
    for fr, to in moves:
        print(f'Slice from {fr} to {to}')
