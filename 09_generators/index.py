def serve_chai():
    yield "Cup1: Elaichi chai"
    yield "Cup2: Lemon chai"
    yield "Cup3: Masala chai"


stall = serve_chai()

for cup in stall:
    print(cup)
