
class CashRegisterManager:

    def __init__(self):
        self.cash_list = []

    def open_cash(self, num):
        print(f"Open Cash {num}")

    def close_cash(self, num):
        print(f"Close Cash {num}")

    def get_num_open_cash(self):
        print(f"Calculate number of open cash")
        return 0


if __name__ == "__main__":
    manager = CashRegisterManager()
    manager.open_cash(1)
    manager.open_cash(2)
    manager.open_cash(1) # bereits geöffnet, hier passiert nichts

    manager.close_cash(2)
    manager.close_cash(3) # noch gar nicht geöffnet, kann nicht geschlossen werden

    num_open_cash = manager.get_num_open_cash()
    print(f"Open Cash {num_open_cash}") #1

    manager = CashRegisterManager()
    print(f"Open Cash {num_open_cash}") #1
