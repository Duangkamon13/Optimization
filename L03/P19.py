"""
P19. Time-lapse math.
A function to compute the shooting interval for time-lapse photography.
"""

def time_int(event_period, viewing_speed, view_period):
    """
    Calculates the required shooting interval (tau) in minutes for a time-lapse video.

    Args:
        event_period (float): The total duration of the event in hours (T).
        viewing_speed (int): The playback speed of the video in frames per second (f).
        view_period (float): The desired length of the time-lapse video in seconds (P).

    Returns:
        float: The shooting interval (tau) in minutes.
    """
    # Step 1: Calculate the total number of frames needed (N)
    # N = f * P
    num_frames = viewing_speed * view_period

    # Step 2: Convert the event period from hours to minutes
    # This is necessary because the final output needs to be in minutes
    event_period_minutes = event_period * 60

    # Step 3: Calculate the shooting interval (tau) in minutes
    # tau = T_minutes / N
    shooting_interval = event_period_minutes / num_frames

    return shooting_interval

if __name__ == '__main__':
    # Invocation example from the problem description
    T = 72  # hours
    f = 50  # fps
    P = 10  # seconds

    # Call the function and store the result
    tau = time_int(T, f, P)

    # Print the result in the required format
    print(tau, 'minutes')
