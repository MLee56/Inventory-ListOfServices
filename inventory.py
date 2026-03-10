import time
import os

while True:
    if os.path.exists("view-request.txt"):
        with open("view-request.txt", "r+", encoding="utf-8") as f:
            name = f.read().strip()
        os.remove("view-request.txt")
        if name:
            if os.path.exists(f'{name}.txt'):
                with open(f'{name}.txt', "r", encoding="utf-8") as f:
                    quantity = f.read().strip()
                    response = quantity
            else:
                response = "Item does not exist"
            with open("view-response.txt", "w", encoding="utf-8") as f:
                f.write(response)

    if os.path.exists("update-request.txt"):
        with open("update-request.txt", "r", encoding="utf-8") as f:
            name = f.readline().strip()
            newQuantity = f.readline().strip()
        os.remove("update-request.txt")
        if not name:
            response = "Item name is empty"
        elif not newQuantity.isnumeric():
            response = "Invalid quantity"
        elif os.path.exists(f'{name}.txt'):
            with open(f'{name}.txt', "w", encoding="utf-8") as f:
                f.write(newQuantity)
            response = "Quantity updated successfully"
        else:
            response = "Item does not exist"
        with open("update-response.txt", "w", encoding="utf-8") as f:
            f.write(response)

    if os.path.exists("alert-request.txt"):
        with open("alert-request.txt", "r", encoding="utf-8") as f:
            name = f.readline().strip()
            threshold = f.readline().strip()
        os.remove("alert-request.txt")
        if not os.path.exists(f'{name}.txt'):
            with open("alert-set-status.txt", "w", encoding="utf-8") as f:
                f.write("Cannot set an alert for an item that does not exist")
        else:
            if name and threshold.isnumeric():
                with open("alerts.txt", "a", encoding="utf-8") as f:
                    f.write(f"{name},{threshold}\n")
                with open("alert-set-status.txt", "w", encoding="utf-8") as f:
                    f.write("Alert set successfully")

    # checking if alert need to be triggered for an item.
    # If an alert is triggered, then remove it from the alerts.txt file
    if os.path.exists("alerts.txt"):
        with open("alerts.txt", "r", encoding="utf-8") as f:
            alerts = f.readlines()
        untriggered_alerts = []
        for alert in alerts:
            name, threshold = alert.strip().split(",")
            if not os.path.exists(f'{name}.txt'):
                untriggered_alerts.append(alert)
                continue
            with open(f'{name}.txt', "r", encoding="utf-8") as f:
                quantity = f.read().strip()
            if int(quantity) < int(threshold):
                with open("alert-notification.txt", "w", encoding="utf-8") as f:
                    f.write(f"Alert: {name} quantity is below {threshold}")
            else:
                untriggered_alerts.append(alert)
        with open("alerts.txt", "w", encoding="utf-8") as f:
            f.writelines(untriggered_alerts)
    time.sleep(2)
