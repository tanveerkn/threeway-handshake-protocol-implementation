import random
from bson import objectid
import pickle
from passlib.hash import sha512_crypt as CryptContext

class Verifier():
    def attr_gen(self):
        a_1 = 0
        a_2 = 1
        share_common = -(random.randint(1, 1000))
        share_0 = -(share_common)
        share_1 = share_0 + 1
        x=objectid()
    def encryption(self):
        uid = ObjectId()
        env1 = str(enc(0)) + str(enc(share_0)) + str(uid)
        env2 = str(enc(1)) + str(enc(share_1)) + str(uid)
    def sig_gen(self):
        CryptContext.encrypt(env1)
        CryptContext.encrypt(env2)
    def sig_ver(self):
        CryptContext.verify(password, 'password')
    def decryption(self):


    def attr_ver(self):

