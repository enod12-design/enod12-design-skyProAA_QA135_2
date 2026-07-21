from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "IPhone 17", "+79253433444"),
    Smartphone("Xiaomi", "Redmi Note 14", "+79164545353"),
    Smartphone("Samsung", "Galaxy s26", "+79266266262"),
    Smartphone("Google", "Pixel 10", "+79154434343"),
    Smartphone("HUAWEI", "Mate 70 Pro", "+79253205454")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.phone_number}")
