menu = [("Suppe", "Tagessuppe von vorvorgestern", 2.3),
        ("Suppe deluxe", "Für die große Geldbörse", 1300.5),
        ("Spaghetti", "Spaghetti ala Susi und Strolch", 7.70)]

def write_entry(name, description, price):
    return ("  {0:<15}{1:<30}{2:>10,.2f} €").format(name, description, price)

def write_header(fill="*"):
    return ("{:" + fill[0] + "^60}\n").format(" Menu ")

def write_footer(fill="*"):
    return "\n" + 60 * fill[0]

def write_category(name):
    return "{0:^60}".format(name)

def write_spacer(fill="\U00002605"):
    return "{0:^60}".format(6 * fill)

# Create menu
string = [write_header("*")]

string.append(write_category("--Vorspeisen--"))

for item in menu[:-1]:
    string.append(write_entry(*item))

string.append(write_spacer())

string.append(write_category("\U0001F56F Candel-Light Dinner \U0001F56F"))

string.append(write_entry(*menu[2]))

string.append(write_spacer())

string.append(write_footer())

# Print menu
print("\n".join(string))
