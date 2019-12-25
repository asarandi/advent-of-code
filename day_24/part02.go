/* advent of code 2019: day 24, part 1 */
package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "container/list"
)

const SIZE = 5
const BUG = '#'
const SPACE = '.'

type board [][]byte

func (b board) toString() string {
    var res string
    for i := 0; i < SIZE; i++ {
        res = res + string(b[i]) + "\n"
    }
    return res
}

func emptyBoard() board {
    res := board{}
    for i := 0; i < SIZE; i++ {
        res = append(res, make([]byte, SIZE))
        for j := 0; j < SIZE; j++ {
            res[i][j] = SPACE
        }
    }
    return res
}

func (bo *board) countBugs() int {
    b := *bo
    res := 0
    for i:=0; i<len(b); i++ {
        for j:=0; j<len(b[i]); j++ {
            if b[i][j] == BUG {
                res++
            }
        }
    }
    return res
}

func (bo *board) countAdjacent(parent, child board, i, j int) int {
    b := *bo
    if parent == nil { parent = emptyBoard() }
    if child == nil { child = emptyBoard() }
    res := 0
    if i == 0 && parent[1][2] == BUG { res++ }
    if j == 0 && parent[2][1] == BUG { res++ }
    if i == 4 && parent[3][2] == BUG { res++ }
    if j == 4 && parent[2][3] == BUG { res++ }
    if i == 1 && j == 2 { for k:=0; k<SIZE; k++ { if child[0][k] == BUG { res++ } } }
    if i == 2 && j == 1 { for k:=0; k<SIZE; k++ { if child[k][0] == BUG { res++ } } }
    if i == 2 && j == 3 { for k:=0; k<SIZE; k++ { if child[k][4] == BUG { res++ } } }
    if i == 3 && j == 2 { for k:=0; k<SIZE; k++ { if child[4][k] == BUG { res++ } } }
    if i > 0 && b[i-1][j] == BUG { res++ }
    if j > 0 && b[i][j-1] == BUG { res++ }
    if i+1 < SIZE && b[i+1][j] == BUG { res++ }
    if j+1 < SIZE && b[i][j+1] == BUG { res++ }
    return res
}

func (b board) age(parent, child board) board {
    res := emptyBoard()
    for i := 0; i < len(b); i++ {
        for j := 0; j < len(b[i]); j++ {
            if i == 2 && j == 2 {
                res[i][j] = '?'
                continue
            }
            count := b.countAdjacent(parent, child, i, j)
            if b[i][j] == BUG && count == 1 {
                res[i][j] = BUG
            }
            if b[i][j] == SPACE && (count == 1 || count == 2) {
                res[i][j] = BUG
            }
        }
    }
    return res
}

func fromString(s string) board {
    trim := strings.Trim(s, " \t\r\n\v\f")
    split := strings.Split(trim, "\n")
    data := make([][]byte, len(split))
    for i := range split {
        data[i] = make([]byte, len(split[i]))
        for j := range split[i] {
            data[i][j] = split[i][j]
        }
    }
    return data
}

func main() {
    content, err := ioutil.ReadFile("sample_01.txt")
    if err != nil {
        panic(err)
    }
    b := fromString(string(content))
    lst := list.New()
    lst.PushBack(b)

    for i:=0; i<10; i++ {
        res, j := 0, 0
        rep := list.New()
        rep.PushBack(emptyBoard())
        for e := lst.Front(); e != nil; e = e.Next() {
            var node, parent, child board
            node, parent, child = nil, nil, nil
            node = e.Value.(board)
            if e.Prev() != nil {
                parent = e.Prev().Value.(board)
            }
            if e.Next() != nil {
                child = e.Next().Value.(board)
            }
            k := node.age(parent, child)
            rep.PushBack(k)
            res += k.countBugs()
            fmt.Println("iteration", i, "item", j); j++
            fmt.Printf(k.toString())
            fmt.Println()
//            fmt.Println("lst.Len()", lst.Len(), "iteration", i, "res", res)
        }
        rep.PushBack(emptyBoard())
        lst = rep
    }
}
