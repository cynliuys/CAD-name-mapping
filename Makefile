CFLAGS = -g -O3 -Wall

cada039: main.o nameMap.o record.o write.o 
	g++ -o $@ main.o nameMap.o record.o write.o $(CFLAGS)

main.o: main.cpp
	g++ -c main.cpp $(CFLAGS)

nameMap.o: nameMap.cpp nameMap.h
	g++ -c nameMap.cpp $(CFLAGS)

record.o: record.cpp nameMap.h
	g++ -c record.cpp $(CFLAGS)

write.o: write.cpp nameMap.h
	g++ -c write.cpp $(CFLAGS)

clean:
	rm -f cada039 *.o
	
