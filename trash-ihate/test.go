package main

import "fmt"

func main() {
	arr := []int{1,1,1,3,3,4,3,2,4,2}
	hash := make(map[int]int)
	
	for i , n :=  range arr {
		if hash[n] {
			return false
		}
		hash[n] = n
	}

	fmt.Println(hash)
}