class Customers:
    def __init__(self, CustomerID, FirstName, LastName, Email, Phone, Address):
        self._CustomerID=CustomerID
        self._FirstName=FirstName
        self._LastName=LastName
        self._Email=Email
        self._Phone=Phone
        self._Address=Address

    @property
    def CustomerID(self):
        return self._CustomerID
    
    @CustomerID.setter
    def CustomerID(self, value):
        self._CustomerID = value

    @property
    def FirstName(self):
        return self._FirstName
    
    @FirstName.setter
    def CustomerID(self, value):
        self._FirstName = value

    @property
    def LastName(self):
        return self._LastName
    
    @LastName.setter
    def LastName(self, value):
        self._LastName = value

    @property
    def Email(self):
        return self._Email
    
    @Email.setter
    def Email(self, value):
        self._Email = value

    @property
    def Phone(self):
        return self._Phone
    
    @Phone.setter
    def Phone(self, value):
        self._Phone = value

    @property
    def Address(self):
        return self._Address
    
    @Address.setter
    def Address(self, value):
        self._Address = value