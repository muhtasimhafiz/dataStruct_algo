import re

precedance = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for i in expression:                        # loops through the expression

        if i.isdigit():                         # checks if i element of the expression is an integer or not, if integer it's pushed into the stack
            postfix += i
            continue

        if not stack:                           # checks if the stack is empty
            stack.append(i)
            continue

        if i == "(":                            # if ( then push into stack and continue the loop
            stack.append(i)
            continue

        if i == ")":                            # if i==) then top elements from the stack is removed and added to postfix variable until ( is popped

            while True:

                if not stack:
                    break

                if stack[-1] == "(":
                    stack.pop()
                    break

                postfix += stack.pop()
            continue
                                                        # python syntax a=[1,2,3], a[-1]=3, -1 index last element of the list/array
        pre_top_stack = precedance[
            stack[-1]]                                  # checks the operand(+-*/) then checks its power/precedance with the top element of the stack
        while precedance[
            i] <= pre_top_stack and pre_top_stack > 0:  # while power of the element is <= to the power/precedance of top element of the stack, remove top element of the stack and added to the posfix expression
            postfix += stack.pop()

            if not stack:
                break

            pre_top_stack = precedance[stack[-1]]

        stack.append(i)

    while stack:                                        # after the loop is completed if there is still elemnts in the stack then continue removing the top element of the stack and added to postfix expression
        postfix += stack.pop()

    return postfix


def string_reversal(expression):                        # reverses the string, for example: 1+2*3 becomes 3*2+1
    st = expression[::-1]

    st = st.replace('(', 'X')
    st = st.replace(')', '(')
    st = st.replace('X', ')')

    return st


def infix_prefix(
        expression):                                    # reverse the expression, find the postfix of the reverse string, reverse the postfix string
    return string_reversal(infix_to_postfix(string_reversal(expression)))


def take_input(query):
    while True:
        print(query)
        try:
            i = int(input(" Input: "))
        except ValueError:
            print("Press a numeric number")
        else:
            return i


def main():
    while True:

        i = take_input(" Press 1 for console input \n Press 2 for file input \n Press 3 to exit\n")

        if i == 1:
            j = take_input(" Press 1 for infix to postfix \n Press 2 for infix to prefix \n Press 3 to exit\n")

            expr = input(" enter expression ")

            x = re.findall("[a-zA-Z]", expr)

            if x:
                print("invalid expression\n\n")
                input(" press a key to continue\n")

                continue

            if j == 1:
                print("\n " + infix_to_postfix(expr) + "\n")
                continue

            if j == 2:
                print("\n " + infix_prefix(expr) + "\n")
                continue

            if j == 3:
                break

        if i == 2:
            file_loc = input(" enter file location")

            data = []

            with open(file_loc, "r") as file:
                data = file.read().split("\n")
                file.close()

            j = take_input(" Press 1 for infix to postfix \n Press 2 for infix to prefix \n Press 3 to exit\n")

            if j == 1:
                with open(file_loc, "a") as file:
                    file.write("\nanswers PostFix\n")
                    for i in data:
                        file.write(infix_to_postfix(i) + "\n")
                    file.close()
                continue

            if j == 2:
                with open(file_loc, "a") as file:
                    file.write("\nanswers prefix\n")
                    for i in data:
                        file.write(infix_prefix(i) + "\n")
                    file.close()
                continue

            if j == 3:
                break

        if i == 3:
            return


main()
