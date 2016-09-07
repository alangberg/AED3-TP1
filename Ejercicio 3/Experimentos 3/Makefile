CPP=g++
FLAGS= -std=c++11

tiempo: tiempo.cpp ej3.o
	$(CPP) $(FLAGS) -o $@ $< ej3.o

sol: sol.cpp ej3.o
	$(CPP) $(FLAGS) -o $@ $< ej3.o

%.o: %.CPP	
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm tiempo
	