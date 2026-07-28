import json
from pathlib import Path
from datetime import datetime

class TaskManager:
    def __init__(self, file="tasks.json"):
        self.file = Path(file)
        self.tasks = self._load()
    
    def _load(self):
        if self.file.exists():
            with open(self.file, 'r') as f:
                return json.load(f)
        return []
    
    def _save(self):
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add(self, description):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "done": False,
            "created": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self._save()
        print(f"✅ Added task #{task['id']}: {description}")
    
    def list(self):
        if not self.tasks:
            print("📭 No tasks")
            return
        for task in self.tasks:
            status = "✅" if task["done"] else "⬜"
            print(f"{status} #{task['id']}: {task['description']}")
    
    def done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self._save()
                print(f"✅ Task #{task_id} completed!")
                return
        print(f"❌ Task #{task_id} not found")
    
    def delete(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self._save()
        print(f"🗑️ Deleted task #{task_id}")

if __name__ == "__main__":
    import sys
    tm = TaskManager()
    
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py [add|list|done|delete] [args]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        tm.add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        tm.list()
    elif cmd == "done" and len(sys.argv) > 2:
        tm.done(int(sys.argv[2]))
    elif cmd == "delete" and len(sys.argv) > 2:
        tm.delete(int(sys.argv[2]))
    else:
        print("❌ Invalid command")
