PYTHON_CMD := python3
SRC := $(wildcard *.pine)
DIST := $(patsubst %.pine,dist/%.pine,${SRC})

ALL: $(DIST)

dist/%.pine: %.pine
	mkdir -p dist
	$(PYTHON_CMD) generate.py $^ $@

clean:
	rm -f $(DIST)
