#include "iostream"
#include "algorithm"
#include "set"
#include "vector"
#include "fstream"
#include "sstream"
#include "queue"
#include <limits>

using namespace std;

template <typename T>
int find_zero(){
    T zero = 1;
    int p = 0;
    while(zero>0){
        zero /= 2;
        ++p;
    }
    return p+1;
}

template <typename T>
int find_inf(){
    T inf = 1;
    int p = 0;
    while(inf != std::numeric_limits<T>::infinity()){
        inf *= 2;
        ++p;
    }

    return p;
}

template <typename T>
T find_eps(){
    T eps = 1;
    T prev_eps = eps;
    int k = 0;
    while(eps+1 > 1){
        prev_eps = eps;
        eps /= 2;
        ++k;
    }
    return prev_eps;
}

int main(){
    cout << find_zero<float>() << "\n";
    cout << find_zero<double>() << "\n";
    cout << find_zero<long double>() << "\n";

    cout << "\n";

    cout << find_inf<float>() << "\n";
    cout << find_inf<double>() << "\n";
    cout << find_inf<long double>() << "\n";

    cout << "\n";

    cout << find_eps<float>() << "\n";
    cout << find_eps<double>() << "\n";
    cout << find_eps<long double>() << "\n";
    return 0;
}