// An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

#include <iostream>
#include <vector>

class Node
{
  public:
  int value;
  Node * xpn;

  Node(int new_value)
  {
  value = new_value;
  }

  static Node * XOR (Node *pervious, Node *next)
  {
  return (Node*)((uintptr_t)(pervious) ^ (uintptr_t)(next));
  }
};

class XOR_LL
{
  public:
  Node* head = NULL;
  Node* tail = NULL;
  int length = 0;

  XOR_LL(Node* head_node)
  {
    head = head_node;
    tail = head_node;
    length += 1;
  }

  void add(int value)
  {
    Node *new_node = new Node(value);

    new_node->xpn = Node::XOR(tail, NULL);
  
  if (tail != NULL)  
    { 
        Node* next = Node::XOR(tail->xpn, NULL);  
        tail->xpn = Node::XOR(new_node, next);  
    } 
    length += 1;
    tail = new_node;
  }

  Node* get(int index)
  {
    Node *curr = head;  
    Node *prev = NULL;  
    Node *next = NULL;  

    for(int i = 0; i < index; i++) 
    {  
        next = Node::XOR(prev, curr->xpn);  
  
        prev = curr;  
        curr = next;  
    }  
    return curr;
  }

  void print_list()
  {
    Node *curr = head;  
    Node *prev = NULL;  
    Node *next = NULL;  
  
    std::cout << "The XOR linked list contains: ";  
  
    while (curr != NULL)  
    {  
        std::cout << curr->value <<" ";  
  
        next = Node::XOR(prev, curr->xpn);  
  
        prev = curr;  
        curr = next;  
    }
    std::cout << "\n"; 
  }
};

int main() {
    // Create the XOR linked list
    Node *head = new Node(1);
    XOR_LL xor_ll(head);
    xor_ll.add(2);
    xor_ll.add(3);
    xor_ll.add(4);
    xor_ll.add(5);

    // Print the list
    xor_ll.print_list();

    // Get the node at the index
    // Indexing starts at 0
    int index = 2; 
    Node* indexed_node = xor_ll.get(index);
    std::cout << "The value of xor_ll at index " << index << " is " << indexed_node->value << "\n"; 

  return 0;
}