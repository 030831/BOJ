#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

int is_operator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '%';
}

int precedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
        case '%':
            return 2;
        default:
            return 0;
    }
}

int is_operand(char c) {
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
}

void infix_to_postfix(char infix[], char postfix[]) {
    int i, j;
    char stack[MAX_SIZE];
    int top = -1;

    for (i = 0, j = 0; infix[i] != '\0'; i++) {
        char c = infix[i];

        if (is_operand(c)) {
            postfix[j++] = c;
        } else if (is_operator(c)) {
            while (top >= 0 && precedence(stack[top]) >= precedence(c)) {
                postfix[j++] = stack[top--];
            }
            stack[++top] = c;
        } else if (c == '(') {
            stack[++top] = c;
        } else if (c == ')') {
            while (stack[top] != '(') {
                postfix[j++] = stack[top--];
            }
            top--;
        }
    }

    while (top >= 0) {
        postfix[j++] = stack[top--];
    }

    postfix[j] = '\0';
}

int main() {
    char infix[MAX_SIZE], postfix[MAX_SIZE];

    scanf("%s", infix);

    infix_to_postfix(infix, postfix);



    printf("%s", postfix);

    return 0;
}
