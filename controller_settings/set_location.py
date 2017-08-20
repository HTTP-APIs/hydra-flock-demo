from flock_controller.mechanics.location import gen_Location, add_location

def main():
    """Set initial location of the central controller."""
    location = gen_Location("0.856901647439813,14.08447265625")
    add_location(location)


if __name__ == "__main__":
    main()
