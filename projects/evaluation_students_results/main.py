# 4.3.1.17 LAB: Evaluating students' results

class StudentsDataException(Exception):
    """Base class for exceptions in this module."""
    pass
    
class BadLine(StudentsDataException):
    def __init__(self, line):
        self.line = line
        super().__init__(f"Bad line: {line}")
    
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__("File is empty")

def process_class_data():
    # Step 1: Ask user for filename
    filename = input("Enter Professor Jekyll's class file: ")

    try:
        # Step 2: Try to open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            # Check if file is empty
            if not lines:
                raise FileEmpty()
            
            # Create an empty dictionary to store student data
            students = {}

            for line_number, line in enumerate(lines, 1):
                # Remove leading/trailing whitespace
                line = line.strip()
                
                try:
                    # Split the line by whitespace
                    parts = line.split()
                    
                    # Check if we have exactly 3 parts (first name, last name, points)
                    if len(parts) != 3:
                        raise BadLine(line)
                    
                    first_name, last_name, points_str = parts
                    
                    # Try to convert points to float
                    try:
                        points = float(points_str)
                    except ValueError:
                        # If points can't be converted to float, it's a bad line
                        raise BadLine(line)
                    
                    # Create student key (combining first and last name)
                    student_key = f"{first_name} {last_name}"
                    
                    # Add points to existing total or create new entry
                    if student_key in students:
                        students[student_key] += points
                    else:
                        students[student_key] = points
                        
                except BadLine as e:
                    print(e)
                    # Continue processing other lines

            # Sort students by their total points
            sorted_students = sorted(students.items(), key=lambda x: x[1])

            # Print the sorted results
            for student, points in sorted_students:
                # Format the output with proper spacing
                print(f"{student:<15} {points}")
                
    except FileNotFoundError:
        print(f"No such file: {filename}")
    except FileEmpty as e:
        print(e)

# Call the function to run the program
if __name__ == "__main__":
    process_class_data()