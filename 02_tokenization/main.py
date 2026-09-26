import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there, my name is Vijay Jadon"

tokens = enc.encode(text)
print("Tokens:", tokens)


