class User:
    """
    class that generates new instances of user 
    """
    user_list=[]
    def __init__(self,first_name,last_name,password,conf_password):

        """
        _init_ methods that help us define properties for our new user object

        Args:
            first_name: New user first name 
            last_name: New user last name 
            password: New user password
            conf_password: New user password confirmation 
        """
        self.first_name= first_name
        self.last_name= last_name
        self.password= password
        self.conf_password= conf_password



