def available_seats(room):
    for row in room:
        for seat in row:
            if seat == "O":
                return True
    return False


def is_available_seat(row, column, room):
    if row > len(room) - 1:
        return False
    room_row = room[row]
    if room_row[column] == "O":
        return True
    return False


def available_percentage(room):
    total_seats = 0
    available_seats = 0
    for row in room:
        for seat in row:
            if seat == "O":
                available_seats += 1
            total_seats += 1
    return (available_seats / total_seats) * 100


def is_there_enough_space(m, room):
    available_seats = 0
    for row in room:
        for seat in row:
            if seat == "O":
                available_seats += 1
    return available_seats >= m


room = [
    ["X", "X", "X", "O", "O", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "O", "O", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "X", "O", "X", "O", "X"],
    ["X", "X", "X", "X", "O", "O", "O", "X", "X", "X"],
    ["O", "O", "X", "O", "O", "O", "X", "X", "X", "X"],
]

print(f"available_seats(room)\n{available_seats(room)}\n")

print(f"is_available_seat(2, 4, room)\n{is_available_seat(2, 4, room)}")
print(f"is_available_seat(10, 4, room)\n{is_available_seat(10, 4, room)}")
print(f"is_available_seat(0, 3, room)\n{is_available_seat(0, 3, room)}\n")

print(f"available_percentage(room)\n{available_percentage(room)}\n")

print(f"is_there_enough_space(20, room)\n{is_there_enough_space(20, room)}")
print(f"is_there_enough_space(5, room)\n{is_there_enough_space(5, room)}")
