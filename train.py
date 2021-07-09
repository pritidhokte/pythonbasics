class train:
    def __init__(self, name, fare, seat):
        self.name = name
        self.fare = fare
        self.seat = seat

    def getstatus(self):
        print("the train name is:", self.name)
        print("available seats:", self.seat)
        print("price of ticket is:", self.fare)

    def bookticket(self):
        if self.seat > 0:
            print("tickets has booked ad your seat_no is", self.seat)
            self.seat = self.seat - 1
        else:
            print("no seat")


intercity = train("intercity expreess", 60, 120)
intercity.getstatus()

intercity.bookticket()

intercity.getstatus()
intercity.bookticket()
