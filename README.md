# taskTrackerCLI
This project practices handling CLI in files and writing and reading files.

The folloowing is the list of commands to use to run the program on your pc. Before running the program, be sure to check the requirements after this list of commands the program follows.

# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress



Now, before running the commands above, type the following into your terminal to register task-cli as a command:
vi ~/.bash_profile
After typing the above line, add alias "task-cli" = python3 task.py 
Save the file by pressing escape symbol. type the ':' symbol followed by wq; Press on enter.
Type source ~/.bash_profile before running the command.

Requirements:
Have the latest version of python running in the directory the program is running or globally to support the program running.
