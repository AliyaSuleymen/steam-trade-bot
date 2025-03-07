from dataclasses import dataclass
from datetime import datetime

from steam_trade_bot.type import CurrencyValue


@dataclass
class Game:
    app_id: int
    name: str


@dataclass
class MarketItem:
    app_id: int
    market_hash_name: str
    market_fee: str | None
    market_marketable_restriction: int | None
    market_tradable_restriction: int | None
    commodity: bool

    def is_tradable(self) -> bool:
        return self.market_tradable_restriction != -1  # -1 means not tradable at all


@dataclass
class MarketItemInfo:
    app_id: int
    market_hash_name: str
    currency: int
    sell_listings: int
    sell_price: CurrencyValue | None
    sell_price_no_fee: CurrencyValue | None


@dataclass
class MarketItemOrders:
    app_id: int
    market_hash_name: str
    currency: int
    timestamp: datetime
    dump: str
    buy_count: int | None
    buy_order: CurrencyValue | None
    sell_count: int | None
    sell_order: CurrencyValue | None
    sell_order_no_fee: CurrencyValue | None


@dataclass
class MarketItemOrder:
    price: CurrencyValue
    quantity: int


@dataclass
class MarketItemNameId:
    app_id: int
    market_hash_name: str
    item_name_id: int


@dataclass
class MarketItemSellHistory:
    app_id: int
    market_hash_name: str
    currency: int
    timestamp: datetime
    history: str


@dataclass
class SellHistoryAnalyzeResult:
    app_id: int
    market_hash_name: str
    currency: int
    timestamp: datetime
    sells_last_day: int
    sells_last_week: int
    sells_last_month: int
    recommended: bool
    deviation: float | None
    sell_order: CurrencyValue | None
    sell_order_no_fee: CurrencyValue | None


@dataclass
class BuySellItem:
    account: str
    app_id: int
    market_hash_name: str
    currency: int
    enabled: bool
    amount: int
    buy_order: CurrencyValue
    sell_order: CurrencyValue
