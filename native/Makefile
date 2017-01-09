CC	= /usr/bin/gcc
OBJ	= lib/knapsack.o lib/bind_solver.o
OBJDEBUG = lib/knapsack.o lib/test_knapsack.o
DEPENDFILE = .depend

SRC = $(OBJ:lib/%.o=src/%.cpp)
HDR = $(OBJ:lib/%.o=src/%.hpp)

LIBFLAGS = -shared
OBJFLAGS =

.PHONY: clean

main: $(OBJDEBUG)
	clang++ -stdlib=libc++ lib/knapsack.o lib/test_knapsack.o -o bin/knapsack_test

dep: $(SRC)
	$(CC) -MM $(SRC) > $(DEPENDFILE)
-include $(DEPENDFILE)

lib/%.o: src/%.cpp
	$(CC) -c $< -o $@ $(OBJFLAGS)

clean:
	rm -rf $(OBJ)