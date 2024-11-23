#include "class.h"
#include <iostream>
using namespace std;


int main ()
{
    Rectangle rectangle;
    rectangle.width = 10;
    rectangle.height = 10;
    cout << rectangle.getArea();

    return 0;
}