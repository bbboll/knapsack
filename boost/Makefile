CC	= /usr/bin/gcc
OBJ	= lib/knapsack.o lib/bind_solver.o
OBJDEBUG = lib/knapsack.o lib/test_knapsack.o
SHARED = bin/libknapsack.so
DEPENDFILE = .depend

SRC = $(OBJ:lib/%.o=src/%.cpp)
HDR = $(OBJ:lib/%.o=src/%.hpp)

LIBFLAGS = -shared -fPIC -lboost_python
OBJFLAGS = -fPIC -I /usr/include/python2.7/

PYTHONLIB = /usr/lib/python2.7

.PHONY: clean

debug: $(OBJDEBUG)
	clang++ -stdlib=libc++ lib/knapsack.o lib/test_knapsack.o -o bin/knapsack_test


test: $(OBJ)
	$(CC) -o $(SHARED) $(OBJ) $(LIBFLAGS)
	cp bin/libknapsack.so $(PYTHONLIB)/libknapsack.so

dep: $(SRC)
	$(CC) -MM $(SRC) > $(DEPENDFILE)
-include $(DEPENDFILE)

lib/%.o: src/%.cpp
	$(CC) -c $< -o $@ $(OBJFLAGS)

clean:
	rm -rf $(SHARED) $(OBJ) $(PYTHONLIB)/libknapsack.so