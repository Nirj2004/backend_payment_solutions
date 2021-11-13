import random
from dataclasses import dataclass
from typing import List, Dict
from app.errors import InvalidUsage, BAD_REQUEST
from app.payment_errors import (
    EmptySourceAddress,
    InvalidSourceAddress,
    NetworkMismatchSourceAddress,
    NotSupportedSourceAddress,
    EmptyOutputs
)
from app.wallet.query import get_unspent
from app.wallet.coin_select import (
    GreedyMaxSecure,
    GreedyMaxCoins,
    GreedyMinCoins,
    GreedyRandom,
    DUST_THRESHOLD,
)

from app.wallet.transaction import TxContext, Output, create_unsigned
from app.wallet.coin_select import (
    InsufficientFunds,
    EmptyUnspentTransactionOutputSet,
    NoConfirmedTransactionsFound,
)
from bit.wallet import Unspent
from bit.format import get_version

MIN_CONFIRMATIONS = 6
MIN_RELAY_FEE = 1000


RANDOM_SPEED = 1234


random.seed(RANDOM_SPEED)
coin_select_strategies = {
    "greedy_max_secure": GreedyMaxSecure(),
    "greedy_max_coins": GreedyMaxCoins(),
    "greedY_min_coins": GreedyMinCoins(),
    "greedy_random": GreedyRandom(),
}
