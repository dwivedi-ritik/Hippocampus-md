/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *first_travarsal = l1;
    struct ListNode *second_travaral = l2;

    struct ListNode *res_head = NULL;
    struct ListNode *last_node = NULL;
    struct ListNode *small_node = NULL;

    while (first_travarsal != NULL && second_travaral != NULL)
    {
        struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (last_node != NULL)
        {
            last_node->next = temp;
        }
        else
        {
            res_head = temp;
        }

        if (first_travarsal->val <= second_travaral->val)
        {
            small_node = first_travarsal;
            first_travarsal = first_travarsal->next;
        }
        else
        {
            small_node = second_travaral;
            second_travaral = second_travaral->next;
        }

        temp->val = small_node->val;
        temp->next = NULL;
        last_node = temp;
    }

    while (first_travarsal != NULL)
    {
        struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));

        if (last_node == NULL)
        {

            res_head = temp;
            last_node = temp;
        }

        last_node->next = temp;
        small_node = first_travarsal;
        first_travarsal = first_travarsal->next;
        temp->val = small_node->val;
        temp->next = NULL;
        last_node = temp;
    }

    while (second_travaral != NULL)
    {
        struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));

        if (last_node == NULL)
        {

            res_head = temp;
            last_node = temp;
        }

        last_node->next = temp;
        small_node = second_travaral;
        second_travaral = second_travaral->next;
        temp->val = small_node->val;
        temp->next = NULL;

        last_node = temp;
    }
    return res_head;
}