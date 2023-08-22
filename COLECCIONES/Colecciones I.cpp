#include <iostream>
using namespace std;
/*Escribir un programa que sume los valores que hay por encima de la diagonal principal de
una matriz de 4 por 4. Los valores se deben asignar aleatoriamente.*/ 

int numero_aleatorio(){
    return(int (-100 + rand()%201));
}

int main(){
    /*Generamos la matriz */
    int matriz[4][4];
    for(int i=0; i<=3;i++){
        for(int j=0; j<=3;j++){ 
            matriz[i][j]=numero_aleatorio();
        }
    }
    /*Sumamons los numeros por encima de la diagonal*/
    int suma=0;
    for(int i=0; i<=3;i++){
        for(int j=0; j<=3;j++){ 
            if(j>i){
                suma+=matriz[i][j];
            }
        }
    }
    /*Imprimimos la matriz y el resultado de la suma*/
    cout<<"La matriz generada es:"<<endl;
    for(int i=0; i<=3;i++){
        for(int j=0; j<=3;j++){ 
            cout<<"\t"<<matriz[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<"La suma de los valores que hay por encima de la diagonal principal de la matriz es: "<<suma<<endl;

}