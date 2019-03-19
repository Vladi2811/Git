#include <iostream>
#include <cstring>
#include <stdlib.h>
using namespace std;
void printCad(const char* cad){
    for(int i = 0; (*(cad+i)<122 && *(cad+i)> 65) || *(cad+i)==32; i++){
        cout << *(cad+i);
        
    }
    
    cout << endl;
}
int main() 
{   
    int* ptr = (int*) malloc(sizeof(int)*4);
    std::memset(ptr,0,4*4);
    *ptr = 20;
    *(ptr + 1) = 5;
    for(int i = 0; i < 4 ; i++){
        cout<<*(ptr+i) << " "; 
    }
    cout << endl;
    
    

    
    std::cin.get();
    return 0;
}