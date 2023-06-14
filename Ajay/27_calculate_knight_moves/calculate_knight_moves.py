def calculate_knight_moves(m, n, x, y):
    # Define the possible knight moves
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    # Initialize the count of valid moves
    count = 0

    # Check each possible move
    for dx, dy in moves:
        # Calculate the new position
        new_x = x + dx
        new_y = y + dy

        # Check if the new position is within the board bounds
        if 0 <= new_x < m and 0 <= new_y < n:
            # Increment the count for a valid move
            count += 1

    return count
