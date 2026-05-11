class TreeNode:
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    
class TreeMap:
    
    def __init__(self):
        self.root = None     

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val, None, None)
        else:
            cur = self.root
            while (cur):
                if key < cur.key:
                    if not cur.left:
                        cur.left = TreeNode(key, val, None, None)
                        return
                    cur = cur.left
                elif key > cur.key:
                    if not cur.right:
                        cur.right = TreeNode(key, val, None, None)
                    cur = cur.right
                else:
                    cur.val = val
                    return


    def get(self, key: int) -> int:
        cur = self.root
        while (cur):
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
            
        cur = self.root
        while (cur.left):
            cur = cur.left

        return cur.val

    def getMinNode(self, root) -> Optional[TreeNode]:
        if not root:
            return None
            
        cur = root
        while (cur.left):
            cur = cur.left

        return cur

    def getMax(self) -> int:
        if not self.root:
            return -1
            
        cur = self.root
        while (cur.right):
            cur = cur.right

        return cur.val

    def removeNode(self, root, key):
        if not root:
            return None
        
        if key < root.key:
            root.left = self.removeNode(root.left, key)
        elif key > root.key:
            root.right = self.removeNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                newNode = self.getMinNode(root.right)
                root.key = newNode.key
                root.val = newNode.val
                root.right = self.removeNode(root.right, newNode.key)
        return root
                

    def remove(self, key: int) -> None:
        self.root = self.removeNode(self.root, key)

    def getInorderKeys(self) -> List[int]:
        if not self.root:
            return []

        keys = []
        stack = []
        cur = self.root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            keys.append(cur.key)
            cur = cur.right
        return keys