#include<stdio.h>
#include<CL/cl.h>
#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include <tuple>
#include<iostream>
#include <algorithm>
#include <array>

using namespace std;

int main(){

    const int height = 565;
    const int width = 848;
	const int window_size = 3;

	
    array<array<int, width>, height> img; //= {{{4,5,6,7},{0,1,2,3},{12,13,14,15},{8,9,10,11}}};
	
	
    ifstream inputfile("image1_data.txt");

    if(!inputfile.is_open()){
        cout<<"Error opening file";
    }

    for(int i=0; i<height; i++){
        for(int j=0; j<width; j++){
            inputfile >> img[i][j];
        }
    }
    
	

    cl_mem image_data_buffer;
	cl_uint platformCount; 
	cl_platform_id *platforms;
	clGetPlatformIDs(5, NULL, &platformCount); 


	platforms = (cl_platform_id*) malloc(sizeof(cl_platform_id) * platformCount);
	clGetPlatformIDs(platformCount, platforms, NULL); 
    

	cl_platform_id platform = platforms[0]; 
	
	char* Info = (char*)malloc(0x1000*sizeof(char));
	clGetPlatformInfo(platform, CL_PLATFORM_NAME      , 0x1000, Info, 0);
	printf("Name      : %s\n", Info);
	clGetPlatformInfo(platform, CL_PLATFORM_VENDOR    , 0x1000, Info, 0);
	printf("Vendor    : %s\n", Info);
	clGetPlatformInfo(platform, CL_PLATFORM_VERSION   , 0x1000, Info, 0);
	printf("Version   : %s\n", Info);
	clGetPlatformInfo(platform, CL_PLATFORM_PROFILE   , 0x1000, Info, 0);
	printf("Profile   : %s\n", Info);
	
	cl_device_id device; 
	cl_int err;
	
	err = clGetDeviceIDs(platform, CL_DEVICE_TYPE_GPU, 1, &device, NULL);
	if(err == CL_DEVICE_NOT_FOUND) {
		err = clGetDeviceIDs(platform, CL_DEVICE_TYPE_CPU, 1, &device, NULL);
	}
	printf("Device ID = %i\n",err);


	cl_context context; 
	context = clCreateContext(NULL, 1, &device, NULL, NULL, NULL);

	FILE *program_handle;
	program_handle = fopen("OpenCL/Kernel.cl", "r");

	size_t program_size;
	fseek(program_handle, 0, SEEK_END);
	program_size = ftell(program_handle);
	rewind(program_handle);

	char *program_buffer;
	program_buffer = (char*)malloc(program_size + 1);
	program_buffer[program_size] = '\0';
	fread(program_buffer, sizeof(char), program_size, program_handle);
	fclose(program_handle);	
	
	cl_program program = clCreateProgramWithSource(context, 1, (const char**)&program_buffer, &program_size, NULL); 
	
	cl_int err3= clBuildProgram(program, 0, NULL, NULL, NULL, NULL);
	printf("program ID = %i\n", err3);
	
	clock_t start, end;
    start = clock();

    cl_kernel kernel = clCreateKernel(program, "medianFilter", &err);

	cl_command_queue queue = clCreateCommandQueueWithProperties(context, device, 0, NULL);

	
	size_t global_size = width*height; //total number of work items
	size_t local_size = width; //Size of each work group
	cl_int num_groups = global_size/local_size; //number of work groups needed
	
	image_data_buffer = clCreateBuffer(context, CL_MEM_READ_WRITE | CL_MEM_COPY_HOST_PTR, height*width*sizeof(int), img.data(), &err);

	clSetKernelArg(kernel, 0, sizeof(cl_mem), &image_data_buffer);

	
	
	cl_int err4 = clEnqueueNDRangeKernel(queue, kernel, 1, NULL, &global_size, &local_size, 0, NULL, NULL);
	

	printf("\nKernel check: %i \n",err4);
	
	err = clEnqueueReadBuffer(queue, image_data_buffer, CL_TRUE, 0, sizeof(img), img.data(), 0, NULL, NULL);
	
	clFinish(queue);

	end = clock();
    float time = ((float) end-start)/CLOCKS_PER_SEC;
    printf("OpenCL MedianFilter Execuition time: %0.8f milliseconds \n", time*1000.0);
	
	ofstream out("OpenCL_filtered_data.txt");
    
    for(int i=0; i<height;i++){
        for(int j=0; j<width;j++){
            out<<img[i][j]<<" ";
        }
        out<<endl;
    }
	
	clReleaseKernel(kernel);
	clReleaseMemObject(image_data_buffer);
	clReleaseCommandQueue(queue);
	clReleaseProgram(program);
	clReleaseContext(context);
    
    return 0;
}