# ------------------------------------------------------------------------------
# main.py - содержит главную функцию,
# обеспечивающую простое тестирование
# ------------------------------------------------------------------------------


import sys
import time

from container.Container import Container


def err_message1():
    print("""incorrect command line!\n \
            Waited:\n \
                command -f infile outfile01 outfile02\n \
            Or:\n '
            command -n number outfile01 outfile02\n""")


def err_message2():
    print("""incorrect qualifier value!\n \
            Waited:\n \
               command -f infile outfile01 outfile02\n \
            Or:\n \
               command -n number outfile01 outfile02\n""")


def main():
    program_start = time.time()
    print(sys.argv)
    if len(sys.argv) not in [5, 4]:
        err_message1()
        return 1

    print("Start")
    c = Container()

    if sys.argv[1] == "-f":
        file = open(sys.argv[2], 'r')
        c.input_pl(file)
        file.close()
    elif sys.argv[1] == "-n":
        size = int(sys.argv[2])
        if size not in range(1, 10000):
            print("incorrect numer of figures = ", size, ". Set 0 < number <= 10000\n")
            return 3
        c.in_rnd_count(size)
    elif sys.argv[1] == "-r":
        c.in_rnd()
    else:
        err_message2()

    file_out_1 = open(sys.argv[3], 'w')
    print(file_out_1.name)
    file_out_1.write("Filled container:\n")
    c.out(file_out_1)
    file_out_1.write("\n-\n-\nTime for program without sort: ")
    file_out_1.write(str(time.time() - program_start))
    file_out_1.close()

    file_out_1 = open(sys.argv[4], 'w')
    print(file_out_1.name)
    program_start = time.time()
    c.shaker_sort()
    program_end = time.time()
    file_out_1.write("\n-\n-\nTime to make sort: ")
    file_out_1.write(str(program_end - program_start))
    c.out(file_out_1)
    file_out_1.close()

    print("finish")


if __name__ == '__main__':
    main()
