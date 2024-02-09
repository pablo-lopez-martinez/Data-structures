# Python Data Structures Implementations

This repository contains implementations of various data structures in Python.

## Contents

- **Linear-structures**: This folder contains implementations of linear data structures.
  - **Lists**: This subfolder contains implementations of linked lists.
    - [DoubleLinkedList.py](Linear-structures/Lists/DoubleLinkedList.py): Implementation of a doubly linked list.
    - [LinkedList.py](Linear-structures/Lists/LinkedList.py): Implementation of a singly linked list.
  - **Queue**: This subfolder contains an implementation of a queue.
    - [Queue.py](Linear-structures/Queue/Queue.py): Implementation of a queue data structure.
  - **Stack**: This subfolder contains an implementation of a stack.
    - [Stack.py](Linear-structures/Stack/Stack.py): Implementation of a stack data structure.

- **Non-linear-structures**: This folder contains implementations of non-linear data structures.
  - **BinarySearchTree**: This subfolder contains an implementation of a binary search tree.
    - [SearchTree.py](Non-linear-structures/BinarySearchTree/SearchTree.py): Implementation of a binary search tree.
  - **Heap**: This subfolder contains an implementation of a heap.
    - [Heap.py](Non-linear-structures/Heap/Heap.py): Implementation of a heap data structure.

## Usage

To use any of the data structure implementations, you can simply import the corresponding Python file into your project. For example:

```python
from Linear-structures.Lists.LinkedList import LinkedList

# Create a linked list
my_list = LinkedList()

# Perform operations on the linked list
my_list.add(1)
my_list.add(2)
my_list.add(3)

print(my_list)

