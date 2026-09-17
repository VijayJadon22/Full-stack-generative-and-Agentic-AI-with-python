def serve_chai():
    yield "Cup1: Elaichi chai"
    yield "Cup2: Lemon chai"
    yield "Cup3: Masala chai"


stall = serve_chai()

# for cup in stall:
#     print(cup)


# normal function
def get_chai_list():
    return ["cup1", "cup2", "cup3"]


# Generator function
def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"


chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
