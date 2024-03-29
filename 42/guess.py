import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
        the following errors when applicable:
        'Please enter a number'
        'Should be a number'
        'Number not in range'
        'Already guessed'
        If all good, return the int"""
        guess = input()
        try:
            guess_int = int(guess)
        except:
            raise ValueError("Please enter a number")

        if guess_int in self._guesses:
            raise ValueError("Already guessed")
        elif guess_int < 1 or guess_int > 20:
            raise ValueError("Number not in range")
        else:
            self._guesses.add(guess_int)

        return guess_int

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
        {guess} is correct!
        {guess} is too low
        {guess} is too high
        Return a boolean"""
        if guess > self._answer:
            print(f"{guess} is too high")
        elif guess < self._answer:
            print(f"{guess} is too low")
        else:
            print(f"{guess} is correct!")
            return True
        return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
        see the tests for the exact win/lose messaging"""
        guess_count = 0
        while not self._win and guess_count < 5:
            try:
                guess = self.guess()
            except ValueError as e:
                print(e.args[0])
                continue

            if self._validate_guess(guess):
                self._win = True
                print(f"It took you {guess_count+ 1} guesses")
            guess_count += 1

        if not self._win:
            print(f"Guessed 5 times, answer was {self._answer}")
            ...


if __name__ == "__main__":
    game = Game()
    game()
