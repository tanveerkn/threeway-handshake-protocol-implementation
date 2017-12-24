import random
from bson import objectid
import pickle
from passlib.hash import sha512_crypt as CryptContext
from demo_gmpy2 import test_encrypt

class Verifier:
    __verifiers = []

    def __init__(self):
        self.__verifiers = pickle.load(open("verfierData.pickle", "rb"))

    def __add__voter(self, vote):
        self.__verifiers.append(vote)
        pickle.dump(self.__verifiers, open("verfierData.pickle", "wb"))

    def genrate_vote(self):
        a_1 = 0
        a_2 = 1
        share_common = -(random.randint(1, 1000))
        share_0 = -(share_common)
        share_1 = share_0 + 1
        uid = ObjectId()
        env1 = CryptContext.encrypt(str(enc(0)) + str(enc(share_0)) + str(uid))
        env2 = CryptContext.encrypt(str(enc(1)) + str(enc(share_1)) + str(uid))
        self.__add__voter((env1, 0))
        self.__add__voter((env1, 1))
        return env1, env2

    def verifyVote(self, verifyVote):
        vote = [vote[1] for vote in self.__verifiers if CryptContext.verify(vote[0], verifyVote)]
        return vote[0] if len(vote) > 0 else -1
