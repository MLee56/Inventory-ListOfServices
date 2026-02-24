import sys
import time
import os

while True:
    # check alerts first
    if os.path.exists("alert-notification.txt"):
        with open("alert-notification.txt", "r", encoding="utf-8") as f:
            message = f.read().strip()
        print(message)
        os.remove("alert-notification.txt")

    user_input = input("Enter 'v' to check inventory or 'u' to update inventory or 'a' to set alert: ")

    if user_input == "v":
        name = input("Enter Item Name: ").strip()
        with open("view-request.txt", 'w', encoding="utf-8") as f:
            f.write(name)

        time.sleep(2)
        if os.path.exists("view-response.txt"):
            with open("view-response.txt", "r", encoding="utf-8") as f:
                data = f.read().strip()
            print(data)
            os.remove("view-response.txt")
    elif user_input == "u":
        name = input("Enter Item Name: ").strip()
        newQuantity = input("Enter new quantity: ").strip()
        with open("update-request.txt", 'w', encoding="utf-8") as f:
            f.write(name + "\n")
            f.write(newQuantity)
        time.sleep(2)
        if os.path.exists("update-response.txt"):
            with open("update-response.txt", "r", encoding="utf-8") as f:
                data = f.read().strip()
            print(data)
            os.remove("update-response.txt")
    elif user_input == "a":
        name = input("Enter Item Name: ").strip()
        threshold = input("Enter threshold number: ").strip()

        with open("alert-request.txt", "w", encoding="utf-8") as f:
            f.write(name + "\n")
            f.write(threshold)
        time.sleep(2)
        if os.path.exists("alert-set-status.txt"):
            with open("alert-set-status.txt", "r", encoding="utf-8") as f:
                data = f.read().strip()
            print(data)
            os.remove("alert-set-status.txt")
    else:
        sys.exit()

