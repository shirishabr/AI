room_a = input("Enter Room A status (DIRTY/CLEAN): ").upper()
room_b = input("Enter Room B status (DIRTY/CLEAN): ").upper()
position = input("Enter vacuum position (A/B): ").upper()

print("\n--- Vacuum Cleaner Actions ---")

if position == "A":

    if room_a == "DIRTY":
        print("SUCK")
        room_a = "CLEAN"

    if room_b == "DIRTY":
        print("MOVE RIGHT")
        position = "B"

        print("SUCK")
        room_b = "CLEAN"

    elif room_b == "CLEAN":
        print("MOVE RIGHT")
        position = "B"

elif position == "B":

    if room_b == "DIRTY":
        print("SUCK")
        room_b = "CLEAN"

    if room_a == "DIRTY":
        print("MOVE LEFT")
        position = "A"

        print("SUCK")
        room_a = "CLEAN"

    elif room_a == "CLEAN":
        print("MOVE LEFT")
        position = "A"

print("\n--- Final State ---")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Position:", position)
print("STOP")