from api import Mazak
import time
import random
from textual_image.renderable import Image
from rich.console import Console
import json



def parse_command(command):
    if command == "exit":
        raise SystemExit
    if command == "export_history":
        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)


console = Console()

if __name__ == "__main__":
    mazak = Mazak()
    print("==============Mazak v0.0.2===================")
    console = Console()
    console.print(Image("logoo.png"))
    history = {
    "messages": []
}
    try:
        while True:
            text = input("👤 ты (you) >")
            if text.startswith("/"):
                parse_command(text[1:])
                continue
            q = mazak.query(text)
            print("🤖 Mazak > думает...")
            time.sleep(random.uniform(0.5, 5)) # имитируем думающий процесс
            print(f"🤖 Mazak > {q.answer}")
            history["messages"].append({"message": text, "answer": q.answer})
            


    except KeyboardInterrupt:
        print("\n==============Mazak v0.0.2===================")
        