import collections
Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, search_value):
    ### Repeat until value is found or the road was traversed
    # Look for the exact value
    # Check left if search_value < root_value
    # Check right if search_value > root_value
    #print(type(root))
    #print(root.value)
    try:
        if(search_value == root.value):
            return True 
        elif(search_value < root.value):
            return contains(root.left, search_value)
        elif(search_value > root.value):
            return contains(root.right, search_value)
        # If we exhaust the search and didn't find any value, return False
        return False
    except AttributeError:
        return False

if __name__ == "__main__":
    # If the value is present
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
    contains(n2, 3)
    #print(contains(n2, 3))
    # If the value is not present
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])
    n1 = Node(value=2, left=None, right=None)
    n2 = Node(value=3, left=n1, right=None)
    n5 = Node(value=7, left=None, right=None)
    n6 = Node(value=9, left=None, right=None)
    n4 = Node(value=8, left=n5, right=n6)
    n3 = Node(value=5, left=n2, right=n4)
    # Call function
    print(contains(n3,4))