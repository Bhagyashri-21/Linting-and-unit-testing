from locust import HttpUser, task, between
from threading import Lock
import random


class FastAPIUser(HttpUser):
    wait_time = between(1, 5)
    group_ids = []
    todo_ids = []  # New list for storing todo IDs
    lock = Lock()

    def on_start(self):
        """Initialize by fetching group IDs and todo IDs."""
        self.fetch_group_ids()
        self.fetch_todo_ids()  # Fetch todos at the start of the test

    def fetch_group_ids(self):
        """Fetch group IDs from the API and update the local list."""
        response = self.client.get("/list/groups/")
        if response.status_code == 200:
            try:
                self.group_ids = [group["id"] for group in response.json()]
                print(f"Fetched group IDs: {len(self.group_ids)}")
            except (KeyError, TypeError) as e:
                print(f"Unexpected response format: {e}")
        else:
            self.log_error("Failed to fetch group IDs", response)

    def fetch_todo_ids(self):
        """Fetch todo IDs from the API and update the local list."""
        response = self.client.get("/list/todos/")
        if response.status_code == 200:
            try:
                self.todo_ids = [todo["id"] for todo in response.json()]
                print(f"Fetched todo IDs: {len(self.todo_ids)}")
            except (KeyError, TypeError) as e:
                print(f"Unexpected response format: {e}")
        else:
            self.log_error("Failed to fetch todo IDs", response)

    def delete_group_by_id(self, group_id):
        """Send a DELETE request for the specified group ID."""
        response = self.client.delete(f"/delete/groups/{group_id}")
        if response.status_code == 200:
            print(f"Successfully deleted group with ID {group_id}.")
            return True
        elif response.status_code == 404:
            print(f"Group with ID {group_id} not found.")
        else:
            self.log_error(f"Failed to delete group {group_id}", response)
        return False

    def delete_todo_by_id(self, todo_id):
        """Send a DELETE request for the specified todo ID."""
        response = self.client.delete(f"/delete/todos/{todo_id}")
        if response.status_code == 200:
            print(f"Successfully deleted todo with ID {todo_id}.")
            return True
        elif response.status_code == 404:
            print(f"Todo with ID {todo_id} not found.")
        else:
            self.log_error(f"Failed to delete todo {todo_id}", response)
        return False

    def update_todo_by_id(self, todo_id):
        """Send a PUT request to update a todo item."""
        # You can customize this with any data for the todo update
        todo_data = {
            "title": f"Updated Todo {todo_id}",
            "description": f"Updated description for todo {todo_id}"
        }

        response = self.client.put(f"/update/todos/{todo_id}", json=todo_data)
        if response.status_code == 200:
            print(f"Successfully updated todo with ID {todo_id}.")
            return True
        elif response.status_code == 404:
            print(f"Todo with ID {todo_id} not found.")
        else:
            self.log_error(f"Failed to update todo {todo_id}", response)
        return False

    def log_error(self, message, response):
        """Log an error with details from the response."""
        print(f"{message}: {response.status_code}, {response.text}")

    @task(2)
    def delete_group(self):
        """Test deleting a group."""
        with self.lock:
            if not self.group_ids:
                print("No group IDs available for deletion.")
                return

            group_id = random.choice(self.group_ids)
            if self.delete_group_by_id(group_id):
                self.group_ids.remove(group_id)

    @task(4)
    def list_todos(self):
        """Test listing all todos."""
        response = self.client.get("/list/todos/")
        if response.status_code == 200:
            todos = response.json()
            print(f"Successfully fetched {len(todos)} todos.")
        else:
            print(
                f"Failed to fetch todos: {
                    response.status_code}, {response.text}"
            )

    @task(2)
    def get_grouped_todos(self):
        """Test fetching grouped todos."""
        response = self.client.get("/get/grouped/todos")
        if response.status_code == 200:
            print("Successfully fetched grouped todos.")
        else:
            self.log_error("Failed to fetch grouped todos", response)

    @task(2)
    def delete_todo(self):
        """Test deleting a todo."""
        with self.lock:
            if not self.todo_ids:
                print("No todo IDs available for deletion.")
                return

            todo_id = random.choice(self.todo_ids)
            if self.delete_todo_by_id(todo_id):
                self.todo_ids.remove(
                    todo_id)  # Remove the deleted todo_id from the list

    @task(2)
    def update_todo(self):
        """Test updating a todo."""
        with self.lock:
            if not self.todo_ids:
                print("No todo IDs available for updating.")
                return

            todo_id = random.choice(self.todo_ids)
            self.update_todo_by_id(todo_id)

    @task(3)  # Adjust weight as needed
    def create_group(self):
        """Test creating a group."""
        payload = {
            "name": f"Test Group {random.randint(1, 1000)}",
            "description": "This is a test group created for load testing."
        }

        response = self.client.post("/create/groups/", json=payload)
        if response.status_code == 200:
            group = response.json()
            print(f"Successfully created group: {group}")
            with self.lock:
                self.group_ids.append(
                    group["id"])  # Add the new group ID to the list
        else:
            self.log_error("Failed to create group", response)
