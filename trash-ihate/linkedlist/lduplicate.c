#include <stdlib.h>
#include <stdio.h>
#include "linkedlist.h"

void duplicate(Node *head){
	Node* result_node_head;
    Node* result_trav;
    Node* node_trav;
    
    int temp = 102;
    
    // if (head == NULL) return head;
    
    result_trav = (Node *)malloc(sizeof(Node));
    
    result_trav->val = head->val;
    result_trav->next = NULL;
    
    temp = head->val;
    
    result_node_head = result_trav;
    
    
    for(node_trav = head->next ; node_trav != NULL ; node_trav = node_trav->next){
        
        if(node_trav->val != temp){

            Node* one_node = (Node*)malloc(sizeof(Node));
            one_node->val = node_trav->val;
            one_node->next = NULL;
            
            result_trav->next = one_node;
        	
        	result_trav = result_trav->next;
        }

        temp = node_trav->val;
	    
        
    }

    for(; result_node_head != NULL ; result_node_head = result_node_head->next){
    	printf("%d " , result_node_head->val);
    }
    // return result_node_head;
    
}
void main()
{
	add_nodes(1);
	add_nodes(1);
	add_nodes(2);

	duplicate(Head);
}


