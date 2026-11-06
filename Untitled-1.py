class TicketBookingSystem:
    def __init__(self, total_seats=10):
        self.total_seats = total_seats
        self.available_seats = list(range(1, total_seats + 1))
        self.bookings = {}

    def display_seats(self):
        print("\n--- Available Seats ---")
        print(self.available_seats)

    def book_ticket(self, name, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.bookings[seat_number] = name
            print(f"\nSuccess! Seat {seat_number} booked for {name}.")
        else:
            print(f"\nSorry, seat {seat_number} is already booked or invalid.")

    def view_bookings(self):
        print("\n--- Current Bookings ---")
        if not self.bookings:
            print("No bookings yet.")
        for seat, name in self.bookings.items():
            print(f"Seat {seat}: {name}")

# Main Program Loop
if __name__ == "__main__":
    system = TicketBookingSystem(total_seats=10)
    
    while True:
        print("\n=== Movie Ticket Booking System ===")
        print("1. View Available Seats")
        print("2. Book a Ticket")
        print("3. View All Bookings")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            system.display_seats()
        elif choice == '2':
            system.display_seats()
            try:
                seat = int(input("Enter seat number to book: "))
                name = input("Enter your name: ")
                system.book_ticket(name, seat)
            except ValueError:
                print("Please enter a valid number for the seat.")
        elif choice == '3':
            system.view_bookings()
        elif choice == '4':
            print("Thank you for using the Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")