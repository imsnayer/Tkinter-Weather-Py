from Tkinter import *
import ttk, urllib2

#Tkinter Application
root = Tk()
root.title("Weather Grabber")
root.geometry('500x200+100+200')

#Application Specifications
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Functions
def main():
	global city
	city = cityVar.get()
	if " " in city:
		city = city.replace (" ", "_") #Swap Spaces with underscores for URL use
		grabWeather()
	else:
		grabWeather()

def grabWeather():
	state = stateVar.get()
	global city
	url = "http://api.wunderground.com/api/204df492f224d7c8/conditions/q/%s/%s.json" % (state, city)
	try:
		request = urllib2.Request(url)
		page = urllib2.urlopen(request).read()
		fahrenheitLine = page.split(",")
		fahrenheitParse = fahrenheitLine[45].split(":")
		fahrenheitValue.set(fahrenheitParse[1])
		celsiusLine = page.split(",")
		celsiusParse = celsiusLine[46].split(":")
		celsiusValue.set(celsiusParse[1])
	except urllib2.HTTPError, error:
		print "Error Loading Page"
		contents = error.read()

#Values
stateVar = StringVar(mainframe)
cityVar = StringVar(mainframe)
fahrenheitValue = StringVar(mainframe)
celsiusValue = StringVar(mainframe)

#Labels
titleLabel = ttk.Label(mainframe, text='Logan\'s Weather Grabber', foreground='#49ADE3')
stateLabel = ttk.Label(mainframe, text='State:', foreground='#49ADE3')
cityLabel = ttk.Label(mainframe, text='City:', foreground='#49ADE3')
fahrenheitLabel = ttk.Label(mainframe, text='Fahrenheit:', foreground='#49ADE3')
fahrenheitValueLabel = ttk.Label(mainframe, textvariable=fahrenheitValue)
celsiusLabel = ttk.Label(mainframe, text='Celsius:', foreground='#49ADE3')
celsiusValueLabel = ttk.Label(mainframe, textvariable=celsiusValue)

#Buttons
grabButton = Button(mainframe, text="Grab Weather", command=main, foreground='#49ADE3', background='#5C5C5C')

#Drop Down Menu
stateVar.set('  ')
stateOptionMenu = OptionMenu(mainframe, stateVar, 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY')

#City Input
cityEntry = ttk.Entry(mainframe, width=20, textvariable=cityVar)

#Layout
titleLabel.grid(row=1, column=3, sticky=(W, E))
stateLabel.grid(row=2, column=1, sticky=(E))
cityLabel.grid(row=2, column=4, sticky=(E))
fahrenheitLabel.grid(row=3, column=1, sticky=(W))
celsiusLabel.grid(row=3, column=4, sticky=(E))
stateOptionMenu.grid(row=2, column=2, sticky=(W))
cityEntry.grid(row=2, column=5, sticky=(W))
grabButton.grid(row=4, column=3, sticky=(W,E))
fahrenheitValueLabel.grid(row=3, column=2, sticky=(W, E))
celsiusValueLabel.grid(row=3, column=5, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
