# course: sdev 140
# author: moore, t
# date: 2021-09-26
# program: TSM_Validation.py
# purpose: bike rental validation module

class DataValidation():
	
	# only allows letters to be typed into the entry
	def NameVal(TypedInput, TypeAction):
		if TypeAction == '1':
			if not TypedInput.replace(' ', '').isalpha():
				return False
		return True
	
	# only allows numbers to be typed into the entry and a max of 5
	def ZipVal(TypedInput, TypeAction):
			if TypeAction == '1':
				if not TypedInput.isdigit():
					return False
				if len(TypedInput) > 5:
					return False
			return True
	
	# only allows numbers to be typed into the entry and a max of 10
	def PhoneVal(TypedInput, TypeAction):
		if TypeAction == '1':
			if not TypedInput.isdigit():
				return False
			if len(TypedInput) > 10:
				return False
		return True
	
	# only allows letters and numbers to be typed into the entry	
	def StreetVal(TypedInput, TypeAction):
		if TypeAction == '1':
			if not TypedInput.replace(' ', '').isalnum():
				return False
		return True
	
	# only allows letters to be typed into the entry with the exception of the '@' and '.' symbols
	def EmailVal(TypedInput, TypeAction):
		if TypeAction == '1':
			if not TypedInput.replace('@', '').replace('.', '').isalnum():
				return False
		return True
	

		