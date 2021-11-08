//------------------------------------------------------------------------------
// main.cpp - содержит главную функцию, 
// обеспечивающую простое тестирование
//------------------------------------------------------------------------------

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cstring>

#include "Container/container.h"

void errMessage1() {
    cout << "incorrect command line!\n"
            "  Waited:\n"
            "     command -f infile outfile01 outfile02\n"
            "  Or:\n"
            "     command -n number outfile01 outfile02\n";
}

void errMessage2() {
    cout << "incorrect qualifier value!\n"
            "  Waited:\n"
            "     command -f infile outfile01 outfile02\n"
            "  Or:\n"
            "     command -n number outfile01 outfile02\n";
}

//------------------------------------------------------------------------------
int main(int argc, char* argv[]) {
    clock_t program_start = clock();
    if(argc != 5) {
        errMessage1();
        return 1;
    }

    cout << "Start"<< endl;
    Container c(10000);

    ////cout << "argv[1] = " << argv[1] << "\n";
    if(!strcmp(argv[1], "-f")) {
        ifstream ifst(argv[2]);
        c.In(ifst);
    }
    else if(!strcmp(argv[1], "-n")) {
        auto size = atoi(argv[2]);
        if((size < 1) || (size > 10000)) { 
            cout << "incorrect numer of figures = "
                 << size
                 << ". Set 0 < number <= 10000\n";
            return 3;
        }
        // системные часы в качестве инициализатора
        srand(static_cast<unsigned int>(time(0)));
        // Заполнение контейнера генератором случайных чисел
        c.InRnd(size);
    }
    else {
        errMessage2();
        return 2;
    }

    // Вывод содержимого контейнера в файл
    ofstream ofst1(argv[3]);
    ofst1 << "Filled container:\n";
    c.Out(ofst1);
    clock_t program_end = clock();
    ofst1 << "\n-\n-\nTime for program without sort: " << (double)(program_end - program_start) / CLOCKS_PER_SEC << " seconds\n-\n-\n";
    // The 2nd part of task
    ofstream ofst2(argv[4]);
    clock_t begin = clock();
    c.ShakerSort();
    clock_t end = clock();
    ofst2 << "\n-\n-\nTime to make sort: " << (double)(end - begin) / CLOCKS_PER_SEC << " seconds\n-\n-\n";
    c.Out(ofst2);

    cout << "Stop"<< endl;

    return 0;
}
