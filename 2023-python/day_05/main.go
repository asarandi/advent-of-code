package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
	"sync"
)

func makeIntSlice(in string) (out []int) {
	for _, s := range strings.Fields(in) {
		n, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}
		out = append(out, n)
	}
	return
}

func convert(seed int, arr [][][]int) int {
	for _, cat := range arr {
		for _, rng := range cat {
			dest, src, num := rng[0], rng[1], rng[2]
			if src <= seed && seed < (src+num) {
				seed = dest + (seed - src)
				break
			}
		}
	}
	return seed
}

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	b = bytes.Trim(b, "\n")

	seeds := []int{}
	conv := [][][]int{}

	for i, spl := range strings.Split(string(b), "\n\n") {
		if i == 0 {
			seeds = makeIntSlice(spl[6:])
			continue
		}

		cat := [][]int{}
		for j, l := range strings.Split(spl, "\n") {
			if j != 0 {
				cat = append(cat, makeIntSlice(l))
			}
		}
		conv = append(conv, cat)
	}

	p1, p2 := math.MaxInt64, math.MaxInt64
	wg := &sync.WaitGroup{}

	for i := 0; i < len(seeds); i += 2 {
		p1 = min(p1, convert(seeds[i], conv))
		p1 = min(p1, convert(seeds[i+1], conv))

		wg.Add(1)
		go func(lo, hi int) {
			defer wg.Done()
			for ; lo < hi; lo++ {
				p2 = min(p2, convert(lo, conv))
			}
		}(seeds[i], seeds[i]+seeds[i+1])
	}
	wg.Wait()

	fmt.Println(p1, p2)
}
