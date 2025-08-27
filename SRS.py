# Node for Student Record (BST)
class StudentNode:
    def __init__(self, roll, name, course, marks):
        self.roll = roll
        self.name = name
        self.course = course
        self.marks = marks
        self.left = None
        self.right = None


class StudentRecordSystem:
    def __init__(self):
        self.root = None

    # Insert student record
    def insert(self, root, roll, name, course, marks):
        if root is None:
            return StudentNode(roll, name, course, marks)
        if roll < root.roll:
            root.left = self.insert(root.left, roll, name, course, marks)
        elif roll > root.roll:
            root.right = self.insert(root.right, roll, name, course, marks)
        else:
            print("⚠️ Roll No already exists!")
        return root

    # Search student record
    def search(self, root, roll):
        if root is None:
            return None
        if roll == root.roll:
            return root
        elif roll < root.roll:
            return self.search(root.left, roll)
        else:
            return self.search(root.right, roll)

    # Delete student record
    def delete(self, root, roll):
        if root is None:
            return None
        if roll < root.roll:
            root.left = self.delete(root.left, roll)
        elif roll > root.roll:
            root.right = self.delete(root.right, roll)
        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None
            # Case 2: One child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # Case 3: Two children → find inorder successor
            temp = self.min_value_node(root.right)
            root.roll, root.name, root.course, root.marks = temp.roll, temp.name, temp.course, temp.marks
            root.right = self.delete(root.right, temp.roll)
        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Display all records (Inorder Traversal)
    def display(self, root):
        if root:
            self.display(root.left)
            print(f"Roll: {root.roll}, Name: {root.name}, Course: {root.course}, Marks: {root.marks}")
            self.display(root.right)


# =============================
# 📌 Menu-Driven Program
# =============================
if __name__ == "__main__":
    srs = StudentRecordSystem()

    while True:
        print("\n====== 🎓 Student Record System ======")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            marks = int(input("Enter Marks: "))
            srs.root = srs.insert(srs.root, roll, name, course, marks)
            print("✅ Student added successfully!")

        elif choice == "2":
            roll = int(input("Enter Roll No to Search: "))
            student = srs.search(srs.root, roll)
            if student:
                print(f"Found -> Roll: {student.roll}, Name: {student.name}, Course: {student.course}, Marks: {student.marks}")
            else:
                print("❌ Student not found.")

        elif choice == "3":
            roll = int(input("Enter Roll No to Delete: "))
            srs.root = srs.delete(srs.root, roll)
            print("🗑️ Student deleted successfully (if existed).")

        elif choice == "4":
            print("\n🎓 All Student Records:")
            srs.display(srs.root)

        elif choice == "5":
            print("👋 Exiting Student Record System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")
