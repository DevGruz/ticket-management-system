def create_event(events):
    try:
        event_name = input("Enter the event name: ")
        total_tickets = int(input("Enter the total number of tickets: "))
        if total_tickets <= 0:
            raise ValueError("Total number of tickets must be a positive integer.")
        events[event_name] = {"total_tickets": total_tickets, "attendees": {}}
        print("Event created successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def purchase_ticket(events):
    try:
        event_name = input("Enter the event name: ")
        if event_name in events:
            available_tickets = events[event_name]["total_tickets"]
            num_tickets = int(
                input(f"Enter the number of tickets you want to buy (Available tickets: {available_tickets}): "))
            if num_tickets <= 0:
                raise ValueError("Number of tickets must be a positive integer.")
            if num_tickets > available_tickets:
                raise ValueError("Not enough tickets available.")
            attendee_name = input("Enter your name: ")
            events[event_name]["total_tickets"] -= num_tickets
            events[event_name]["attendees"].setdefault(attendee_name, 0)
            events[event_name]["attendees"][attendee_name] += num_tickets
            print(f"Tickets purchased successfully for {event_name}!")
        else:
            raise KeyError("Event not found.")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def view_ticket_details(events):
    print("Available events:")
    for event_name, event_info in events.items():
        available_tickets = event_info["total_tickets"]
        print(f"{event_name} - Available tickets: {available_tickets}")
    try:
        event_name = input("Enter the event name to view ticket details: ")
        if event_name in events:
            print(f"Attendee list for {event_name}:")
            for attendee, num_tickets in events[event_name]["attendees"].items():
                print(f"{attendee}: {num_tickets} ticket(s)")
        else:
            raise KeyError("Event not found.")
    except KeyError as e:
        print(f"Error: {e}")


def print_main_menu():
    print("\nMenu:")
    print("1. Create Event")
    print("2. Purchase Ticket")
    print("3. View Ticket Details")
    print("4. Exit the Program")


def main():
    events = {}  # Dictionary to store events and ticket counts

    while True:
        print_main_menu()
        choice = input("Select an option: ")

        if choice == "1":
            create_event(events)
        elif choice == "2":
            purchase_ticket(events)
        elif choice == "3":
            view_ticket_details(events)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please select an option from the menu.")


if __name__ == "__main__":
    main()
