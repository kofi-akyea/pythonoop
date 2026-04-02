from controllers import TaskManagerController
from ui import CommandLineUI


def main():
    controller = TaskManagerController("Student")
    ui = CommandLineUI(controller)
    ui.run()


if __name__ == "__main__":
    main()
