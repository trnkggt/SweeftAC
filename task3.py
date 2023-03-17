# Only does first 3 second
def bomberman(seconds, initial):
    dict_for_indexes = {}

    def main():
        # Step 1: find the positions of bombs
        for row in range(len(initial)):
            for col in range(len(initial[row])):
                if initial[row][col] == 'O':
                    dict_for_indexes[row, col] = True

        # Step 2: add the bombes
        for row in range(len(initial)):
            for col in range(len(initial[row])):
                if initial[row][col] != 'O':
                    initial[row][col] = 'O'

        # Step 3: Explode the initial bombes
        for row, col in dict_for_indexes.keys():

            if row == 0 and col == 0:
                initial[row][col] = ''
                initial[row + 1][col] = ''
                initial[row][col + 1] = ''
            elif row == 0:
                if col == len(initial[row]) - 1:
                    initial[row][col] = ''
                    initial[row + 1][col] = ''
                    initial[row][col - 1] = ''
                else:
                    initial[row][col] = ''
                    initial[row + 1][col] = ''
                    initial[row][col - 1] = ''
            elif row == len(initial) - 1 and col == len(initial[row]) - 1:
                initial[row][col] = ''
                initial[row - 1][col] = ''
                initial[row][col - 1] = ''
            elif row == len(initial) - 1:
                initial[row][col] = ''
                initial[row - 1][col] = ''
                initial[row][col - 1] = ''
                initial[row][col + 1] = ''
            else:
                if col == len(initial[row]) - 1:
                    initial[row][col] = ''
                    initial[row + 1][col] = ''
                    initial[row - 1][col] = ''
                    initial[row][col - 1] = ''

                else:
                    initial[row][col] = ''
                    initial[row + 1][col] = ''
                    initial[row][col + 1] = ''
                    initial[row - 1][col] = ''
                    initial[row][col - 1] = ''

    if seconds % 3 == 0:
        for i in range(0, seconds, 3):
            main()

            print(initial)


bomberman(9, [["X", "X", "X"],
              ["X", "O", "X"],
              ["X", "X", "X"]
              ])

