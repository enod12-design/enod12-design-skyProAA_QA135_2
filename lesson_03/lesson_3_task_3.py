from address import Address
from mailing import Mailing

from_addr = Address("101000",
                    "Moscow",
                    "Tverskay",
                    "1",
                    "2")

to_addr = Address("190000",
                  "Saint-Petersburg",
                  "Nevsky prospekt",
                  "13",
                  "14")

mailing = Mailing(to_address=to_addr,
                  from_address=from_addr,
                  cost=10000,
                  track="RU123456789CN")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment} "
    f"Стоимость {mailing.cost} рублей."
)
