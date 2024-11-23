#ifndef ADVANCED_LENGHT_H
#define ADVANCED_LENGHT_H
using namespace std;

class Lenght
{
    bool operator==(const Lenght& other) const;
    strong_ordering operator<=>(const Lenght& other) const;

    Lenght operator+(const Lenght& other) const;
    Lenght operator+=(const Lenght& other);

    Lenght operator=(const Lenght& other);

    Lenght& operator++();
    Lenght operator++(int);

    operator int() const;

};
#endif