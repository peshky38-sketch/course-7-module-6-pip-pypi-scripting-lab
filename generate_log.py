from datetime import datetime


def generate_log(data):
    # Validate that the input is a list.
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    # Create a filename using today's date.
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each log entry to the file.
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print a confirmation message.
    print(f"Log written to {filename}")


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)
