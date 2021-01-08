class Iphone():
    def __init__(self, model, color, number ):
        self.model = model 
        self.color = color
        self.number = number
            super().__init__(phone_number):
            self.fingerprint = None

    
      def __str__(self):
        return f"This phone belongs to {self.phone_number}"

      def unlock(self, fingerprint=None):
        if (fingerprint == self.fingerprint):
    print("Phone unlocked because no fingerprint has not been set.")