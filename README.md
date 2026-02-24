# Inventory-ListOfServices Microservice Overview

`main.py` provides a text prompt UI for viewing/updating items and setting alerts

`inventory.py` runs as a background worker that processes requests and triggers alerts.

 `potato.txt` is an example item file containing the current quantity for the item "potato".

**Files**
- **`main.py`**: CLI front-end. Prompts the user to view (`v`), update (`u`) or set an alert (`a`) for an item. Communicates with `inventory.py` via files (requests/responses).

- **`inventory.py`**: Background worker. Watches for request files, performs reads/writes on individual item files (ex., `potato.txt`), manages `alerts.txt`, and writes notification files when thresholds are triggered.

- **`potato.txt`**: Example item file containing a numeric quantity (currently `12`). Create additional `<item>.txt` files to add items.

**Running**
1. Open two terminals in this folder.
2. In the first terminal run the background worker:

```
python inventory.py
```

3. In the second terminal run the CLI front-end:

```
python main.py
```

Interact with the CLI using the prompts.

**Communication Contract**

- `view-request.txt`: single line containing the item name to view (ex., `potato`).

- `view-response.txt`: single line containing the numeric quantity or a short error message (ex., `Item does not exist`).

- `update-request.txt`: two lines: first the item name, second the new numeric quantity (ex., `potato\n5`).

- `update-response.txt`: single line with success or error status (ex., `Quantity updated successfully`).

- `alert-request.txt`: two lines: item name, threshold (number) (ex., `potato\n3`).

- `alert-set-status.txt`: status message indicating whether the alert was set, or why it failed.

- `alerts.txt`: persistent list of active alerts; each line is `name,threshold`.

- `alert-notification.txt`: single line human-readable notification written when an alert triggers (ex,, `Alert: potato quantity is below 3`).
