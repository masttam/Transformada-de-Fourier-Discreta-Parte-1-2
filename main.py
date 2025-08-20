import sys
from src.examen_p1 import run


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py examen_p1")
        sys.exit(1)

    task = sys.argv[1].strip().lower()
    if task == "examen_p1":
        run()
    else:
        print(f"Tarea desconocida: {task}")
        print("Uso: python main.py examen_p1")


if __name__ == "__main__":
    main()
