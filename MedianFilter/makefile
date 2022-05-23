median:
	g++ medianFilter.cpp -g -o bin/medianFilter.out

filter:
	bin/medianFilter.out

host:
	g++ host.cpp -g -o bin/host.out -lOpenCL

make para_filter:
	bin/host.out

pre:
	python3 preprocessing.py

post:
	python3 post_processing.py

speedup:
	python3 speedup.py

clean:
	 rm -rf bin/*
	 rm -rf data/image/*
	 rm -rf data/imageData/*
	 rm -rf data/shapeData/*