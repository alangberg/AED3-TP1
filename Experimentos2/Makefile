CPP=g++
FLAGS= -std=c++11

tiempo: tiempo.cpp ej2.o
	$(CPP) $(FLAGS) -o $@ $< ej2.o

sol: sol.cpp ej2.o
	$(CPP) $(FLAGS) -o $@ $< ej2.o

%.o: %.cpp
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm tiempo
