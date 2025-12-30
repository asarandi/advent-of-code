package main

import (
	"os"
	"regexp"
	"strconv"
	"strings"
)

type shape = [9]int
type region = [][]int

func canPlace(r region, s shape, y, x int) bool {
	for i := 0; i < 9; i++ {
		if s[i] == 1 && r[(i/3)+y][(i%3)+x] == 1 {
			return false
		}
	}
	return true
}

func place(r region, s shape, y, x, value int) {
	for i := 0; i < 9; i++ {
		if s[i] == 1 {
			r[(i/3)+y][(i%3)+x] = value
		}
	}
}

func rotate(in shape) (out shape) {
	for i, o := range []int{2, 5, 8, 1, 4, 7, 0, 3, 6} {
		out[o] = in[i]
	}
	return out
}

func makeShape(in string) (out shape) {
	for i, v := range strings.ReplaceAll(in, "\n", "") {
		if string(v) == "#" {
			out[i] = 1
		}
	}
	return out
}

func makeRegion(in string) (out region) {
	re := regexp.MustCompile(`(\d+)x(\d+)`)
	nums := re.FindStringSubmatch(in)
	w, _ := strconv.Atoi(nums[1])
	h, _ := strconv.Atoi(nums[2])

	out = make([][]int, h)
	for i := range out {
		out[i] = make([]int, w)
	}
	return out
}

func getCounts(in string) (out []int) {
	for _, s := range strings.Fields(in[1+strings.Index(in, ":"):]) {
		i, _ := strconv.Atoi(s)
		out = append(out, i)
	}
	return out
}

func getInput(f string) ([]shape, []region, [][]int) {
	data, _ := os.ReadFile(f)
	split := strings.Split(string(data), "\n\n")
	shp, rgn := split[:len(split)-1], split[len(split)-1]
	shapes, regions, counts := []shape{}, []region{}, [][]int{}
	for _, v := range shp {
		shapes = append(shapes, makeShape(v[2:]))
	}
	for v := range strings.Lines(rgn) {
		regions = append(regions, makeRegion(v))
		counts = append(counts, getCounts(v))
	}
	return shapes, regions, counts
}

func boolToInt(b bool) int {
	if b {
		return 1
	}
	return 0
}

func sumShape(s shape) int {
	n := 0
	for _, v := range s {
		n += v
	}
	return n
}

func canPlaceAll(shapes []shape, region region, counts []int) bool {
	h, w := len(region), len(region[0])
	n := 0
	for i, v := range counts {
		n += v * sumShape(shapes[i])
	}
	return n < h*w
}

func main() {
	shapes, regions, counts := getInput("input")
	n := 0
	for i, rgn := range regions {
		cnt := counts[i]
		n += boolToInt(canPlaceAll(shapes, rgn, cnt))
	}
	print(n)
}
