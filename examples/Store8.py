#!/usr/bin/env python3

# ---------
# Store8.py
# ---------

class Price :
    def get_frequent_renter_points (self, days_rented) : # const
        return 1

class RegularPrice (Price) :
    def get_charge (self, days_rented) : # const
        result = 2
        if days_rented > 2 :
            result += (days_rented - 2) * 1.5
        return result

class NewReleasePrice (Price) :
    def get_charge (self, days_rented) : # const
        return days_rented * 3

    def get_frequent_renter_points (self, days_rented) : # const
        return 2 if (days_rented > 1) else 1

class ChildrensPrice (Price) :
    def get_charge (self, days_rented) : # const
        result = 1.5
        if days_rented > 3 :
            result += (days_rented - 3) * 1.5
        return result

class Movie :
    REGULAR     = RegularPrice()
    NEW_RELEASE = NewReleasePrice()
    CHILDRENS   = ChildrensPrice()

    def __init__ (self, title, price) :
        self.title = title
        self.set_price(price)

    """
    price
        get_charge()
    """
    def get_charge (self, days_rented) : # const
        return self.price.get_charge(days_rented)

    """
    price
        get_frequent_renter_points()
    """
    def get_frequent_renter_points (self, days_rented) :
        return self.price.get_frequent_renter_points(days_rented)

    def get_title (self) : # const
        return self.title

    def set_price (self, price) :
        self.price = price

class Rental :
    def __init__ (self, movie, days_rented) :
        self.movie       = movie
        self.days_rented = days_rented

    """
    movie
        get_charge()
    """
    def get_charge (self) : # const
        return self.movie.get_charge(self.days_rented)

    def get_days_rented (self) : # const # no longer used
        return self.days_rented

    """
    movie
        get_frequent_renter_points()
    """
    def get_frequent_renter_points (self) : # const
        return self.movie.get_frequent_renter_points(self.days_rented)

    def get_movie (self) : # const
        return self.movie

class Customer :
    def __init__ (self, name) :
        self.name    = name
        self.rentals = []

    def add_rental (self, rental) :
        self.rentals.append(rental)

    def get_name (self) : # const
        return self.name

    """
    iter(rentals).next()
        get_charge()
    """
    def get_total_charge (self) : # const, O(n)
        result = 0
        for each in self.rentals :
            result += each.get_charge()
        return result

    """
    iter(rentals).next()
        get_frequent_renter_points()
    """
    def get_total_frequent_renter_points (self) : # const, O(n)
        result = 0
        for each in self.rentals :
            result += each.get_frequent_renter_points()
        return result

    """
    iter(rentals).next()
        get_charge()
        get_movie()
            get_title()
    """
    def statement (self) : # O(n)
        result = "Rental Record for " + self.get_name() + "\n";
        for each in self.rentals :
            result += "\t" + each.get_movie().get_title() + "\t" + str(each.get_charge()) + "\n" # each.get_harge() again!
        result += "Amount owed is " + str(self.get_total_charge())                 + "\n"
        result += "You earned "     + str(self.get_total_frequent_renter_points()) + " frequent renter points";
        return result

print("Store8.py")

x = Customer("Penelope")
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "Amount owed is 0\n"                  + \
    "You earned 0 frequent renter points")

x.add_rental(Rental(Movie("Shane", Movie.REGULAR), 2))
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "Amount owed is 2\n"                  + \
    "You earned 1 frequent renter points")

x.add_rental(Rental(Movie("Red River", Movie.REGULAR), 5))
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "Amount owed is 8.5\n"                + \
    "You earned 2 frequent renter points")

x.add_rental(Rental(Movie("Giant", Movie.NEW_RELEASE), 1))
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "Amount owed is 11.5\n"               + \
    "You earned 3 frequent renter points")

x.add_rental(Rental(Movie("2001", Movie.NEW_RELEASE), 3))
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "Amount owed is 20.5\n"               + \
    "You earned 5 frequent renter points")

x.add_rental(Rental(Movie("Big Country", Movie.CHILDRENS), 3))
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "\tBig Country\t1.5\n"                + \
    "Amount owed is 22.0\n"               + \
    "You earned 6 frequent renter points")

x.add_rental(Rental(Movie("Spartacus", Movie.CHILDRENS), 5))
assert (x.statement() ==                    \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "\tBig Country\t1.5\n"                + \
    "\tSpartacus\t4.5\n"                  + \
    "Amount owed is 26.5\n"               + \
    "You earned 7 frequent renter points")

print("Done.")
