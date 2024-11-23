#include "class.h"
#include <iostream>
using namespace std;

void Rectangle::draw(){
    cout << "Drawing a rectangle" << endl;
    cout << "Dimension" << width << ", " << height << endl;
}

void Rectangle::getArea(){
    return width * height;
}
 
// Changes in this compilation file extends to the other files connected to the main class
