"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self, first_name, last_name, email_address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s, %s, %s>" % (self.first_name, 
                                            self.last_name, 
                                            self.email_address)


def read_customers_from_file(filepath):
    """Read customers data and populate dictionary of customers.

    Dictionary will be {email_address: Customer object}
    """

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email_address,
         password) = line.strip().split("|")

        customers[email_address] = Customer(first_name,
                                     last_name,
                                     email_address,
                                     password)

    return customers


def get_by_email(email):
    """gets information about a customer by their email address"""

    return customers[email_address]