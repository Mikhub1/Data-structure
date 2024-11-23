#include <iostream>

using namespace std;

int main () 
{
    int numbers[] ={10,20,30,40};
    numbers[0]= 10;

    int second[size(numbers)];

    for (int number:numbers)
        cout << number << endl;

    

    cout << numbers[30];
}