script="hey this is vijay"
encoded_script=script.encode("utf-8")
decoded_script=encoded_script.decode("utf-8")

print(f"Without encoding : {script}")
print(f"With encoding : {encoded_script}")
print(f"With decoding : {decoded_script}")