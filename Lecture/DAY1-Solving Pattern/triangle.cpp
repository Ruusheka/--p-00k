#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int row=1;
    while(row<=n){

        //space
        int space = n-row;
        while(space){
            cout<<" ";
            space-=1;
        }
        //triangle1
        int j=1;
        while(j<=row){
            cout<<j;
            j+=1;
        }

        //triange2
        int start2=row-1;
        while(start2){
            cout<<start2;
            start2-=1;
        }

        cout<<endl;
        row+=1;

    }
}