CFLAGS = -O3 -march=native
all: build/rkpw_d build/rkpw_ld build/rkpw_q
build:
	mkdir -p build
build/rkpw_d: rkpw.c | build
	gcc $(CFLAGS) -o $@ rkpw.c -lm
build/rkpw_ld: rkpw.c | build
	gcc $(CFLAGS) -DLD -o $@ rkpw.c -lm
build/rkpw_q: rkpw.c | build
	gcc $(CFLAGS) -DQUAD -o $@ rkpw.c -lquadmath -lm
clean:
	rm -rf build
