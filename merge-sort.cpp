#include <fstream>
#include <iostream>
#include <ctime>
#include <string>
#include <chrono>
#include <windows.h>
#include <iomanip>

template<typename T>
T* MergeSort(T* A, int n) {
    T* a[2] = { A , new T[n] };
    int c1 = 0; int c2 = 1; 
    int L = 1;
    int i, j, topL, topR, k;
    while (L < n) {
        c2 = c1; c1 = 1 - c1;
        k = 0;
        while (k < n) {
            i = k; j = k + L;
            topL = j; topR = j + L;
            if (topL > n) { topL = n; topR = 0; }
            else if (topR > n) { topR = n; }
            while (i < topL && j < topR) {
                if (a[c2][i] > a[c2][j]) {
                    a[c1][k] = a[c2][j]; ++j; ++k;
                }
                else {
                    a[c1][k] = a[c2][i]; ++i; ++k;
                }
            }
            if (i < topL) {
                while (i < topL) {
                    a[c1][k] = a[c2][i]; ++i; ++k;
                }
            }
            else if (j < topR){
                while (j < topR) {
                    a[c1][k] = a[c2][j]; ++j; ++k;
                }
            }
        }
        L *= 2;
    }
    delete[] a[c2];
    return a[c1];
}

void GenerateArray(double *A, int n, double lo = -100, double hi = 100) {
    for (int i = 0; i < n; ++i) {
        A[i] = lo + (double(rand()) / double(RAND_MAX)) * (hi - lo);
    }
}

long long MakeRun(int N) {

    double* A = new double[N];

    GenerateArray(A, N);

    auto begin = std::chrono::high_resolution_clock::now();
    A = MergeSort<double>(A, N);
    auto end = std::chrono::high_resolution_clock::now();

    //for (int i = 1; i < N; ++i) {
    //    std::cout << std::setprecision(17) << A[i] - A[i-1] << " ";
    //}
    //std::cout << std::endl;

    delete[] A;

    auto elapsed_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    return elapsed_ns.count();
}

void MakeTest(int N, std::ofstream &outfile) {
    int n = 3;
    for (int i = 0; i < N; ++i) {
        outfile << n << "/" << MakeRun(n) << " ";
        n *= 2;
    }
}


int main() {

    srand(time(NULL));

    for (int i = 0; i < 10; ++i) {
        std::ofstream outfile;
        outfile.open("out" + std::to_string(i) + ".txt");
        MakeTest(25, outfile);
        outfile.close();
    }

    return 0;
}