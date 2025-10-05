"""
Hoàn tác (Undo/Redo) trong ứng dụng
Kiểm tra ngoặc đúng/sai trong biểu thức ((a + b) * c)
Đệ quy (Recursion) trong ngôn ngữ lập trình
Duyệt cây hoặc đồ thị (DFS)
"""

# Hoàn tác (Undo/Redo) trong ứng dụng
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def get_text(self):
        return self.text

TextEditorInstance = TextEditor()
TextEditorInstance.type("Hello, ")
TextEditorInstance.type("world!")
print(TextEditorInstance.get_text())  # Output: Hello, world!

TextEditorInstance.undo()
print(TextEditorInstance.get_text())  # Output: Hello,

TextEditorInstance.redo()
print(TextEditorInstance.get_text())  # Output: Hello, world!

# Mo ta ky hon qua trinh nay cua UndoStack/RedoStack/Text
# Luc dau nguoi dung go "Hello, "
# UndoStack = [""] (luu trang thai truoc do)
# RedoStack = []
# Text = "Hello, "
# Sau do nguoi dung go "world!"
# UndoStack = ["", "Hello, "] (luu trang thai truoc do)
# RedoStack = []
# Text = "Hello, world!"
# Sau do nguoi dung bam Undo
# UndoStack = [""] (pop trang thai truoc do)
# RedoStack = ["Hello, world!"] (luu trang thai hien tai de redo)
# Text = "Hello, "
# Sau do nguoi dung bam Redo
# UndoStack = ["", "Hello, "] (luu trang thai truoc do)
# RedoStack = [] (pop trang thai truoc do)
# Text = "Hello, world!"

# Kiểm tra ngoặc đúng/sai trong biểu thức ((a + b) * c)
def is_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return len(stack) == 0
print(is_balanced("((a + b) * c)"))  # Output: True
print(is_balanced("((a + b] * c)"))  # Output: False
print(is_balanced("{[()]}"))          # Output: True
print(is_balanced("{[(])}"))          # Output: False

# Đệ quy (Recursion) trong ngôn ngữ lập trình
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Duyệt cây hoặc đồ thị (DFS)
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
def dfs(node):
    if node is None:
        return
    print(node.value)
    for child in node.children:
        dfs(child)
# Example usage:
root = Node(1)
child1 = Node(2)
child2 = Node(3)
root.children.append(child1)
root.children.append(child2)
child1.children.append(Node(4))
child1.children.append(Node(5))
child2.children.append(Node(6))
dfs(root)