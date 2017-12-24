from Verifier import Verifier
import pickle


class Counter:
    verify_server = Verifier()

    def add_vote(self, vote):
        yes, no = pickle.load(open("votesCount.pickle", "rb"))
        new = self.verify_server.verifyVote(verifyVote=vote)
        if new == 0:
            no += 1
            print "Yes count : " + yes + "No count : " + no
        elif new == 1:
            yes += 1
            print "Yes count : " + yes + "No count : " + no
        else:
            print "inavalid vote"
        pickle.dump((yes, no), open("votesCount.pickle", "wb"))



