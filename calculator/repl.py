import sys

class CalculatorREPL:
    def __init__(self):
        self.running = True

    def start(self):
        print("Welcome to the Advanced Python Calculator!")
        print("Type 'exit' to quit.")

        while self.running:
            try:
                command = input(">>> ").strip().lower()
                if command == "exit":
                    self.running = False
                else:
                    print(f"Unknown command: {command}")
            except KeyboardInterrupt:
                print("\nExiting calculator.")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    CalculatorREPL().start()

