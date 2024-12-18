
# 0x0A. Prime Game

## Overview

This project challenges you to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. In this game, two players (Maria and Ben) take turns removing prime numbers and their multiples from a set of consecutive integers. The player who cannot make a move loses the game. The task is to determine the winner of each round based on the optimal plays made by both players.

## Project Requirements

- **Allowed Editors:** vi, vim, emacs
- **Interpreted/Compiled on:** Ubuntu 20.04 LTS using Python 3.4.3
- **PEP 8 Compliance:** Your code should adhere to the PEP 8 style guide (version 1.7.x)
- **File Endings:** All files must end with a new line
- **Executable Files:** All files should be executable

## Task Details

**Prototype:**
`def isWinner(x, nums)`
Where:

- `x` is the number of rounds.
- `nums` is a list containing the number `n` for each round.

The goal is to determine the player who won the most rounds. If the winner cannot be determined, return `None`.

## Gameplay Description

Maria and Ben are playing the game with a set of consecutive integers from `1` to `n`. Each player, starting with Maria, takes turns choosing a prime number from the set. After a prime is selected, that number and its multiples are removed from the set. The player who cannot make a move loses the game.

---

### Example

#### Input

```python
x = 3
nums = [4, 5, 1]
```

**First round (n = 4):**

```text
Maria picks 2 and removes 2, 4, leaving 1, 3.
Ben picks 3 and removes 3, leaving 1.
Ben wins as Maria cannot make a move.
```

**Second round (n = 5):**

```text
Maria picks 2 and removes 2, 4, leaving 1, 3, 5.
Ben picks 3 and removes 3, leaving 1, 5.
Maria picks 5 and removes 5, leaving 1.
Maria wins as Ben cannot make a move.
```

**Third round (n = 1):**

```text
Ben wins as there are no prime numbers left for Maria to choose.
```

**Result:**

Ben has the most wins.

**Code Example:**

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

**Output:**

`Winner: Ben`

---

## Concepts Covered

- **Prime Numbers:** Understanding prime numbers and efficient algorithms for identifying them.
- **Sieve of Eratosthenes:** An efficient algorithm to find all prime numbers up to a given limit.
- **Game Theory:** Strategic decision-making and optimal play for competitive games.
- **Dynamic Programming/Memoization:** Optimizing game state calculations for multiple rounds.
- **Python Programming:** Using loops, conditional statements, arrays, and lists for implementing the game logic.

---

### Visual Representation

Below is an image illustrating the concept of prime numbers and the game's rules:

```markdown
![Prime Numbers](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Prime_number_spiral_0_100.gif/500px-Prime_number_spiral_0_100.gif)
```

---

## Author

- _Refiloe Radebe_
