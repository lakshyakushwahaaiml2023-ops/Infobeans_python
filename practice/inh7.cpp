// Online C++ compiler (editor)
// Write and run C++ online using this editor.

#include <iostream>
using namespace std;

class A {
    public:
    A() {
        cout<<"A constructor called...\n";
    }
    virtual void func() {
        cout<<"A method called";
        return;
    }

    static void func2() {
        cout<<"A - Static Function Called\n";
    }
};

class B : public A {
    public:
    B() {
        cout<<"B constructor called\n";
    }
    void func () override {
        cout<<"B method called\n";
        return;
    }

    static void func2() {
        cout<<"B static method\n";
    }
};

int main() {
    A* obj = new B();
    obj->func();
    A::func2();
    B::func2();
}