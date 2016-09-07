CPP=g++
FLAGS= -std=c++11

tiempo: tiempo_alternativo.cpp ej2_alternativo.o
	$(CPP) $(FLAGS) -o $@ $< ej2_alternativo.o

sol: sol.cpp ej2_alternativo.o
	$(CPP) $(FLAGS) -o $@ $< ej2_alternativo.o

%.o: %.cpp
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm tiempo
