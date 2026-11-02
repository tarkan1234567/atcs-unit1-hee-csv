def countdown(n):
    # Base case
    if n <= 0:
        return

    # Current work
    print(n)

    # Recursive call with smaller problem
    countdown(n - 1)

countdown(5)
