import sys
import json
import os

FILE = "tasks.json"

def loadTasks():
	if not os.path.exists(FILE):
		return []
	with open(FILE, "r") as f:
		try:
			return json.load(f)
		except json.JSONDecodeError:
			return []

def saveTasks(tasks):
	with open(FILE, "w") as f:
		json.dump(tasks, f, indent=4)

def addTask(description):
	tasks = loadTasks()
	task = {
	    "id": len(tasks) + 1,
	    "description": description,
	    "status": "todo",
	}
	tasks.append(task)
	saveTasks(tasks)
	print("added task", task["id"], ":", task["description"])

def listTasks(status=None):
	tasks = loadTasks()
	if not tasks:
		print("No Tasks Found")
		return
	for any in tasks:
		if status == None or any["status"] == status:
		    print("[", any["id"], "]", any["description"], "-", any["status"])

def updateTasks(id, description):
	tasks = loadTasks()
	for any in tasks:
		if any["id"] == id:
		    any["description"] = description
		    saveTasks(tasks)
		    print("Updated Task #", id)
		    return
	print("Task Not Found")

def deleteTask(id):
	tasks = loadTasks()
	newTasks = [t for t in tasks if t["id"] != id]
	if len(newTasks) == len(tasks):
	    print("Task Not Found")
	else:
		for i, task in enumerate(newTasks):
		    task["id"] = i + 1
		saveTasks(newTasks)
		print("Deleted Task #", id)

def mark_status(task_id, status):
	tasks = loadTasks()
	for t in tasks:
		if t["id"] == task_id:
			t["status"] = status
			saveTasks(tasks)
			print("Task #", task_id, "marked as", status)
			return
	print("Task not found.")

def main():
	if len(sys.argv) < 2:
		print("Usage: python task.py [add|list|update|delete|mark-done|mark-progress|list-done|list-todo|list-progress] ...")
		return

	command = sys.argv[1]

	if command == "add":
		description = " ".join(sys.argv[2:])
		addTask(description)
	elif command == "list":
		listTasks()
	elif command == "update":
		updateTasks(int(sys.argv[2]), " ".join(sys.argv[3:]))
	elif command == "delete":
		deleteTask(int(sys.argv[2]))
	elif command == "mark-done":
		mark_status(int(sys.argv[2]), "done")
	elif command == "mark-in-progress":
		mark_status(int(sys.argv[2]), "in-progress")
	elif command == "list done":
		listTasks("done")
	elif command == "list todo":
		listTasks("todo")
	elif command == "list in-progress":
		listTasks("in-progress")
	else:
		print("Unknown command.")

if __name__ == "__main__":
	main()
