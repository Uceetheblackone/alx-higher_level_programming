#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 modoule."""
    import hidden_4

    for name in dir(hidden_4):
        if not name.startswith('__'):
            print(name)

