def display_disposal_history(disposal_history):
    """
    Given a disposal history as a list of tuples in the format (points, date), 
    display the points earned and the history for the disposal.
    """
    total_points = sum([points for points, _ in disposal_history])
    print(f"Total points earned: {total_points}\n")
    print("Disposal history:")
    for i, (points, date) in enumerate(disposal_history):
        print(f"{i+1}. {date}: {points} points")