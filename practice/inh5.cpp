// Online C++ compiler (editor)
// Write and run C++ online using this editor.

#include <iostream>
using namespace std;

class A {
    public:
    virtual void func() {
        cout<<"A method called";
        return;
    }
};

class B : public A {
    public:
    void func () override {
        cout<<"B method called";
        return;
    }
};

int main() {
    A* obj = new B();
    obj->func();
}