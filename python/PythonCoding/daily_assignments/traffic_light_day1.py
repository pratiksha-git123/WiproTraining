color = input("Enter color (Red/Yellow/Green): ").lower()
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid color")