class Boop:
    def __enter__(self):
        print("Entering...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")

with Boop():
    print("hi")
    assert False