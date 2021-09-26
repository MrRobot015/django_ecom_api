#======== helper functions =======#

import random

def generate_session_token(length=10):
    """generate the session token to be used in user authentication"""
    session_token = ''.join(random.SystemRandom().choice(
        [chr(i) for i in range(97,129)] + 
        [str(i) for i in range(10)]) 
        for _ in range(length)
        )
    return session_token