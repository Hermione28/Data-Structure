
class Solution:
    def __init__(self):
        self.document = []      
        self.redo_stack = []    

    def append(self, x):
        # append x into document
        self.document.append(x)
        self.redo_stack.clear()   

    def undo(self):
        # undo last change
        if self.document:
            self.redo_stack.append(self.document.pop())

    def redo(self):
        # redo changes
        if self.redo_stack:
            self.document.append(self.redo_stack.pop())

    def read(self):
        # read the document
        return "".join(self.document)
