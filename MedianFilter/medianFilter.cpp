#include <stdio.h>
#include<iostream>
#include<fstream>
#include <algorithm>
#include <array>

using namespace std;


int main(){
    int shape[2];
    ifstream shapefile("shape_data.txt");

    if(!shapefile.is_open()){
        cout<<"Error opening file";
    }

    for(int i=0; i<2; i++){
        shapefile >> shape[i];
    }

    const int height = shape[0];
    const int width = shape[1];

    //int img[height][width];
    //array<array<int, width>, height> img;
    int img[height][width];
    
    ifstream inputfile("image1_data.txt");

    if(!inputfile.is_open()){
        cout<<"Error opening file";
    }

    for(int i=0; i<height; i++){
        for(int j=0; j<width; j++){
            inputfile >> img[i][j];
        }
    }

    clock_t start, end;
    start = clock();

    int window_size = 3;
    int temp[9];
    int temp_len = sizeof(temp) / sizeof(temp[0]);

    for(int i=0; i<height-window_size; i++){
        for(int j=0; j<width-window_size; j++){
        
            int k = 0;
            for(int x=0; x<window_size; x++){
                for(int y=0; y<window_size; y++){
                    temp[k+y] = img[i+x][j+y];
                }
                k += window_size;
            }

            sort(temp, temp+temp_len);
            int median = temp[8/2];
            img[i+1][j+1] = median;
            
            for(int t=0; t<9; t++){
                temp[t] = 0;
            }
        }
    }

    end = clock();
    float time = ((float) end-start)/CLOCKS_PER_SEC;
    printf("Sequential MedianFilter Execuition time: %0.8f milliseconds \n", time*1000.0);

    ofstream out("filtered_data.txt");
    
    for(int i=0; i<height;i++){
        for(int j=0; j<width;j++){
            out<<img[i][j]<<" ";
        }
        out<<endl;
    }

    return 0;
}