
class PalindromChecker:

    def check_text(self, text):
        char_array = [char for char in text]

        stack = []

        for char in char_array:
            stack.append(char)

        for char in char_array:
            if char != stack.pop():
                print("FEHLER")
                return

        print("SUCCESS")



if __name__ == "__main__":
    palindromChecker = PalindromChecker()
    palindromChecker.check_text("hennah")