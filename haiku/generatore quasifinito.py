from random import choice
from guizero import *
from json import load


def extract(filename):
    with open("%s.json" % filename, "r") as outfile:
        return load(outfile)
                               
app=App(title="Generatore di Haiku")
intro=Text(app, text="Benvenuto su Generatore di Haiku!")
bottone=PushButton(app, text="genera Haiku", command=extract)


def generate(json):
    return "\n".join(
        [
            str(choice(json["verso %s" % str(i)]))
            for i in range(1, len(json.items()) + 1)
            ]
        )


if __name__ == "__main__":
    json = extract("haiku")
    haiku = generate(json)
    print(haiku)

app.display()

