class LeaveType:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __str__(self):
        return f"{self.name}: {self.days} days"

class LeaveTypeManagement:
    def __init__(self):
        self.leave_types = []

    def add_leave_type(self, leave_type):
        for lt in self.leave_types:
            if lt.name == leave_type.name:
                print(f"Leave type '{leave_type.name}' already exists.")
                return
        self.leave_types.append(leave_type)
        print(f"Leave type '{leave_type.name}' added with {leave_type.days} days.")

    def remove_leave_type(self, leave_name):
        for lt in self.leave_types:
            if lt.name == leave_name:
                self.leave_types.remove(lt)
                print(f"Leave type '{leave_name}' removed.")
                return
        print(f"Leave type '{leave_name}' does not exist.")

    def list_leave_types(self):
        if not self.leave_types:
            print("No leave types available.")
        else:
            print("Available leave types:")
            for lt in self.leave_types:
                print(f"- {lt}")

def main():
    manager = LeaveTypeManagement()
    
    while True:
        print("\nLeave Type Management System")
        print("1. Add Leave Type")
        print("2. Remove Leave Type")
        print("3. List Leave Types")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            leave_name = input("Enter leave type name: ")
            leave_days = int(input("Enter number of leave days: "))
            leave_type = LeaveType(leave_name, leave_days)
            manager.add_leave_type(leave_type)
        elif choice == '2':
            leave_name = input("Enter leave type name to remove: ")
            manager.remove_leave_type(leave_name)
        elif choice == '3':
            manager.list_leave_types()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()