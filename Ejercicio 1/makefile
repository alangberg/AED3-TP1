CC=gcc
CXX=g++
RM=rm -f
CPPFLAGS=-g $(shell root-config --cflags)
LDFLAGS=-g $(shell root-config --ldflags)
LDLIBS=$(shell root-config --libs)

SRCS=ej1.cc
OBJS=$(subst .cc,.o,$(SRCS))

all: tool

tool: $(OBJS)
    $(CXX) $(LDFLAGS) -o ej1 $(OBJS) $(LDLIBS) 

ej1.o: ej1.cc nodo.h

nodo.o: nodo.h

clean:
    $(RM) $(OBJS)

dist-clean: clean
    $(RM) tool