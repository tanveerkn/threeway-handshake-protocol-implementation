from Voter import Voter
import random

for no in range(10):
    new_voter = Voter()
    new_voter.cast_vote(random.randint(0, 1))
