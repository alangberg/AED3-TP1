CXX=g++
CXXFLAGS=-std=c++11

OBJS=exp_3.o
MAIN=exp_3

all: $(MAIN)

$(MAIN): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

exp_3.o: exp_3.cpp

clean:
	rm -f $(OBJS) $(MAIN) \
	rm - f exp_por_tesoros_mejor_caso.out exp_por_tesoros_peor_caso.out exp_por_tesoros_caso_random.out exp_por_mochila.out

new: clean all

tesoros:
	clear && \
	./exp_3 -t 2 10 20 0 41 60 100 exp_por_tesoros_mejor_caso.out && echo "Listo Mejor Caso" && \
	./exp_3 -t 2 10 20 0 0 20 100 exp_por_tesoros_peor_caso.out && echo "Listo Peor Caso" && \
	./exp_3 -t 2 10 20 0 0 60 100 exp_por_tesoros_caso_random.out && echo "Listo Caso Random" && \
	python graficar_tesoros.py exp_por_tesoros_mejor_caso.out exp_por_tesoros_peor_caso.out exp_por_tesoros_caso_random.out tesoros_grafico.eps

mochilas:
	clear && \
	./exp_3 -m 30 0 50 100 exp_por_mochila.out && echo "Listo" && \
	python graficar_mochilas.py exp_por_mochila.out mochilas_grafico.eps