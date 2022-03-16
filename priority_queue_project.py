#!/usr/bin/python3

""" 
An implementation of a priority queue that utilizes a max-heap
"""

from logging import error
import unittest
import math

class HeapCapable(list):
    def __init__(self, lst):
        """
        Initializes a new heap from a list.
        """
        super().__init__(lst) # calling the superclass (list) constructor
        self.heap_size = len(self)

def left(i):
    """
    Return the left child of the given node.
 
    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's left child
    :rtype: int
        """
    return 2*i+1

def right(i):
    """
    Return the right child of the given node.
    
    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's right child
    :rtype: int
    """
    return 2*(i+1)

def parent(i):
    """
    Return the parent of the given node.

    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's parent
    :rtype: int
    """
    return math.floor( (i-1) / 2)

def max_heapify(A,i):
    """
    Given an array A, and assuming that the subtrees rooted at A[i]'s L and R children are max-heaps, restore the max-heap property.
    
    :param A: an array.
    :param i: the index of the  node to be floated down
    :type A: heapsort_skeleton.HeapCapable
    :type i: int
    """
    l=left(i)
    r=right(i)
    
    largest=i
    if l<A.heap_size and A[l]>A[i]:
        largest=l
    if r<A.heap_size and A[r]>A[largest]:
        largest=r
    if largest !=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest)

def build_max_heap(A):
    """ Build a max-heap, from an unsorted array. 

    :param A: the array to be sorted.
    :type A: heapsort_skeleton.HeapCapable
    """
    for i in range(A.heap_size // 2-1,-1,-1):
        max_heapify(A,i)

class MaxPriorityQueue():
    def __init__(self,array):
        self.heap = HeapCapable(array)
        build_max_heap(self.heap)


def maximum(A):
    """returns the largest key

    :param A: a max heap, satisfying the max-heap-property

    :type A: priority_queue_project.HeapCapable
    """
    return A[0]


def extract_max(A):
    """removes and returns the largest key

    :param A: a max heap, satisfying the max-heap-property

    :type A: priority_queue_project.HeapCapable
    """
    if A.heap_size < 1:
        error("heap underflow")
    max=A[0]
    A[0] = A[A.heap_size-1]
    A.heap_size = A.heap_size-1
    max_heapify(A,0)
    return max



def increase_key(A,index,newValue):
    """increases the value at the given index with a new, higher value. 
    This value is then sorted to its proper place in the heap.

    :param A: a max heap, satisfying the max-heap-property
    :param index: the index of the value to be increased
    :param newValue: the value that they key at the given index is replaced with

    :type A: priority_queue_project.HeapCapable
    """
    if newValue < A[index]:
        error("New key is smaller than current key!")
        return
    A[index] = newValue
    while index > 0 and A[ parent( index ) < A[ index ] ]:
        A[ index ], A[ parent(index)] = A[ parent (index)], A[index]
        index=parent(index)

def heap_insert(A,newValue):
    """inserts the newValue into an exisiting max-heap.

    :param A: a max heap, satisfying the max-heap-property
    :param newValue: the value to be inserted into the heap.

    :type A: priority_queue_project.HeapCapable
    """
    A.heap_size = A.heap_size + 1
    A.append(-math.inf)
    increase_key(A, A.heap_size-1, newValue)

class testHeapSort(unittest.TestCase):

############## ALL PRIORITY QUEUE TESTS BELOW ##############

    def test_initialize(self):
        A=[5,4,7,1,3]
        queue=MaxPriorityQueue(A)
        self.assertEqual(queue.heap, [ 7, 4, 5, 1, 3 ])

    def test_maximum_1(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        build_max_heap(A)
        self.assertEqual( maximum (A) , 27)

    def test_maximum_with_repeated_values(self):
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3, 18])
        build_max_heap(A)
        self.assertEqual( maximum (A), 18)

    def test_extract_max(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        build_max_heap(A)
        self.assertEqual( extract_max(A), 27)

    def test_extract_max_with_two_calls(self):
        A=HeapCapable([ 10, 8, 4, 2, 34, 45, 12, 9, 2, 1, 4, 0 ])
        build_max_heap(A)
        self.assertEqual(extract_max(A),45)
        self.assertEqual(extract_max(A),34)

    def test_extract_max_with_repeated_values(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])
        build_max_heap(A)
        self.assertEqual( extract_max(A), 27)

    def test_increase_key(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        build_max_heap(A)
        increase_key(A,0,28)
        self.assertEqual( A, [28, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0] )

    def test_increase_key_non_zero_index(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])
        build_max_heap(A)
        increase_key(A,5,10)
        self.assertEqual(A, [10, 27, 27, 17, 13, 27, 3, 16, 7, 12, 4, 8, 9, 0, 1, 5])

    def test_increase_key_multiple_values(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])
        build_max_heap(A)
        increase_key(A,5,28)
        increase_key(A,2,30)
        self.assertEqual(A, [30, 27, 28, 17, 13, 27, 3, 16, 7, 12, 4, 8, 9, 0, 1, 5])

    def increase_key_error_statement(self):
        A = HeapCapable([ 28, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])
        build_max_heap(A)
        increase_key(A,0,10)
        self.assertEqual(A,[ 28, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])


    def test_heap_insert(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])
        build_max_heap(A)
        heap_insert(A,30)
        self.assertEqual(A, [30, 27, 27, 27, 13, 10, 3, 17, 7, 12, 4, 8, 9, 0, 1, 5, 16])

    def test_heap_insert_with_multiple_values(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0, 27, 27])
        build_max_heap(A)
        heap_insert(A,29)
        heap_insert(A,6)
        self.assertEqual(A, [6, 29, 27, 27, 13, 10, 3, 17, 27, 12, 4, 8, 9, 0, 1, 5, 16, 7])
        



############## ALL HEAP TESTS BELOW ########################
    def test_left_1(self):
        self.assertEqual( left(0), 1 )

    def test_left_2(self):
        self.assertEqual( left(2), 5 )

    def test_left_3(self):
        self.assertEqual( left(3), 7 )

    def test_right_1(self):
        self.assertEqual( right(0), 2 )

    def test_right_2(self):
        self.assertEqual( right(2), 6 )

    def test_right_3(self):
        self.assertEqual( right(3), 8 )

    def test_parent_1(self):
        self.assertEqual( parent(1), 0 )
    
    def test_parent_2(self):
        self.assertEqual( parent(2), 0 )
    
    def test_parent_3(self):
        self.assertEqual( parent(3), 1 )
    
    def test_parent_4(self):
        self.assertEqual( parent(4), 1 )

    def test_max_heapify_general_case(self):
        """ 
        CLRS3, exercise 6.2-1
        """
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        max_heapify(A,2)
        self.assertEqual( A, [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])

    def test_max_heapify_untouched(self):
        """ 
        MaxHeapify() does not change the array if A[i] is larger than its two children
        """
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        max_heapify(A, 1)
        self.assertEqual(A, [ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])


    def test_max_heapify_reduced_heap_size(self):
        """ 
        Max-Heapify() should always ckeck against the heap's size, not the array's length!
        """
        A = HeapCapable([ 3, 10, 7, 9, 7, 5, 2, 8, 5, 4 ])
        A.heap_size=7
        max_heapify(A,0)
        self.assertEqual( A, [ 10, 9, 7, 3, 7, 5, 2, 8, 5, 4 ])


    def test_buildmaxheap_unique_values(self):
        """
        BuildMaxHeap: general case, with non-repeated values
        """
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        self.assertEqual(A, [19, 17, 18, 16, 10, 6, 12, 13, 1, 8, 5, 4, 2, 3])

    def test_buildmaxheap_repeated_values(self):
        """
        BuildMaxHeap: general case, with repeated values
        """
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
        build_max_heap(A)
        self.assertEqual(A, [18, 16, 17, 10, 12, 13, 7, 3, 4, 7, 8, 8, 7, 3])

    def test_buildmaxheap_1_element_array(self):
        """
        BuildMaxHeap: special case - 1-element array
        """
        A = HeapCapable([7])
        build_max_heap(A)
        self.assertEqual(A, [7])





def main():
        unittest.main()

if __name__ == '__main__':
        main()


