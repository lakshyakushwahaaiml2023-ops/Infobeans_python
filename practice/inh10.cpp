//Pure Virtual functions are functions that have no definition in the base class and must be implemented in derived classes. 
//They are declared by assigning 0 in the declaration. 
//A class that contains at least one pure virtual function is called an abstract class and cannot be instantiated. 
//Abstract classes are used to define interfaces in C++.

#include <iostream>
using namespace std;

class Shape {
    public:
    virtual void getArea() = 0;
};


class Circle : public Shape {
    public:
    void getArea() override {
        float radius;
        cout<<"Enter Radius: ";
        cin>>radius;
        cout<<"Area of the Circle: "<<radius * 3.14 * radius;
    }
};

class Rectangle : public Shape {
    public:
    void getArea() override {
        float l, w;
        cout<<"Enter length: ";
        cin>>l;
        cout<<"Enter width: ";
        cin>>w;
        cout<<"Area of the Rectangle: "<<l * w;
    }
};


int main() {
    Shape * c = new Circle();
    c->getArea();
    cout<<endl;
    c = new Rectangle();
    c->getArea();
}