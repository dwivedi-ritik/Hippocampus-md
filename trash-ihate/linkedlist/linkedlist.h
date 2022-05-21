#ifndef LINKED_LIST_H_

#define LINKED_LIST_H_

typedef struct node
{
    int val;
    struct node *next;
} Node;

extern Node *Head;

void add_nodes(int);

void print_all();


#endif //LINKED_LIST_H_