# =============================
# Charity Fund Management System
# Python Project for VS Code
# =============================

import os

donors = []
donations = []


# -----------------------------
# Add Donor
# -----------------------------
def add_donor():
    print("\n--- Add Donor ---")

    donor_id = input("Enter Donor ID: ")
    name = input("Enter Donor Name: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")

    donor = {
        "id": donor_id,
        "name": name,
        "phone": phone,
        "city": city
    }

    donors.append(donor)

    print("Donor Added Successfully!")


# -----------------------------
# View Donors
# -----------------------------
def view_donors():
    print("\n--- Donor List ---")

    if len(donors) == 0:
        print("No donors available.")
    else:
        for donor in donors:
            print("---------------------------")
            print("Donor ID :", donor["id"])
            print("Name     :", donor["name"])
            print("Phone    :", donor["phone"])
            print("City     :", donor["city"])


# -----------------------------
# Add Donation
# -----------------------------
def add_donation():
    print("\n--- Add Donation ---")

    donor_id = input("Enter Donor ID: ")

    found = False
    donor_name = ""

    for donor in donors:
        if donor["id"] == donor_id:
            found = True
            donor_name = donor["name"]

    if found == False:
        print("Donor not found!")
        return

    amount = float(input("Enter Donation Amount: "))
    purpose = input("Enter Purpose: ")

    donation = {
        "donor_id": donor_id,
        "donor_name": donor_name,
        "amount": amount,
        "purpose": purpose
    }

    donations.append(donation)

    print("Donation Added Successfully!")


# -----------------------------
# View Donations
# -----------------------------
def view_donations():
    print("\n--- Donation List ---")

    if len(donations) == 0:
        print("No donations available.")
    else:
        for donation in donations:
            print("---------------------------")
            print("Donor ID   :", donation["donor_id"])
            print("Donor Name :", donation["donor_name"])
            print("Amount     :", donation["amount"])
            print("Purpose    :", donation["purpose"])


# -----------------------------
# Total Collection
# -----------------------------
def total_collection():
    total = 0

    for donation in donations:
        total = total + donation["amount"]

    print("\nTotal Charity Fund Collected =", total)


# -----------------------------
# Search Donor
# -----------------------------
def search_donor():
    print("\n--- Search Donor ---")

    donor_id = input("Enter Donor ID: ")

    found = False

    for donor in donors:
        if donor["id"] == donor_id:
            found = True

            print("---------------------------")
            print("Donor ID :", donor["id"])
            print("Name     :", donor["name"])
            print("Phone    :", donor["phone"])
            print("City     :", donor["city"])

    if found == False:
        print("Donor not found!")


# -----------------------------
# Save Data to File
# -----------------------------
def save_data():
    file = open("charity_data.txt", "w")

    file.write("DONORS\n")

    for donor in donors:
        line = donor["id"] + "," + donor["name"] + "," + donor["phone"] + "," + donor["city"] + "\n"
        file.write(line)

    file.write("DONATIONS\n")

    for donation in donations:
        line = (
            donation["donor_id"] + "," +
            donation["donor_name"] + "," +
            str(donation["amount"]) + "," +
            donation["purpose"] + "\n"
        )

        file.write(line)

    file.close()

    print("Data Saved Successfully!")


# -----------------------------
# Load Data from File
# -----------------------------
def load_data():
    if os.path.exists("charity_data.txt") == False:
        return

    file = open("charity_data.txt", "r")

    lines = file.readlines()

    section = ""

    for line in lines:
        line = line.strip()

        if line == "DONORS":
            section = "donors"

        elif line == "DONATIONS":
            section = "donations"

        elif line != "":
            parts = line.split(",")

            if section == "donors":
                donor = {
                    "id": parts[0],
                    "name": parts[1],
                    "phone": parts[2],
                    "city": parts[3]
                }

                donors.append(donor)

            elif section == "donations":
                donation = {
                    "donor_id": parts[0],
                    "donor_name": parts[1],
                    "amount": float(parts[2]),
                    "purpose": parts[3]
                }

                donations.append(donation)

    file.close()


# -----------------------------
# Main Menu
# -----------------------------
def main():
    load_data()

    while True:
        print("\n==============================")
        print(" CHARITY FUND MANAGEMENT SYSTEM ")
        print("==============================")

        print("1. Add Donor")
        print("2. View Donors")
        print("3. Add Donation")
        print("4. View Donations")
        print("5. Total Collection")
        print("6. Search Donor")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_donor()

        elif choice == "2":
            view_donors()

        elif choice == "3":
            add_donation()

        elif choice == "4":
            view_donations()

        elif choice == "5":
            total_collection()

        elif choice == "6":
            search_donor()

        elif choice == "7":
            save_data()

        elif choice == "8":
            save_data()
            print("Thank You! Exiting Program.")
            break

        else:
            print("Invalid Choice! Try Again.")


# -----------------------------
# Program Start
# -----------------------------
main()