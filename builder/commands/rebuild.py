import os
import shutil

from .run import main as run


def clear():
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)
        if item != 'venv':
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)


def main():
    clear()
    run()


if __name__ == '__main__':
    main()
