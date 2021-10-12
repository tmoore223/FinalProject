# course: sdev 140
# author: moore, t
# date: 2021-09-26
# program: mooretylerFinalProject.py
# purpose: bike rental program

from tkinter import *

# import ttk for more modern visuals later on
from tkinter import ttk

# pull DateEntry for easier date selection
from tkcalendar import DateEntry

# loads timedelta to figure the amount of days between rental period
from datetime import timedelta

# custom module for data validation
import TSM_Validation

# used to set current file location for file loading
import os
CurrentDir = os.path.abspath(__file__)
DirName = os.path.dirname(CurrentDir)
os.chdir(DirName)

# starts the Tk interpreter
root = Tk()

class OrderForm(Frame):
	
	def __init__(self, root):
		root.title('Bike Works (by TSM)')
		
		# defines the main window
		MainFrame = ttk.Frame(root)
		
		# sets style for the windows
		s = ttk.Style()
		s.configure('TFrame', background='#71b6f0')
		s.configure('TRadiobutton', background='#71b6f0')
		s.configure('TCheckbutton', background='#71b6f0')
		
		# defines the grid and configures rows/columns
		MainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight = 1)
		root.resizable(0, 0)
		
		# creates the images and displays them on window
		root.imgLogo = PhotoImage(file='BikeWorksLogo.png', name='logo')
		lblMainLabel = Label(MainFrame, image='logo', bg='#71b6f0').grid(column=0, row=0)
		root.imgPic = PhotoImage(file='BikeWorksPic.png', name='bike')
		lblPic = Label(MainFrame, image='bike', bg='#71b6f0').grid(column=1, row=0)
		
		# label for displaying any error messages or other information
		root.ErrorMessage = StringVar()
		lblError = ttk.Label(MainFrame, text='', foreground='red', background='#71b6f0', font=('',14), textvariable=root.ErrorMessage)
		lblError.grid(column=0, row=11, columnspan=2, sticky=W)
	
		# each line with label and text entry box plus variable to store entry
		# also validates each key entered into entry boxes
		root.FullName = StringVar()
		root.lblFullName = ttk.Label(MainFrame, text='Full Name:', background='#71b6f0')
		root.lblFullName.grid(column=0, row=1, sticky=W)
		txtFullName = ttk.Entry(MainFrame, width=40, textvariable=root.FullName, validate='key')
		txtFullName['validatecommand'] = (txtFullName.register(TSM_Validation.DataValidation.NameVal),'%P', '%d')
		txtFullName.grid(column=1, row=1, sticky=(E))
		
		root.PhoneNumber = StringVar()
		root.lblPhoneNumber = ttk.Label(MainFrame, text='Phone Number:', background='#71b6f0')
		root.lblPhoneNumber.grid(column=0, row=2, sticky=W)
		txtPhoneNumber = ttk.Entry(MainFrame, width=40, textvariable=root.PhoneNumber, validate='key')
		txtPhoneNumber['validatecommand'] = (txtPhoneNumber.register(TSM_Validation.DataValidation.PhoneVal),'%P','%d')
		txtPhoneNumber.grid(column=1, row=2, sticky=(W, E))
		
		root.StreetAddress = StringVar()
		root.lblStreetAddress = ttk.Label(MainFrame, text='Street Address:', background='#71b6f0')
		root.lblStreetAddress.grid(column=0, row=3, sticky=W)
		txtStreetAddress = ttk.Entry(MainFrame, width=40, textvariable=root.StreetAddress, validate='key')
		txtStreetAddress['validatecommand'] = (txtStreetAddress.register(TSM_Validation.DataValidation.StreetVal),'%P','%d')
		txtStreetAddress.grid(column=1, row=3, sticky=(W, E))
		
		root.ZipCode = StringVar()
		root.lblZipCode = ttk.Label(MainFrame, text='Zipcode:', background='#71b6f0')
		root.lblZipCode.grid(column=0, row=4, sticky=W)
		txtZipCode = ttk.Entry(MainFrame, width=10, textvariable=root.ZipCode, validate='key')
		txtZipCode['validatecommand'] = (txtZipCode.register(TSM_Validation.DataValidation.ZipVal),'%P','%d')
		txtZipCode.grid(column=1, row=4, sticky=W)
		
		root.EmailAddress = StringVar()
		root.lblEmailAddress = ttk.Label(MainFrame, text='Email Address:', background='#71b6f0')
		root.lblEmailAddress.grid(column=0, row=5, sticky=W)
		txtEmailAddress = ttk.Entry(MainFrame, width=40, textvariable=root.EmailAddress, validate='key')
		txtEmailAddress['validatecommand'] = (txtEmailAddress.register(TSM_Validation.DataValidation.EmailVal),'%P','%d')
		txtEmailAddress.grid(column=1, row=5, sticky=W)
		
		# defines option frame with border for visability
		OptionsFrame = ttk.Frame(MainFrame, borderwidth=2, padding=5, relief='ridge')
		OptionsFrame.grid(column=0, row=6, columnspan=2, sticky=(N, S, E, W))
		
		lblOptions = ttk.Label(OptionsFrame, text='Options', background='#71b6f0').grid(column=0, row=6, sticky=(W, E))
		
		# defines checkbox with boolean variable for selection
		root.InsuranceCheck = BooleanVar()
		lblInsurance = ttk.Label(OptionsFrame, text='Insurance:', background='#71b6f0').grid(column=1, row=6, sticky=W)
		btnInsurance = ttk.Checkbutton(OptionsFrame, variable = root.InsuranceCheck, onvalue=True, offvalue=False)
		btnInsurance.grid(column=2, row=6, sticky=W)
		
		# defines each radio button and passes text to variable for later retrival
		root.BikeType = StringVar()
		root.lblBikeType = ttk.Label(OptionsFrame, text='Bike Type:', background='#71b6f0')
		root.lblBikeType.grid(column=0, row=7, sticky=W)
		root.btnRoadBike = ttk.Radiobutton(OptionsFrame, text='Road Bike', variable=root.BikeType, value='roadbike')
		root.btnRoadBike.grid(column=0, row=8, padx=(0,5), sticky=W)
		root.btnMountainBike = ttk.Radiobutton(OptionsFrame, text='Mountain Bike', variable=root.BikeType, value='mountainbike')
		root.btnMountainBike.grid(column=0, row=9, padx=(0,5), sticky=W)
		root.btnCruiserBike = ttk.Radiobutton(OptionsFrame, text='Cruiser Bike', variable=root.BikeType, value='cruiserbike')
		root.btnCruiserBike.grid(column=0, row=10, padx=(0,5), sticky=W)
		
		lblRentalDates = ttk.Label(OptionsFrame, text='Rental Dates', background='#71b6f0').grid(column=1, row=7, sticky=E)
		
		# defines the date input labels and text entries
		root.StartDate = StringVar()
		lblStartDate = ttk.Label(OptionsFrame, text='Start Date:', background='#71b6f0').grid(column=1, row=8, sticky=W)
		root.deStartDate = DateEntry(OptionsFrame, selectmode='day', textvariable=root.StartDate)
		root.deStartDate.grid(column=2, row=8)
		

		root.EndDate = StringVar()
		lblEndDate = ttk.Label(OptionsFrame, text='End Date:', background='#71b6f0').grid(column=1, row=9, sticky=W)
		root.deEndDate = DateEntry(OptionsFrame, selectmode='day', textvariable=root.EndDate)
		root.deEndDate.grid(column=2, row=9 )
		
		
		# defines the final buttons and placement
		root.btnApply = ttk.Button(MainFrame, text='Apply', command=self.apply, state='disabled')
		root.btnApply.grid(column=1, row=12)
		btnVerify = ttk.Button(MainFrame, text='Confirm', command=self.verify)
		btnVerify.grid(column=2, row=12)
		btnClear = ttk.Button(MainFrame, text='Clear', command=self.clear).grid(column=3, row=12, columnspan=1, sticky=W)
		
		# pads out each widget in the main window
		for child in MainFrame.winfo_children():
			child.grid_configure(padx=5, pady=5)
							
		# sets cursor into first entry once program starts
		txtFullName.focus()	
	
	# used to verify all data after entry
	def verify(self):
	
		# checks to make sure end date is not before the start date
		def DateCheck():
			end = root.deEndDate.get_date()
			start = root.deStartDate.get_date()
			if end >= start:
				root.ErrorMessage.set('')
				root.btnApply.state(['!disabled'])
			if end < start:
				root.btnApply.state(['disabled'])
				root.ErrorMessage.set('End must be later than start.')
		
		# checks to make sure each entry is not blank
		# if specs not met highlight and display error for each offending entry and disables apply button
		def EntryCheck():
			if len(root.FullName.get()) == 0:
				root.lblFullName['text'] = 'Full Name: *'
				root.lblFullName['foreground'] = 'red'
				root.btnApply.state(['disabled'])
				root.ErrorMessage.set('*cannot be blank')
			else:
				if len(root.FullName.get()) != 0:
					root.lblFullName['text'] = 'Full Name:'
					root.lblFullName['foreground'] = 'black'
			if len(root.PhoneNumber.get()) == 0:
				root.lblPhoneNumber['text'] = 'Phone Number: *'
				root.lblPhoneNumber['foreground'] = 'red'
				root.btnApply.state(['disabled'])
				root.ErrorMessage.set('*cannot be blank')
			else:
			
				# makes sure phone number is required length
				if len(root.PhoneNumber.get()) != 0:
					if len(root.PhoneNumber.get()) != 10:
						root.lblPhoneNumber['text'] = 'Phone Number: *'
						root.lblPhoneNumber['foreground'] = 'red'
						root.btnApply.state(['disabled'])
						root.ErrorMessage.set('*Phone number must be 10 digits')
					else:
						root.lblPhoneNumber['text'] = 'Phone Number:'
						root.lblPhoneNumber['foreground'] = 'black'
			if len(root.StreetAddress.get()) == 0:
				root.lblStreetAddress['text'] = 'Street Address: *'
				root.lblStreetAddress['foreground'] = 'red'
				root.btnApply.state(['disabled'])
				root.ErrorMessage.set('*cannot be blank')
			else:
				if len(root.StreetAddress.get()) != 0:
					root.lblStreetAddress['text'] = 'Street Address:'
					root.lblStreetAddress['foreground'] = 'black'
			if len(root.ZipCode.get()) == 0:
				root.lblZipCode['text'] = 'Zipcode: *'
				root.lblZipCode['foreground'] = 'red'
				root.btnApply.state(['disabled'])
				root.ErrorMessage.set('*cannot be blank')
			else:
			
				# makes sure zip code is required length
				if len(root.ZipCode.get()) != 0:
					if len(root.ZipCode.get()) != 5:
						root.lblZipCode['text'] = 'Zipcode: *'
						root.lblZipCode['foreground'] = 'red'
						root.ErrorMessage.set('*Not a valid zip code')
						root.btnApply.state(['disabled'])
					else:
						root.lblZipCode['text'] = 'Zipcode:'
						root.lblZipCode['foreground'] = 'black'
			if len(root.EmailAddress.get()) == 0:
				root.lblEmailAddress['text'] = 'Email Address: *'
				root.lblEmailAddress['foreground'] = 'red'
				root.btnApply.state(['disabled'])
				root.ErrorMessage.set('*cannot be blank')
			else:
				if len(root.EmailAddress.get()) != 0:
				
					# checks to make sure the email address includes '@' and correct common top level domains
					if not '@' in root.EmailAddress.get():
						root.lblEmailAddress['text'] = 'Email Address: *'
						root.lblEmailAddress['foreground'] = 'red'
						root.ErrorMessage.set('*Not a valid email address')
						root.btnApply.state(['disabled'])
					elif not root.EmailAddress.get()[-4:] in '.com.org.edu.gov.net':
						root.lblEmailAddress['text'] = 'Email Address: *'
						root.lblEmailAddress['foreground'] = 'red'
						root.ErrorMessage.set('*Not a valid email address')
						root.btnApply.state(['disabled'])
					else:
						root.lblEmailAddress['text'] = 'Email Address:'
						root.lblEmailAddress['foreground'] = 'black'
			
			# checks to make sure a bike selection has been made
			if len(root.BikeType.get()) == 0:
				root.lblBikeType['text'] = 'Bike Type: *'
				root.lblBikeType['foreground'] = 'red'
				root.ErrorMessage.set('*Please make a bike selection')
				root.btnApply.state(['disabled'])
			else:
				if len(root.BikeType.get()) != 0:
					root.lblBikeType['text'] = 'Bike Type:'
					root.lblBikeType['foreground'] = 'black'
				
		DateCheck()
		EntryCheck()
		
			
	# clears any entrys from boxs and selections then displays message
	def clear(self):
		root.FullName.set('')
		root.PhoneNumber.set('')
		root.StreetAddress.set('')
		root.ZipCode.set('')
		root.EmailAddress.set('')
		root.InsuranceCheck.set(False)
		root.BikeType.set('')
		root.btnApply.state(['disabled'])
		root.ErrorMessage.set('Form Cleared')

	# after apply button is pressed creates new window	
	def apply(self):
		
		# defines the new window
		QuoteForm = Toplevel(root, bg='#71b6f0')
		QuoteForm.title('Bike Works Quote (by TSM)')
		QuoteForm.resizable(0, 0)
		
		# sets style for new window
		s = ttk.Style()
		s.configure('Frame2.TFrame', background='#71b6f0')
		s.configure('TRadiobutton', background='#71b6f0')
		s.configure('TCheckbutton', background='#71b6f0')
		
		# reuses named images for new window
		lblMainLabel = Label(QuoteForm, image='logo', bg='#71b6f0').grid(column=0, row=0, sticky=(W, E))
		lblPic = Label(QuoteForm, image='bike', bg='#71b6f0').grid(column=1, row=0, sticky=(W, E))
		
		# lays out all labels with the data from previous window
		root.FullNameData = root.FullName.get()
		root.lblFullName = ttk.Label(QuoteForm, text='Full Name:', background='#71b6f0')
		root.lblFullName.grid(column=0, row=1, sticky=W)
		lblFullNameData = ttk.Label(QuoteForm, width=40, text=root.FullNameData, background='#71b6f0')
		lblFullNameData.grid(column=1, row=1, sticky=(E))
		
		root.PhoneNumberData = root.PhoneNumber.get()
		root.lblPhoneNumber = ttk.Label(QuoteForm, text='Phone Number:', background='#71b6f0')
		root.lblPhoneNumber.grid(column=0, row=2, sticky=W)
		lblPhoneNumberData = ttk.Label(QuoteForm, width=40, text=root.PhoneNumberData, background='#71b6f0')
		lblPhoneNumberData.grid(column=1, row=2, sticky=(W, E))
		
		root.StreetAddressData = root.StreetAddress.get()
		root.lblStreetAddress = ttk.Label(QuoteForm, text='Street Address:', background='#71b6f0')
		root.lblStreetAddress.grid(column=0, row=3, sticky=W)
		lblStreetAddressData = ttk.Label(QuoteForm, width=40, text=root.StreetAddressData, background='#71b6f0')
		lblStreetAddressData.grid(column=1, row=3, sticky=(W, E))
		
		root.ZipCodeData = root.ZipCode.get()
		root.lblZipCode = ttk.Label(QuoteForm, text='Zipcode:', background='#71b6f0')
		root.lblZipCode.grid(column=0, row=4, sticky=W)
		lblZipCodeData = ttk.Label(QuoteForm, width=10, text=root.ZipCodeData, background='#71b6f0')
		lblZipCodeData.grid(column=1, row=4, sticky=W)
		
		root.EmailAddressData = root.EmailAddress.get()
		root.lblEmailAddress = ttk.Label(QuoteForm, text='Email Address:', background='#71b6f0')
		root.lblEmailAddress.grid(column=0, row=5, sticky=W)
		lblEmailAddressData = ttk.Label(QuoteForm, width=40, text=root.EmailAddressData, background='#71b6f0')
		lblEmailAddressData.grid(column=1, row=5, sticky=W)
		
		# pulls and displays choices from previous window and disables any changes
		root.BikePriceData = StringVar()
		lblBikePrice = ttk.Label(QuoteForm, text='Bike Price:', background='#71b6f0').grid(column=2, row=5)
		lblBikePriceData = ttk.Label(QuoteForm, textvariable=root.BikePriceData, background='#71b6f0').grid(column=3, row=5)
		
		root.InsurancePriceData = StringVar()
		lblInsurancePrice = ttk.Label(QuoteForm, text='Insurance Price:', background='#71b6f0').grid(column=2, row=6, rowspan=2, sticky=N)
		lblInsurancePriceData = ttk.Label(QuoteForm, textvariable=root.InsurancePriceData, background='#71b6f0').grid(column=3, row=6, rowspan=3, sticky=N)
		
		root.RentalPriceData = StringVar()
		lblRentalPrice = ttk.Label(QuoteForm, text='Rental Price:', background='#71b6f0').grid(column=2, row=7, rowspan=2, sticky=N)
		lblRentalPriceData = ttk.Label(QuoteForm, textvariable=root.RentalPriceData, background='#71b6f0').grid(column=3, row=7, rowspan=3, sticky=N)
		
		# defines option frame with border for visability
		OptionsFrame = ttk.Frame(QuoteForm, borderwidth=2, padding=5, relief='ridge')
		OptionsFrame.grid(column=0, row=6, columnspan=2, sticky=(N, S, E, W))
		
		lblOptions = ttk.Label(OptionsFrame, text='Options', background='#71b6f0').grid(column=0, row=6, sticky=(W, E))
		
		# pulls checkbox data from previous window
		root.InsuranceData = root.InsuranceCheck.get()
		lblInsurance = ttk.Label(OptionsFrame, text='Insurance:', background='#71b6f0').grid(column=1, row=6, sticky=W)
		btnInsurance = ttk.Checkbutton(OptionsFrame, variable = root.InsuranceCheck, onvalue=True, offvalue=False, state='disabled')
		btnInsurance.grid(column=2, row=6, sticky=W)
		
		# pulls radio button data from previous window
		root.BikeTypeData = root.BikeType.get()
		lblBikeType = ttk.Label(OptionsFrame, text='Bike Type:', background='#71b6f0').grid(column=0, row=7, sticky=W)
		btnRoadBike = ttk.Radiobutton(OptionsFrame, text='Road Bike', variable=root.BikeType, value='roadbike', state='disabled')
		btnRoadBike.grid(column=0, row=8, padx=(0,5), sticky=W)
		btnMountainBike = ttk.Radiobutton(OptionsFrame, text='Mountain Bike', variable=root.BikeType, value='mountainbike', state='disabled')
		btnMountainBike.grid(column=0, row=9, padx=(0,5), sticky=W)
		btnCruiserBike = ttk.Radiobutton(OptionsFrame, text='Cruiser Bike', variable=root.BikeType, value='cruiserbike', state='disabled')
		btnCruiserBike.grid(column=0, row=10, padx=(0,5), sticky=W)
		
		lblRentalDates = ttk.Label(OptionsFrame, text='Rental Dates', background='#71b6f0').grid(column=1, row=7, sticky=E)
		
		# pulls the date inputs from the previous windows
		root.StartDateData = root.deStartDate.get_date()
		lblStartDate = ttk.Label(OptionsFrame, text='Start Date:', background='#71b6f0').grid(column=1, row=8, sticky=W)
		lblStartDateData = ttk.Label(OptionsFrame, width=10, text=root.StartDateData)
		lblStartDateData.grid(column=2, row=8, sticky=W)
		
		root.EndDateData = root.deEndDate.get_date()
		lblEndDate = ttk.Label(OptionsFrame, text='End Date:', background='#71b6f0').grid(column=1, row=9, sticky=W)
		lblEndDateData = ttk.Label(OptionsFrame, width=10, text=root.EndDateData)
		lblEndDateData.grid(column=2, row=9, sticky=W)
		
		# sets up the buttons for ordering and displaying prices as well as exiting
		root.btnOrder = ttk.Button(QuoteForm, text='Order', state='disabled')
		root.btnOrder.grid(column=1, row=12, columnspan=2)
		
		# runs calculation module
		btnCalc = ttk.Button(QuoteForm, text='Calculate Price', command=lambda: self.PriceCalc(root.StartDateData, root.EndDateData))
		btnCalc.grid(column=2, row=12)
		btnQuit = ttk.Button(QuoteForm, text='Quit', command=root.destroy).grid(column=3, row=12)
	
	# determines the price of each option and displays them
	def PriceCalc(self, start, end):
		if root.BikeTypeData == 'roadbike':
			BikeCost = 45
			root.BikePriceData.set(f'${BikeCost} per day')
		if root.BikeTypeData == 'mountainbike':
			BikeCost = 35
			root.BikePriceData.set(f'${BikeCost} per day')
		if root.BikeTypeData == 'cruiserbike':
			BikeCost = 25
			root.BikePriceData.set(f'${BikeCost} per day')
		if root.InsuranceData == True:
			InsuranceCost = 5
			root.InsurancePriceData.set(f'${InsuranceCost} per day')
		if root.InsuranceData == False:
			InsuranceCost = 0
			root.InsurancePriceData.set(f'${InsuranceCost} per day')
		
		# counts how many days the rental period is 
		dates = []
		diff = (end-start).days
		for i in range(diff+1):
			day = start + timedelta(days=i)
			dates.append(day)
		
		# calculates the cost of the rental
		if dates != '':
			cost = (len(dates) * BikeCost) + (len(dates) * InsuranceCost)
			root.RentalPriceData.set(f'${cost} total')
		root.btnOrder.state(['!disabled'])


# define main with first window
def main():
	if __name__ == "__main__":
		OrderForm(root)
		root.mainloop()


main()
