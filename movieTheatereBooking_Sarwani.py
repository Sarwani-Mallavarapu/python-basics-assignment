total_seats = 350
tickets_sold = 0
total_bookings = 0
rejected_bookings = 0

while True:
    tickets = int(input("Enter number of tickets (0 to exit): "))

    # break to exit booking system
    if tickets == 0:
        break

    # skip invalid ticket numbers
    if tickets < 0 or tickets > total_seats:
        print("Invalid ticket number")
        continue

    ages = []
    valid = True

    # for loop to check each person's age
    for i in range(tickets):
        age = int(input(f"Enter age of person {i+1}: "))
        ages.append(age)

        if age < 16:
            valid = False

    if valid:
        print(f"BOOKING CONFIRMED - {tickets} tickets")
        total_bookings += 1
        tickets_sold += tickets
        total_seats -= tickets
    else:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1

print("\nFinal Report:")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", total_seats)
