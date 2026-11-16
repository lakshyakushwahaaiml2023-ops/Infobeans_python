#include <iostream>
using namespace std;

void toh(int tiles, char src, char aux, char dest) {
    if(tiles == 0) return;
    toh(tiles - 1, src, dest, aux);
    cout<<src<<"-->"<<dest<<endl;
    toh(tiles - 1, aux, src, dest);
}

int main() {
    toh(3, 'A', 'B', 'C');
}