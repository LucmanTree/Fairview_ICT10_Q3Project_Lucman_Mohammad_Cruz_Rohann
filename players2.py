from pyscript import document

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

 playerlist = document.getElementById("classmates")

    playerlist.innerHTML = ""

    for name in players:
        li = document.createElement("li")
        li.innerText = name
        player_list.appendChild(li) #this one inserts the list item into the webpage

