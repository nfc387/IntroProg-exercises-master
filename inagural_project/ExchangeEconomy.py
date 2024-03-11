
class ExchangeEconomyClass:
    
    # Define parameters for an exchange economy with two consumers

    def __init__(self, omega_1=[0.8,1-0.8], omega_2=[0.3,1-0.3], alpha=1/3, beta=2/3):
        "define two person exchange economy and define endowments for consumer A and B"

        self.omega_A1 = omega_1[0] # A's endowment of good 1
        self.omega_A2 = omega_2[0] # A's endowment of good 2
        
        self.omega_B1 = omega_1[1] # B's endowment of good 1
        self.omega_B2 = omega_2[1] # B's endowment of good 2

        self.alpha = alpha # Calibration parameter
        self.beta = beta # Calibration parameter

        self.p1 = 1 # price for item 1 -> optimize w.r.t
        self.p2 = 1 # sets price for item 2 to numeraire

    def utility_function(self, consumer):
        "defines the utility function, given who the consumer is"

        if consumer == "A": # goods and calibration for consumer A
            x_1 = self.omega_A1
            x_2 = self.omega_A2
            cal = self.alpha
            
        elif consumer == "B": # goods and calibration for consumer B
            x_1 = self.omega_B1
            x_2 = self.omega_B2
            cal = self.beta

        else:
            print("Error, consumer not defined")

        return x_1**cal * x_2**(1-cal) # utility calculation
    
    def goods_equilibrium(self, consumer):
        # Define the optimal solution for each consumer
        if consumer == "A":
            x_1star = self.alpha * (self.p1*self.omega_A1 + self.p2 * self.omega_A2)/self.p1
            

Economy1 = ExchangeEconomyClass()

print(Economy1.utility_function(consumer="B"))