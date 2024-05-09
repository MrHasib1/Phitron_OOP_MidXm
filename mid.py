class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().__init__()
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)

        seat = []

        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append(0)
            seat.append(row)

        self.__seats[id] = seat

    def book_seats(self,id, seat_list):
        if id not in self.__seats:
            print('Show id not found', id)
            return
        
        for i in seat_list:
            if (i[0] < 0 or i[0] >= self.__rows) or (i[0] < 0 or i[1] >= self.__cols):
                return f'{i} is not valid'
            elif self.__seats[id][i[0]] [i[i]] is True:
                return f'Seat {i} is booked'
            else:
                self.__seats[id][i[0]] [i[i]] = True
                return f'seat is successfully booked'

    def show_list(self):
        print("Show list: ")
        for i in self.__show_list:
            print(f"ID: {i[0]}, Show Name: {i[1]}, time and date: {i[2]}")

    def view_available_seats(self, id):
        print()
        if id not in self.__seats:
            print(f"There is no show with id '{id}'")
            return -1
        else:
            print(f"Available Seats for the show with ID: {id} :")
            for i, row in enumerate(self.__seats[id]):
                for j, col in enumerate(row):
                    if j == 0:
                        if col == 0:
                            print("[", "0,", end = " ")
                        else:
                            print("[", "1,", end = " ")
                    elif j == len(self.__seats[id]) - 1:
                        if col == 0:
                            print("0", "]", end = " ")
                        else:
                            print("1", "]", end = " ")
                    else:
                        if col == 0:
                            print("0,", end = " ")
                        else:
                            print("1,", end = " ")
                print()
            return 1
        
hall_no_1 = Hall(15, 15, 1)

hall_no_1.entry_show(10001,"JAWAN","12 PM")
hall_no_1.entry_show(10002,"RA ONE"," 3 PM")
hall_no_1.entry_show(10003,"Master"," 6 PM")
hall_no_1.entry_show(10004,"Son Of Sattamurty"," 9 PM")

while True:
    print("--------Please select Option---------")
    print("1: View all Running Show")
    print("2: View available seat in show")
    print("3: Book a ticket in a show")
    print("4: Exits")

    option = int(input("Enter the option: "))

    print("\n\n\n")

    if option == 1:
        hall_no_1.show_list()
    elif option == 2:
        id = input("Enter the Id: ")
        hall_no_1.view_available_seats()
    elif option == 3:
        id = input("Enter the show ID: ")
        isValid = hall_no_1.view_available_seats(id)
        if isValid == -1:
            print("Try Again with a valid Show ID!")
        else:
            x = int(input("Enter the row no. of the seat (1 - 10) : "))
            y = int(input("Enter the column no. of the seat (1 - 10): "))
            x -= 1
            y -= 1
            seat_loaction = (x,y)
            text = hall_no_1.book_seats(id, [seat_loaction])
            print(text)
    elif option == 4:
        break
    else:
        print(f"{option} is an invalid option")




    
    