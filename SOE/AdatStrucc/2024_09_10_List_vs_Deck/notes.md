# Dynamic array vs. linked list

| Data structure         | Dynamic array  | Linked List  | Double Linked List |
| ---------------------- | -------------- | ------------ | ------------------ |
| Memory                 | OK             | OK + Pointer | OK + 2 Pointer     |
| append / push back     | quick / length | length       | quick              |
| insert(0) / push front | length         | quick        | quick              |
| [idx] random access    | quick          | length       | length             |
| insert at position     | length         | length       | length             |
| find item              | length         | length       | length             |
| insert after item      | length         | length       | length             |
| pop back               | quick          | length       | quick              |
| pop front              | length         | quick        | quick              |
| pop position           | length         | length       | length             |

where:
 - length ~ O(n)
 - quick ~ O(1)


# (Some) Abstract Data Types/Structures

## FIFO - Queue
 - push back
 - pop front

## LIFO - Stack
 - push back
 - pop back

## Priority Queue:
 - push
 - pop_max

## Set
 - add unique
 - contains?
 - remove 

