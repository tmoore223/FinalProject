# course: sdev 140
# author: moore, t
# date: 2021-09-25
# program: m06_assn2_ex3_mooretyler.py
# purpose: final project basic form

from tkinter import *

# import ttk for more modern visuals later on
from tkinter import ttk

# starts the Tk interpreter
root = Tk()

class OrderForm:
	def __init__(self, root):
		root.title('Bike Works (by TSM)')
		
		# defines the main window
		MainFrame = ttk.Frame(root)
		
		# defines the grid and configures rows/columns
		MainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight = 1)
		root.resizable(0, 0)
		ttk.Label(MainFrame, text='Bike Works').grid(column=1, row=0, sticky=(W, E))
		
		# each line with label and text entry box plus variable to store entry
		root.FullName = StringVar()
		lblFullName = ttk.Label(MainFrame, text='Full Name:').grid(column=0, row=1, sticky=W)
		txtFullName = ttk.Entry(MainFrame, width=40, textvariable=root.FullName)
		txtFullName.grid(column=1, row=1, sticky=(E))
		
		root.PhoneNumber = StringVar()
		lblPhoneNumber = ttk.Label(MainFrame, text='Phone Number:').grid(column=0, row=2, sticky=W)
		txtPhoneNumber = ttk.Entry(MainFrame, width=40, textvariable=root.PhoneNumber)
		txtPhoneNumber.grid(column=1, row=2, sticky=(W, E))
		
		root.StreetAddress = StringVar()
		lblStreetAddress = ttk.Label(MainFrame, text='Street Address:').grid(column=0, row=3, sticky=W)
		txtStreetAddress = ttk.Entry(MainFrame, width=40, textvariable=root.StreetAddress)
		txtStreetAddress.grid(column=1, row=3, sticky=(W, E))
		
		root.ZipCode = StringVar()
		lblZipCode = ttk.Label(MainFrame, text='Zipcode:').grid(column=0, row=4, sticky=W)
		txtZipCode = ttk.Entry(MainFrame, width=10, textvariable=root.ZipCode)
		txtZipCode.grid(column=1, row=4, sticky=W)
		
		root.EmailAddress = StringVar()
		lblEmailAddress = ttk.Label(MainFrame, text='Email Address:').grid(column=0, row=5, sticky=W)
		txtEmailAddress = ttk.Entry(MainFrame, width=40, textvariable=root.EmailAddress)
		txtEmailAddress.grid(column=1, row=5, sticky=W)
		
		# defines option frame with border for visability
		OptionsFrame = ttk.Frame(MainFrame, borderwidth=2, padding=5, relief='ridge')
		OptionsFrame.grid(column=0, row=6, columnspan=2, sticky=(N, S, E, W))
		
		lblOptions = ttk.Label(OptionsFrame, text='Options').grid(column=0, row=6, sticky=(W, E))
		
		# defines checkbox with boolean variable for selection
		root.InsuranceCheck = BooleanVar()
		lblInsurance = ttk.Label(OptionsFrame, text='Insurance:').grid(column=1, row=6, sticky=W)
		btnInsurance = ttk.Checkbutton(OptionsFrame, variable = root.InsuranceCheck, onvalue=True, offvalue=False)
		btnInsurance.grid(column=2, row=6, sticky=W)
		
		# defines each radio button and passes text to variable for later retrival
		root.BikeType = StringVar()
		lblBikeType = ttk.Label(OptionsFrame, text='Bike Type:').grid(column=0, row=7, sticky=W)
		btnRoadBike = ttk.Radiobutton(OptionsFrame, text='Road Bike', variable=root.BikeType, value='roadbike')
		btnRoadBike.grid(column=0, row=8, padx=(0,5), sticky=W)
		btnMountainBike = ttk.Radiobutton(OptionsFrame, text='Mountain Bike', variable=root.BikeType, value='mountainbike')
		btnMountainBike.grid(column=0, row=9, padx=(0,5), sticky=W)
		btnCruiserBike = ttk.Radiobutton(OptionsFrame, text='Cruiser Bike', variable=root.BikeType, value='cruiserbike')
		btnCruiserBike.grid(column=0, row=10, padx=(0,5), sticky=W)
		
		lblRentalDates = ttk.Label(OptionsFrame, text='Rental Dates').grid(column=1, row=7, sticky=E)
		
		# defines the date input labels and text entries
		root.StartDate = StringVar()
		lblStartDate = ttk.Label(OptionsFrame, text='Start Date:').grid(column=1, row=8, sticky=W)
		txtStartDate = ttk.Entry(OptionsFrame, width=10, textvariable=root.StartDate)
		txtStartDate.grid(column=2, row=8, sticky=W)
		
		root.EndDate = StringVar()
		lblEndDate = ttk.Label(OptionsFrame, text='End Date:').grid(column=1, row=9, sticky=W)
		txtEndDate = ttk.Entry(OptionsFrame, width=10, textvariable=root.EndDate)
		txtEndDate.grid(column=2, row=9, sticky=W)
	
		# defines the final buttons and placement
		btnOrder = ttk.Button(MainFrame, text='Order').grid(column=1, row=11)
		btnClear = ttk.Button(MainFrame, text='Clear').grid(column=2, row=11, columnspan=1, sticky=W)
		
		# pads out each widget in the main window
		for child in MainFrame.winfo_children():
			child.grid_configure(padx=5, pady=5)
			
		# sets cursor into first entry once program starts
		txtFullName.focus()
		
# define main with first window
def main():
	OrderForm(root)
	root.mainloop()


main()
