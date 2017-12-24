from Verifier import Verifier
from Counter import Counter

class Voter():
    __v_server = Verifier()
    __c_server = Counter()

    def cast_vote(self, vote):
        yes, no = self.__v_server.genrate_vote()
        if vote == 1:
            self.__c_server.add_vote(yes)
        elif vote == 0:
            self.__c_server.add_vote(no)
        else:
            print "Invalid Input"
