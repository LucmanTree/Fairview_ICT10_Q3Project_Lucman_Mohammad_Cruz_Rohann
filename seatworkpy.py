from pyscript import document
def registrationconfirmation(e):
    # Check if the "Yes" radio button for registration is selected
    Yes = document.getElementById("registrationconfirmation1").checked
    No = document.getElementById("registrationconfirmation2").checked
    # If the student is registered, return True
    if Yes:
        return True
    else:
        return False

def medicalclearance(e):
    # Check if the "Yes" radio button for medical clearance is selected
    Yes = document.getElementById("medicalclearance1").checked
    No = document.getElementById("medicalclearance2").checked
    # If medically cleared, return True
    if Yes:
        return True
    else:
        return False

def gradelevelandsection(e):  
    # Check which grade level is selected
    g7 = document.getElementById("7").checked
    g8 = document.getElementById("8").checked
    g9 = document.getElementById("9").checked
    g10 = document.getElementById("10").checked
    # Check which section is selected
    Sapphire = document.getElementById("SAPPHIRE").checked
    Emerald = document.getElementById("EMERALD").checked
    Ruby = document.getElementById("RUBY").checked
    Topaz = document.getElementById("TOPAZ").checked
    Jade = document.getElementById("JADE").checked

    # Grade 7 team assignments
    if g7 and Sapphire:
        return ("Green Hornets", "#1e7f43")
    if g7 and Emerald:
        return ("Yellow Tigers", "#facc15")
    if g7 and Ruby:
        return ("Red Bulldogs", "#dc2626")
    if g7 and Topaz:
        return ("Blue Bears", "#1f4ed8")
    if g7 and Jade:
        return ("Green Hornets", "#1e7f43")
    # Grade 8 team assignments
    if g8 and Sapphire:
        return ("Green Hornets", "#1e7f43")
    if g8 and Emerald:
        return ("Yellow Tigers", "#facc15")
    if g8 and Ruby:
        return ("Red Bulldogs", "#dc2626")
    if g8 and Topaz:
        return ("Blue Bears", "#1f4ed8")
    if g8 and Jade:
        return ("Green Hornets", "#1e7f43")
    # Grade 9 team assignments
    if g9 and Sapphire:
        return ("Green Hornets", "#1e7f43")
    if g9 and Emerald:
        return ("Yellow Tigers", "#facc15")
    if g9 and Ruby:
        return ("Red Bulldogs", "#dc2626")
    if g9 and Topaz:
        return ("Blue Bears", "#1f4ed8")
    if g9 and Jade:
        return ("Green Hornets", "#1e7f43")
    # Grade 10 team assignments
    if g10 and Sapphire:
        return ("Green Hornets", "#1e7f43")
    if g10 and Emerald:
        return ("Yellow Tigers", "#facc15")
    if g10 and Ruby:
        return ("Red Bulldogs", "#dc2626")
    if g10 and Topaz:
        return ("Blue Bears", "#1f4ed8")
    if g10 and Jade:
        return ("Green Hornets", "#1e7f43")
    # If no valid grade and section combination is selected
    return None

def run_all(e=None):
    # Get the output div where results will be displayed
    output = document.getElementById("output")

    # Check registration status
    if not registrationconfirmation(e):
        output.innerHTML = "❌ Not registered online"
        return

    # Check medical clearance
    if not medicalclearance(e):
        output.innerHTML = "❌ Not medically cleared"
        return

    # Determine team based on grade and section
    team = gradelevelandsection(e)
    if team is None:
        output.innerHTML = "❌ Please select grade and section"
        return

    # Display the final result
    name, color = team
    output.innerHTML = f"✅ You are eligible!<br>You are <b>{name}</b>"
    output.style.background = color
    output.style.color = "white"
    output.style.padding = "10px"

# Run the program when the "Check" button is clicked
document.getElementById("runAll").onclick = run_all
