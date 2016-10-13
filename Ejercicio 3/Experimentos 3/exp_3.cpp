// g++ -std=c++11 exp_3.cpp -o exp_3 
#include <iostream>
#include <list>
#include <vector>
#include <sstream>
#include <fstream>
#include <time.h>
#include <chrono>

#define MOCHILA_1 0
#define MOCHILA_2 1
#define MOCHILA_3 2
#define CANT_MAX_MOCHILAS 3

using namespace std;
#define ya chrono::high_resolution_clock::now

template<typename S, typename T>
struct tupla{
    S primero;
    T segundo;
    tupla(S p, T s) : primero(p), segundo(s){}
};

template<typename S, typename T, typename U>
struct tripla{
    S primero;
    T segundo;
    U tercero;
    tripla(S p, T s, U u) : primero(p), segundo(s), tercero(u){}
};

typedef int*** matriz_3d;

typedef struct mochila_str{
    int capacidad;
    list<int> elementos;
} mochila;

typedef struct tesoro_str{
    int tipo;
    int peso;
    int valor;
} tesoro;

int indiceDelElementoMaximo(vector<int> opciones){
    // Requiere opciones != vacio
    // Devuelve el indice del elemento de mayor valor.
    // En caso de empate devuelve el menor de esos indices.
    int valor = opciones[0], res = 0;
    for(int i = 1; i < opciones.size(); ++i){
        if(valor < opciones[i]){
            valor = opciones[i];
            res = i;
        }
    }
    return res;
}

void imprimirSalida(int ganancia, mochila* ms, int cantMochilas){
    cout << ganancia << endl;
    for(int i = 0; i < cantMochilas; i++){
        int cantElementos = ms[i].elementos.size();
        // if(cantElementos == 0) continue; // si no tiene nada que siga con la otra mochila
        cout << cantElementos;
        for(list<int>::iterator it = ms[i].elementos.begin(); it != ms[i].elementos.end(); ++it)
            cout << " " << *it; 
        cout << endl;
    }
}

void leerEntrada(istream& is, mochila** mochilas, int& cantMochilas, tesoro** tesoros, int& cantTesoros){
    int cantTipoTesoros;
    cin >> cantMochilas >> cantTipoTesoros;

    *mochilas = new mochila[CANT_MAX_MOCHILAS];

    for(int i = 0; i < cantMochilas; i++)
        cin >> (*mochilas)[i].capacidad;
    // las mochilas restantes las llenamos con 0
    for(int i = cantMochilas; i < CANT_MAX_MOCHILAS; i++){
        (*mochilas)[i].capacidad = 0;
    }

    // Los elementos los ponemos en una lista porque a priori no sabemos cuantos van a ser
    // y necesitamos insertalos en O(1), el vector no lo garantizaba.
    list<tesoro> tesorosLista;
    for(int i = 0; i < cantTipoTesoros; i++){
        int cantTipoIEsimo, pesoTipoIEsimo, valorTipoIEsimo;
        cin >> cantTipoIEsimo >> pesoTipoIEsimo >> valorTipoIEsimo;
        for(int j = 0; j < cantTipoIEsimo; j++)
            tesorosLista.push_back((tesoro){i+1, pesoTipoIEsimo, valorTipoIEsimo});
    }

    // Ahora que ya sabemos cuantos elementos son los ponemos en un vector --> O(cantElem)
    cantTesoros = tesorosLista.size();
    *tesoros = new tesoro[cantTesoros];
    int i;
    list<tesoro>::iterator it;
    for(i = 0, it = tesorosLista.begin(); it != tesorosLista.end(); ++it, ++i){
        (*tesoros)[i].tipo = it->tipo; 
        (*tesoros)[i].peso = it->peso; 
        (*tesoros)[i].valor = it->valor;
    }
}

matriz_3d crearMatriz3D(int filas, int columnas, int profundidad){
    // requiere que todos los parametros sean > 0
    int*** m = new int**[filas];
    for(int i = 0; i < filas; i++){
        m[i] = new int*[columnas];
        for(int j = 0; j < columnas; j++){
            m[i][j] = new int[profundidad];
            for(int k = 0; k < profundidad; k++){
                m[i][j][k] = 0;
            }
        }
    }
    return m;
}

void copiarMatriz3D(matriz_3d& m1, matriz_3d& m2, int filas, int columnas, int profundidad){
    // A m1 le asigna m2: m1 <- m2
    for(int i = 0; i < filas; i++){
        for(int j = 0; j < columnas; j++){
            for(int k = 0; k < profundidad; k++){
                m1[i][j][k] = m2[i][j][k];
            }
        }
    }
}

void borrarMatriz3D(matriz_3d m, int filas, int columnas){
    for(int i = 0; i < filas; i++){
        for(int j = 0; j < columnas; j++){
            delete[] m[i][j];
        }
        delete[] m[i];
    }
    delete[] m;
}

int ej3(mochila* mochilas, int cantMochilas, tesoro* tesoros, int cantTesoros){

    int gananciaMaxima = 0;

    // Creamos un arreglo de matrices, una para cada elemento. Nos guardamos
    // un "historial" paso a paso de cada tesoro que fuimos agregando para 
    // reconstruir la solucion (saber que elementos pusimos en cada mochila).
    matriz_3d* matrices = new matriz_3d[cantTesoros+1]; // +1 para el 1er caso == ningun elemento
    for(int i = 0; i < cantTesoros+1; i++){
        matrices[i] = crearMatriz3D(mochilas[MOCHILA_1].capacidad+1, 
                                    mochilas[MOCHILA_2].capacidad+1, 
                                    mochilas[MOCHILA_3].capacidad+1);
    }

    // La matriz m de la iteracion k-esima guarda en la posicion m[i][j][k] la ganancia optima para las mochilas
    // de tamaño i, j y k simultaneamente habiendo recorrido los primeros k tesoros.
    // Notar que si por ejemplo la mochila 3 no venia en la entrada entonces el problema se reduce
    // a una matriz 2D (dimension = m1 x m2 x 1). Y si solo se recibe una mochila, el problema se 
    // reduce a un vector (dimension = m1 x 1 x 1).
    for(int i = 0; i < cantTesoros; i++){
        if(i != 0)
            copiarMatriz3D(matrices[i+1], matrices[i], 
                            mochilas[MOCHILA_1].capacidad+1, 
                            mochilas[MOCHILA_2].capacidad+1, 
                            mochilas[MOCHILA_3].capacidad+1);
        for(int m1 = mochilas[MOCHILA_1].capacidad; m1 >= 0; m1--){
            for(int m2 = mochilas[MOCHILA_2].capacidad; m2 >= 0; m2--){
                for(int m3 = mochilas[MOCHILA_3].capacidad; m3 >= 0; m3--){
                    vector<int> opciones;
                    opciones.push_back(matrices[i+1][m1][m2][m3]);
                    if (tesoros[i].peso <= m1)
                        opciones.push_back(matrices[i+1][m1-tesoros[i].peso][m2][m3]+tesoros[i].valor);
                    if (tesoros[i].peso <= m2)
                        opciones.push_back(matrices[i+1][m1][m2-tesoros[i].peso][m3]+tesoros[i].valor);
                    if (tesoros[i].peso <= m3)
                        opciones.push_back(matrices[i+1][m1][m2][m3-tesoros[i].peso]+tesoros[i].valor);
                    // el maximo de cada opcion da el optimo para cada iteracion
                    matrices[i+1][m1][m2][m3] = opciones[indiceDelElementoMaximo(opciones)];
                }
            }
        }
    }

    gananciaMaxima = matrices[cantTesoros]
            [mochilas[MOCHILA_1].capacidad][mochilas[MOCHILA_2].capacidad][mochilas[MOCHILA_3].capacidad];

    // Recorremos las matrices de cada paso para ver que tesoro pusimos en cada mochila
    int m1 = mochilas[MOCHILA_1].capacidad;
    int m2 = mochilas[MOCHILA_2].capacidad;
    int m3 = mochilas[MOCHILA_3].capacidad;
    for(int i = cantTesoros-1; i >= 0; i--){
        if(matrices[i][m1][m2][m3] != matrices[i+1][m1][m2][m3]){
            // => el tesoro i-esimo lo pusimos,
            // ahora nos fijamos en que mochila
            vector<int> opciones = {-1, -1, -1};
            if (tesoros[i].peso <= m1)
                opciones[MOCHILA_1] = matrices[i][m1-tesoros[i].peso][m2][m3];
            if (tesoros[i].peso <= m2)
                opciones[MOCHILA_2] = matrices[i][m1][m2-tesoros[i].peso][m3];
            if (tesoros[i].peso <= m3)
                opciones[MOCHILA_3] = matrices[i][m1][m2][m3-tesoros[i].peso];

            switch(indiceDelElementoMaximo(opciones)){
                case MOCHILA_1:
                    mochilas[MOCHILA_1].elementos.push_back(tesoros[i].tipo);
                    m1 -= tesoros[i].peso; 
                    break;
                case MOCHILA_2:
                    mochilas[MOCHILA_2].elementos.push_back(tesoros[i].tipo);
                    m2 -= tesoros[i].peso;
                    break;
                case MOCHILA_3:
                    mochilas[MOCHILA_3].elementos.push_back(tesoros[i].tipo);
                    m3 -= tesoros[i].peso;
                    break;
            }
        }
    }

    for(int i = 0; i < cantTesoros+1; i++)
        borrarMatriz3D(matrices[i], mochilas[MOCHILA_1].capacidad+1, mochilas[MOCHILA_2].capacidad+1);
    delete[] matrices;

    return gananciaMaxima;
}

string simularEntrada(vector<int> mochilas, vector< tripla<int, int, int> > tesoros){
    string res;
    res += to_string(mochilas.size()) + " " + to_string(tesoros.size()) + "\n";
    for(int i = 0; i < mochilas.size(); i++){
        if(i == 0)
            res += to_string(mochilas[i]);
        else
            res += " " + to_string(mochilas[i]);
    }
    res += "\n";
    for(int i = 0; i < tesoros.size(); i++)
        res += to_string(tesoros[i].primero) + " " + to_string(tesoros[i].segundo) + " " + to_string(tesoros[i].tercero) + "\n";
    return res;
}

#define MAX_CANTIDAD_TESOROS 50
#define MAX_CANTIDAD_PESO_M 50
// ./exp_3 <-t tesoros> <cantMochilas> <peso m1> <peso m2> <peso m3> <peso del min tesoro> <peso del max tesoro> <cantidad de repeiticiones> <archivo de salida>
//         <-m mochilas> <cantidad de tesoros> <peso del min tesoro> <peso del max tesoro> <cantidad de repeiticiones> <archivo de salida>
int main(int argc, char const *argv[]){

    vector< tupla<int, double> > mediciones;
    string path;

    if(string(argv[1])=="-t"){
        // Variando los tesoros
        int variaciones = MAX_CANTIDAD_TESOROS;
        int repeticiones = atoi(argv[8]);
        path = string(argv[9]);

        vector<int> mochilasIN;
        for(int i = 0; i < atoi(argv[2]); i++){
            mochilasIN.push_back(atoi(argv[3+i]));
        }
        
        vector< tripla<int, int, int> > tesorosIN;

        for(int i = 0; i < variaciones; i++){
            // cout << i << endl;
            int cantMochilas, cantTesoros;
            mochila* mochilas;
            tesoro* tesoros;

            int min = atoi(argv[6]);
            int max = atoi(argv[7]);
            int r = rand()%(max-min + 1) + min;
            tesorosIN.push_back(tripla<int,int,int>(1, r, 1));
            
            auto inicio_medicion = ya();
            for(int j = 0; j < repeticiones; j++){
                istringstream iss(simularEntrada(mochilasIN, tesorosIN));
                cin.rdbuf(iss.rdbuf());

                leerEntrada(cin, &mochilas, cantMochilas, &tesoros, cantTesoros);

                int ganancia = ej3(mochilas, cantMochilas, tesoros, cantTesoros);
                // imprimirSalida(ganancia, mochilas, cantMochilas);

                delete[] mochilas;
                delete[] tesoros;
            }
            auto fin_medicion = ya();
            tupla<int, double> t(i+1, (double) chrono::duration_cast<std::chrono::nanoseconds>(fin_medicion - inicio_medicion).count()/repeticiones);
            mediciones.push_back(t);
        }

    } else {
        // Variando la capacidad de la mochila
        // [2-12],[12-2],[4-6],[6-4],[3-8],[8-3]
        vector< tupla<int, int> > capacidades;
        capacidades.push_back(tupla<int, int>(2, 12));
        capacidades.push_back(tupla<int, int>(12, 2));
        capacidades.push_back(tupla<int, int>(4, 6));
        capacidades.push_back(tupla<int, int>(6, 4));
        capacidades.push_back(tupla<int, int>(3, 8));
        capacidades.push_back(tupla<int, int>(8, 3));

        int variaciones = capacidades.size(); 
        int repeticiones = atoi(argv[5]);
        path = string(argv[6]);

        vector<int> mochilasIN(2);
        vector< tripla<int, int, int> > tesorosIN;

        int min = atoi(argv[3]);
        int max = atoi(argv[4]);
        for(int i = 0; i < atoi(argv[2]); i++){
            int r = rand()%(max-min + 1) + min;
            tesorosIN.push_back(tripla<int,int,int>(1, r, 1));
        }

        for(int i = 0; i < variaciones; i++){
            // cout << i << endl;
            int cantMochilas, cantTesoros;
            mochila* mochilas;
            tesoro* tesoros;

            mochilasIN[0] = capacidades[i].primero;
            mochilasIN[1] = capacidades[i].segundo;

            auto inicio_medicion = ya();
            for(int j = 0; j < repeticiones; j++){
                istringstream iss(simularEntrada(mochilasIN, tesorosIN));
                cin.rdbuf(iss.rdbuf());

                leerEntrada(cin, &mochilas, cantMochilas, &tesoros, cantTesoros);

                int ganancia = ej3(mochilas, cantMochilas, tesoros, cantTesoros);
                // imprimirSalida(ganancia, mochilas, cantMochilas);

                delete[] mochilas;
                delete[] tesoros;
            }
            auto fin_medicion = ya();
            tupla<int, double> t(i+1, (double) chrono::duration_cast<std::chrono::nanoseconds>(fin_medicion - inicio_medicion).count()/repeticiones);
            mediciones.push_back(t);
        }
    }

    ofstream salida;
    salida.open(path.c_str());
    for(int i = 0; i < mediciones.size(); i++){
        salida << mediciones[i].primero << " "
            << mediciones[i].segundo << endl;
    }

    return 0;
}