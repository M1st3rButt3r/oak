from oak import run

while True:
    text = input("oak >")
    output, _error = run(text, "shell")
    if _error:
        print(_error)
    else:
        print(output)
