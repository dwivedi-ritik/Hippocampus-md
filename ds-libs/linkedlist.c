#include "stdio.h"
#include "stdlib.h"

struct node
{
    int val;
    struct node *next;
};

typedef struct node Node;

Node *Head = NULL;

void add_nodes(int data)
{
    Node *usr_node = (Node *)malloc(sizeof(Node));
    usr_node->val = data;
    usr_node->next = NULL;

    if (Head == NULL)
    {
        Head = usr_node;
        return;
    }

    Node *temp_trav = Head;
    for (; temp_trav->next != NULL; temp_trav = temp_trav->next)
        ;
    temp_trav->next = usr_node;
}

void print_all()
{
    Node *temp = Head;
    for (; temp != NULL; temp = temp->next)
    {
        printf("%d ", temp->val);
    }
    printf("\n");
}

void main()
{
    add_nodes(23);
    add_nodes(53);
    add_nodes(43);
    add_nodes(33);
    print_all();
}