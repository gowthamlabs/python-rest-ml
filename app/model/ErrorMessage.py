class ErrorMessage:

    # def __init__(self, message):
        # ## initializing the attribute
        # self.message = message

    # @property
    # def message(self):
        # return self.message

    # ## the attribute name and the method name must be same which is used to set the value for the attribute
    # @message.setter
    # def message(self, message):
        # self.message = message
		
    def __init__(self):
        ## private varibale or property in Python
        self.message = "";

    ## getter method to get the properties using an object
    def get_message(self):
        return self.message

    ## setter method to change the value 'a' using an object
    def set_message(self, message):
        self.message = message