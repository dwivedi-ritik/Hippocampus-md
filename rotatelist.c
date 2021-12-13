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

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void main()
{
    int arr[6] = {1, 2, 3, 4, 5, 6};
    for (int i = 0; i < 6; i++)
    {
        add_nodes(arr[i]);
    }

    //Rotating a array

    for (int i = 0; i < 2233; i++)
    {

        int length = 5, last = arr[0], temp;

        for (int i = 1; i < length; i++)
        {
            temp = arr[i];
            arr[i] = last;
            last = temp;
        }
        arr[0] = last;
    }
    // for (int i = 0; i < 5; i++)
    // {
    //     printf("%d ", arr[i]);
    // }
    // printf("\n");
    // [1,2,3]

    for (int i = 0; i < 100; i++)
    {
        Node *temp_link = Head;

        int last = temp_link->val;
        int temp;

        while (temp_link != NULL)
        {
            temp = temp_link->val;
            temp_link->val = last;
            last = temp;
            temp_link = temp_link->next;
        }
        Head->val = last;
    }

    print_all();
}

//Working solutionmax

// typedef struct ListNode Node;
// struct ListNode *rotateRight(struct ListNode *head, int rot)
// {

//     if (head == NULL)
//         return head;
//     Node *len = head;

//     int link_length = 0;
//     while (len != NULL)
//     {
//         len = len->next;
//         link_length++;
//     }
//     rot = rot % link_length;
//     for (int i = 0; i < rot; i++)
//     {
//         Node *temp_link = head;

//         int last = temp_link->val;
//         int temp;

//         while (temp_link != NULL)
//         {
//             temp = temp_link->val;
//             temp_link->val = last;
//             last = temp;
//             temp_link = temp_link->next;
//         }
//         head->val = last;
//     }
//     return head;
// }