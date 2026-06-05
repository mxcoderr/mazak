from api import Mazak

if __name__ == "__main__":
    mazak = Mazak()
    print("==============Mazak v0.0.1===================")

    try:
        while True:
            text = input("ты (you): ")
            q = mazak.query(text)
            print(f"Mazak 🤖: {q.answer}")

    except KeyboardInterrupt:
        print("\n==============Mazak v0.0.1===================")
        