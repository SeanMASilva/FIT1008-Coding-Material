from unittest import TestCase
from data_structures.array_heap import ArrayHeap
from data_structures.max_array_heap import MaxArrayHeap
from data_structures.min_array_heap import MinArrayHeap

def check_heap_ordering(heap_array, bound, ordering):
    for i in range(1, bound):
        valid = (2*i     > bound or ordering(heap_array[i], heap_array[2*i    ])) and \
                (2*i + 1 > bound or ordering(heap_array[i], heap_array[2*i + 1]))
        if not valid: 
            print(heap_array, i)
            return False

    return True

class TestArrayHeap(TestCase):
    def test_init(self):
        heap = ArrayHeap(0, 'max')

        self.assertRaises(ValueError, lambda: ArrayHeap(-1, 'max'))
        self.assertRaises(ValueError, lambda: ArrayHeap(1, 'asdf'))
        self.assertRaises(ValueError, lambda: heap.add(1))
    
    def test_add(self):
        heap = ArrayHeap[int](10, 'max')
        for i in range(10):
            self.assertEqual(len(heap), i)
            heap.add(i)
            self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, i, lambda a, b: a >= b))
        
        self.assertRaises(ValueError, lambda: heap.add(1))
            
    
        heap = ArrayHeap(10, 'min')
        for i in range(10):
            heap.add(i)
            self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, i, lambda a, b: a <= b))
    
    def test_extract(self):
        heap = ArrayHeap[int](10, 'min')
        self.assertRaises(ValueError, heap.extract_root)

        for i in range(10):
            heap.add(i)
        
        for i in range(10):
            self.assertEqual(len(heap), 10 - i)
            min_item = heap.extract_root()
            self.assertEqual(min_item, i)
            self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, len(heap), lambda a, b: a <= b))
    
    def test_peek(self):
        heap = ArrayHeap(10, 'max')
        self.assertRaises(IndexError, heap.peek)

        for i in range(10):
            heap.add(i)
            self.assertEqual(heap.peek(), i)
            self.assertEqual(len(heap), i + 1)

    def test_heapify(self):
        heap = ArrayHeap.heapify(list(range(10)), 'max')
        self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, len(heap), lambda a, b: a >= b))

        heap = ArrayHeap.heapify(list(range(10)), 'min')
        self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, len(heap), lambda a, b: a <= b))
        self.assertIs(type(heap), ArrayHeap)
        elems = [heap.extract_root() for _ in range(10)]

        self.assertEqual(elems, [0,1,2,3,4,5,6,7,8,9])

class TestMinArrayHeap(TestCase):
    def setUp(self):
        self.heap = MinArrayHeap(10)

    def test_init(self):
        self.assertRaises(ValueError, lambda: MinArrayHeap(-1))
    
    def test_add(self):
        for i in range(10):
            self.assertEqual(len(self.heap), i)
            self.heap.add(i)
            self.assertTrue(check_heap_ordering(self.heap._UnorderedArrayHeap__array, i, lambda a, b: a <= b))
        
        self.assertRaises(ValueError, lambda: self.heap.add(1))
    
    def test_extract(self):
        self.assertRaises(ValueError, self.heap.extract_min)
        
        for i in range(10):
            self.heap.add(i)
        
        for i in range(10):
            self.assertEqual(len(self.heap), 10-i)
            min_item = self.heap.extract_min()
            self.assertEqual(min_item, i)
            self.assertTrue(check_heap_ordering(self.heap._UnorderedArrayHeap__array, len(self.heap), lambda a, b: a <= b))
        
        self.assertRaises(ValueError, self.heap.extract_min)
    
    def test_peek(self):
        self.assertRaises(IndexError, self.heap.peek)

        for i in range(10):
            self.heap.add(i)
            self.assertEqual(self.heap.peek(), 0)
        
        for i in range(10):
            self.assertEqual(self.heap.peek(), i)
            self.heap.extract_min()
        
        self.assertRaises(IndexError, self.heap.peek)
    
    def test_heapify(self):
        heap = MinArrayHeap.heapify(range(10))

        self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, len(heap), lambda a, b: a <= b))
        self.assertIs(type(heap), MinArrayHeap)
        elems = [heap.extract_root() for _ in range(10)]

        self.assertEqual(elems, [0,1,2,3,4,5,6,7,8,9])

class TestMaxArrayHeap(TestCase):
    def setUp(self):
        self.heap = MaxArrayHeap(10)
    
    def test_add(self):
        for i in range(10):
            self.assertEqual(len(self.heap), i)
            self.heap.add(i)
            self.assertTrue(check_heap_ordering(self.heap._UnorderedArrayHeap__array, i, lambda a, b: a >= b))
        
        self.assertRaises(ValueError, lambda: self.heap.add(1))
    
    def test_extract(self):
        self.assertRaises(ValueError, self.heap.extract_max)
        
        for i in range(10):
            self.heap.add(i)
        
        for i in range(10):
            self.assertEqual(len(self.heap), 10-i)
            max_item = self.heap.extract_max()
            self.assertEqual(max_item, 9-i)
            self.assertTrue(check_heap_ordering(self.heap._UnorderedArrayHeap__array, len(self.heap), lambda a, b: a >= b))
        
        self.assertRaises(ValueError, self.heap.extract_max)
    
    def test_peek(self):
        self.assertRaises(IndexError, self.heap.peek)

        for i in range(10):
            self.heap.add(i)
            self.assertEqual(self.heap.peek(), i)
        
        for i in range(10):
            self.assertEqual(self.heap.peek(), 9-i)
            self.heap.extract_max()
        
        self.assertRaises(IndexError, self.heap.peek)
    
    def test_heapify(self):
        heap = MaxArrayHeap.heapify(range(10))

        self.assertTrue(check_heap_ordering(heap._UnorderedArrayHeap__array, len(heap), lambda a, b: a >= b))
        self.assertIs(type(heap), MaxArrayHeap)
        elems = [heap.extract_root() for _ in range(10)]

        self.assertEqual(elems, [9,8,7,6,5,4,3,2,1,0])
