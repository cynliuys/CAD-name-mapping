CFLAGS = -O3 -Wall
CFLAGS = -g -Wall

ec: main.o nameMap.o namePair.o name.o util.o
	g++ -o $@ main.o nameMap.o namePair.o name.o util.o $(CFLAGS) -std=c++11

main.o: main.cpp
	g++ -c main.cpp $(CFLAGS)

nameMap.o: nameMap.cpp nameMap.h
	g++ -c nameMap.cpp $(CFLAGS)

namePair.o: namePair.cpp namePair.h
	g++ -c namePair.cpp $(CFLAGS)

name.o: name.cpp name.h
	g++ -c name.cpp $(CFLAGS)

util.o: util.cpp util.h
	g++ -c util.cpp $(CFLAGS)


clean:
	rm -f ec *.o
	