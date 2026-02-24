import time
import os

print("Test: View Inventory")
with open("view-request.txt", "w", encoding="utf-8") as f:
    f.write("potato")

time.sleep(2)

if os.path.exists("view-response.txt"):
    with open("view-response.txt", "r", encoding="utf-8") as f:
        print("Response:", f.read().strip())
    os.remove("view-response.txt")

print("\nTest: Update Inventory")
with open("update-request.txt", "w", encoding="utf-8") as f:
    f.write("potato\n50")

time.sleep(2)

if os.path.exists("update-response.txt"):
    with open("update-response.txt", "r", encoding="utf-8") as f:
        print("Response:", f.read().strip())
    os.remove("update-response.txt")

print("\nTest: Set Alert")
with open("alert-request.txt", "w", encoding="utf-8") as f:
    f.write("potato\n656")

time.sleep(2)

if os.path.exists("alert-set-status.txt"):
    with open("alert-set-status.txt", "r", encoding="utf-8") as f:
        print("Response:", f.read().strip())
    os.remove("alert-set-status.txt")

time.sleep(3)

print("\nTest: Alert notification")
if os.path.exists("alert-notification.txt"):
    with open("alert-notification.txt", "r") as f:
        print(f"Notification Received: {f.read()}")
