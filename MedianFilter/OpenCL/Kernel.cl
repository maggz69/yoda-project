__kernel void medianFilter(
	__global int* img
	)

{	

	int i = get_global_id(0);
	int grp_id = get_group_id(0);
	int width = 848;
	int limit1 = (grp_id+1)*width-3;
	int limit2 = width*width - 2*width;
	int window_size = 3;
	int temp[9] = {};
	int len = sizeof(temp) / sizeof(temp[0]);

	if(i<=limit1 || i>=limit2){
		
		int k = 0;
		int j = 0;
		for(int x=0; x<window_size; x++){
			for(int y=0; y<window_size; y++){
				temp[k+y] = img[(i+j)+y];
			}
			k += window_size;
			j += width;
		}
		//sort temp
		for (int c = 0; c < 8; c++) {
        	int min = c;

			for (int t = c + 1; t < 9; t++) {
				if (temp[t] < temp[min]) {
					min = t;
				}
			}
			if (min != c) {
				int val = temp[min];
				temp[min] = temp[c];
				temp[c] = val;
			}
    	}
		//get median
		int median = temp[4];
		//change centre pixel in window to median value
		img[i+width+1] = median;
		
		for(int t=0; t<9; t++){
			temp[t] = 0;
		}

	}
	
}


