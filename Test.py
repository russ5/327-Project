#########################################
# CMPE 327 - SOFTWARE QA | ASSIGNMENT 2
# Riley Wells
#########################################

class user:

    def __init__(self, privilege, tsf, vs):
        self.privilege = 0
        self.tsf = 'nothing'
        self.vs = 'nothing'

    # Setters, Getters

    def getPrivlige(self):
        return self.privilege

    def getTsf(self):
        return self.tsf

    def getVs(self):
        return self.vs

    def setPrivilege(self, privilege):
        self.privilege = privilege

    def logout(self):

    def createService(self, serviceNumber, date, serviceName):

    def deleteService(self, serviceNumber, serviceName):

    def sellTicket(self, serviceNumber, numTickets):


