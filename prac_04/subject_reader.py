"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the newline character at the end
            parts = line.split(',')  # Split the line into its components
            parts[2] = int(parts[2])  # Convert the number of students to an integer
            subjects.append(parts)  # Add the processed line to the list of subjects
    return subjects


def display_subject_details(subjects):
    """Display subject details in a formatted manner."""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()