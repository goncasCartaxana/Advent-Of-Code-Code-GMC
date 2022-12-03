 # A giant Rock Paper Scissors tournament
 # Rock Paper Scissors is a game between two players.
 # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If same shape, it's a draw.
 # "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
 # The second column--" ?  X for Rock, Y for Paper, and Z for Scissors.
 # The score:
 # the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
 # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# txt File structure: "A Y\n" for every line

def PredictScoreRPS(filePath):
    file = open(filePath, "r")
    text = file.readlines()

    # SUM scores
    OponentsScore = 0
    PlayerScore = 0
    for line in text: # line[0] the other player move, line[2] our move.
        # Points for move
        # Oponnent
        if line[0] == "A":
            OponentsScore += 1
        elif line[0] == "B":
            OponentsScore += 2
        elif line[0] == "C":
            OponentsScore += 3
        # Player
        if line[2] == "X":
            PlayerScore += 1
        elif line[2] == "Y":
            PlayerScore += 2
        elif line[2] == "Z":
            PlayerScore += 3
        # Points for winning/Losing
        if line[0] == "A":# Rock
            if line[2] == "X": #X for Rock - Draw
                PlayerScore += 3
                OponentsScore += 3
            if line[2] == "Y": #Y for Paper - Win
                PlayerScore += 6
            if line[2] == "Z": #Z for Scissors - Loss
                OponentsScore += 6
        if line[0] == "B":# Paper
            if line[2] == "X": #X for Rock - Loss
                OponentsScore += 6
            if line[2] == "Y": #Y for Paper - Draw
                PlayerScore += 3
                OponentsScore += 3
            if line[2] == "Z": #Z for Scissors - Win
                PlayerScore += 6
        if line[0] == "C":# Scissors
            if line[2] == "X": #X for Rock - Win
                PlayerScore += 6
            if line[2] == "Y": #Y for Paper - Loss
                OponentsScore += 6
            if line[2] == "Z": #Z for Scissors - Draw
                OponentsScore += 3
                PlayerScore +=3
    return PlayerScore, OponentsScore




if __name__ == "__main__":
    file = "2 Dec RockPaperScissors Game.txt"
    PS, OS = PredictScoreRPS( file)
    print(f"Our score is {PS} and the Oponnet's score is {OS} ")