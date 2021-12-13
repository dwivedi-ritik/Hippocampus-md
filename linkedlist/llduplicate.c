#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

// I will try to implement the the 
Node *deleteDuplicate(Node *head_node){
	 int arr[300] , res[300] , temp = 102;
	int length = 0 , top = -1;

	Node* temp_node = head_node;
	Node* result_node;

	if (temp_node == NULL) return temp_node;
	
	for(int i = 0 ; temp_node != NULL ; temp_node = temp_node->next , i++ ){
		arr[i] = temp_node->val;
		length++ ; 
	}

	for(int i = 0 ; i < length ; i++){
		
		if (arr[i] != temp){
			
			top++;

			res[top] = arr[i];
			
			temp = arr[i];
		}else if ( top > -1 && res[top] == arr[i] ) {
			top--;
		}

	}

	//Creating new node with
	result_node = (Node *)malloc(sizeof(Node));
	
    if(top == -1){
        result_node = NULL;
        
        return result_node;
    }
    
    
    result_node->val = res[0];
	result_node->next = NULL;
	
	Node *result_head = result_node;

	for(int i = 1 ; i <= top ; i++){

		Node* one_node = (Node *)malloc(sizeof(Node));
		one_node->val = res[i];
		one_node->next = NULL;
		result_node->next = one_node;
		result_node = result_node->next;


	}
	return result_head;
}



void main()
{
	add_nodes(1);

	add_nodes(1);
	add_nodes(1);
	// add_nodes(2);
	// add_nodes(3);
	deleteDuplicate(Head);
	// printf("head is pointing to -> %d\n" , Head->val);
	// print_all();
}
