class HotelManagement():
	def __init__(self):
		self.info = {}
		self.addhotel()

	def addhotel(self):
		hotelname = input("Enter Hotel hotelname: ")
		if self.info.get(hotelname, False):
			print("Hotel with same hotelname already exist!..")
			self.addhotelagain()
		else:
			self.info[hotelname]={}
			self.addroom(hotelname)

	def addroom(self, hotelname):
		roomnumber = input("Enter Room Number: ")
		self.info[hotelname][roomnumber]={"amenities": [], "amenitiesList": [], "cost": 0}
		i = 0
		while i < 5:
			self.addamenities(hotelname, roomnumber)
			i += 1
		self.addamenitiesagain(hotelname, roomnumber)


	def addAmenities(self, hotelname, roomNo):
		item = input("Enter the amenities hotelname: ")
		value = input("Enter amenities prize in $ (should be a number): ")
		self.info[hotelname][roomNo]["amenities"].append({item:value})
		self.info[hotelname][roomNo]["amenitiesList"].append(item)
		self.info[hotelname][roomNo]["cost"] += int(value)
		self.addamenitiesagain(hotelname, roomNo)


	def addhotelagain(self):
		add_hotel = input("Do you want to add New Hotel (Yes/No): ")
		if add_hotel.lower() == "yes":
			self.addhotel()
		elif add_hotel.lower() == "no":
			self.display()
		else:
			print("Invalid Input")
			self.addhotelagain()

	def addroomagain(self, hotelname):
		add_room = input("Do you want to add more Room(Yes/No): ")
		if add_room.lower() == "yes":
			self.addroom(hotelname)
		elif add_room.lower() == "no":
			self.addhotelagain()
		else:
			print("Invalid Input")
			self.addroomagain(hotelname)


	def addamenitiesagain(self, hotelname, roomNo):
		add_amenities = input("Do you want to add more amenities(Yes/No): ")
		if add_amenities.lower() == "yes":
			self.addAmenities(hotelname, roomNo)
		elif add_amenities.lower() == "no":
			self.addroomagain(hotelname)
		else:
			print("Invalid Input")
			self.addamenitiesagain(hotelname, roomNo)

	def display(self, budget=0):
		for hotel_hotelname, room_info in self.info.items():
			context = "\nRoom No {0} have the amenities like {1}, and room rent is ${2}."
			if budget == 0:
				info = '\n\n\n{0} Hotel have following rooms\n'.format(hotel_hotelname)
				for room, amenti_info in room_info.items():
					amenti = ', '.join(amenti_info['amenitiesList'])
					cost = amenti_info['cost']
					info += context.format(room, amenti, cost)
				print(info)
			else:
				info = '\n\n\n{0} Hotel have following rooms matching your budget\n'.format(hotel_hotelname)
				availability = False
				for room, amenti_info in room_info.items():
					cost = amenti_info['cost']
					if cost <= budget:
						amenti = ', '.join(amenti_info['amenitiesList'])
						availability = True
						info += context.format(room, amenti, cost)
				if availability:
					print(info)
				else:
					print("\n\n\nNo room available for your budget in hotel {0}".format(hotel_hotelname))
			print("\n***********************************************************\n")
		if budget == 0:
			self.getUserBudget()

	def getUserBudget(self):
		print("\n***********************************************************\n")
		budget = int(input("Please enter your budget: "))
		if budget > 1:
			self.display(budget)
		else:
			print("Invalid Budget range")
			self.getUserBudget()
			
HotelManagement()
