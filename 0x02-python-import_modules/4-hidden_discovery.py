#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for h in dir(hidden_4):
        if h[0] != "_" and h[1] != "_":
            print(h)
