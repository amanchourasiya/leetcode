package main

import (
	"fmt"
)

type Stack []string

func main() {
	res := BalanceBrackets("()(){}()")
	if res == true {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

	res = BalanceBrackets("()({}()")
	if res == true {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

	res = BalanceBrackets("()(){]()")
	if res == true {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

	res = BalanceBrackets("()()}{()")
	if res == true {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}

func BalanceBrackets(input string) bool {
	var stack Stack
	for _, bracket := range input {
		bracket := string(bracket)
		if bracket == "(" || bracket == "[" || bracket == "{" {
			stack.Push(bracket)
		} else {
			if stack.IsEmpty() {
				return false
			}
			prevBracket, _ := stack.Pop()
			if bracket == ")" && prevBracket != "(" {
				return false
			} else if bracket == "]" && prevBracket != "[" {
				return false
			} else if bracket == "}" && prevBracket != "{" {
				return false
			}
		}
	}

	if !stack.IsEmpty() {
		return false
	}

	return true

}

// IsEmpty return true if Stack is empty else returns false
func (s *Stack) IsEmpty() bool {
	if len(*s) == 0 {
		return true
	}
	return false
}

// Pop returns the element at TOS and other bool parameter as false if the stack was empty
func (s *Stack) Pop() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {

		index := len(*s) - 1
		element := (*s)[index]
		*s = (*s)[:index]
		return element, true
	}
}

// Push adds new element into the stack
func (s *Stack) Push(str string) {
	*s = append(*s, str)
}
