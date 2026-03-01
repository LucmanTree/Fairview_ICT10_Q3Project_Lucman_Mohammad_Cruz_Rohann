from flask import Flask, render_template, request

classmates = [
"Balagat, Michael",
"Bernardo, Miko",
"Caguiron, Carriena",
"Calida, Lorenzo", 
"Chan, Jazmar",
"Cruz, Rohann",
"David, Antonio",
"De Guzman, Uno",
"De Guzman, Nia",
"Francisco, Annika",
"Kaur, Navjot",
"Laconsay, Heleina",
"Lepasana, Khen",
"Lopez, Liam",
"Lucman, Mohammad",
"Malapitan, Caleb",
"Manahan, Samantha",
"Manuel, Elyze",
"Mendoza, Matthew",
"Palafox, Coby",
"Ramirez, Alfiona",
"Reynoso, Izeck",
"Santos, Cas",
"Santos, Rafaela",
"Tolentino, Kelsey",
"Toribio, Sasha",
"Valdez, David",
]

@app.route("/", methods=["GET", "POST"])
def players():
    names_to_show = []

    if request.method == "POST":
        for name in classmates:
            names_to_show.append(name)

    return render_template("players.html", names=names_to_show)

if __name__ == "__main__":
    app.run(debug=True)
