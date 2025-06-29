import csv

def export_to_csv(users, filename="users_bmidata.csv"):
    if not users:
        return
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)
