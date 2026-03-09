from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
MENU: str = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    load_file(projects)  # Load projects initially
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print(MENU)
        user_input = input(">>> ").upper()
        if user_input == "L":
            load_file(projects)
        elif user_input == "S":
            save_data_to_file(projects)
        elif user_input == "D":
            display_projects(projects)
        elif user_input == "F":
            filter_projects(projects)
        elif user_input == "A":
            add_project(projects)
        elif user_input == "U":
            update_project(projects)
        elif user_input == "Q":
            if input("Would you like to save to projects.txt? ").strip().lower() == "yes":
                save_data_to_file(projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid Menu Choice")


def load_file(projects):
    projects.clear()
    try:
        with open(FILENAME, 'r') as infile:
            infile.readline()  # Skip header
            for line in infile:
                parts = line.strip().split('\t')
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
            print(f"Data loaded from {FILENAME}")
    except FileNotFoundError:
        print(f"{FILENAME} not found.")


def save_data_to_file(projects):
    """Saves the updated projects and new projects to the designated file"""
    file_name = input("File Name:\n>>>")
    with open(file_name, 'w') as outfile:  # Using 'with' to ensure file is closed automatically
        outfile.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            outfile.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                          f"{project.cost_estimate:.2f}\t{project.completion_percentage}\n")
    print(f"Data saved to {file_name}")


def display_projects(projects):
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda p: p.start_date):
        print(f"  {project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    print("Completed projects:")
    for project in sorted(complete_projects, key=lambda p: p.start_date):
        print(f"  {project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")


def filter_projects(projects):
    try:
        filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "),
                                                 "%d/%m/%Y").date()
        for project in sorted(projects, key=lambda p: p.start_date):
            project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
            if project_date >= filter_date:
                print(f"{project.name}, start: {project.start_date}, priority {project.priority}, "
                      f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input_date("Start date (dd/mm/yy): ")
    priority = input_int("Priority: ")
    cost_estimate = input_float("Cost estimate: $")
    completion_percentage = input_int("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print("Project added")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    project_choice = input_int("Project choice: ", limit=len(projects) - 1)
    project = projects[project_choice]
    print(f"Selected: {project.name}, start: {project.start_date}, priority {project.priority}, "
          f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    project.completion_percentage = input_int("New percentage: ")
    project.priority = input_int("New priority: ")
    print(f"{project.name} has been updated")


def input_date(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            print("Invalid date format. Please enter in dd/mm/yyyy format.")


def input_int(prompt, limit=None):
    while True:
        try:
            value = int(input(prompt))
            if limit is not None and value > limit:
                print(f"Please enter a number between 0 and {limit}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


main()