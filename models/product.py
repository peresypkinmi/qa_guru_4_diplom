from dataclasses import dataclass


@dataclass
class Product:
    product_schema = {
        "Id": int,
        "IsActive": bool,
        "Code": int,
        "RegionId": int,
        "LanguageId": int,
        "IsBad": bool,
        "OraId": int,
        "IsArchived": bool,
        "Name": str,
        "NameShort": str,
        "IsOnlyOnline": bool,
        "IsSiteShow": bool,
        "UrlCode": str,
        "Status": bool,
        "Price": int,
        "CurrencyId": int,
        "Point": bool,
        "OldPrice": int,
        "ProductSaldo": {
            "Id": int,
            "ProductId": int,
            "ScladId": int,
            "Volume": int
        },
        "Weight": int
    }

    NameFull: str = ''
    Price: int = ''

    def get_name_full(self):
        if "Серия" in self.NameFull:
            line = self.NameFull.split(' Серия')
            self.NameFull = line[0]
        return self.NameFull

    def get_price(self):
        return self.Price
