import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    with open(sys.argv[1], newline="") as csvfile:
        database = list(csv.reader(csvfile))
        STRs = database[0][1:]

    with open(sys.argv[2], "r") as sequencefile:
        sequence = sequencefile.read()

    STR_counts = [longest_match(sequence, STR) for STR in STRs]

    for row in database[1:]:
        name = row[0]
        profile = list(map(int, row[1:]))
        if STR_counts == profile:
            print(name)
            return

    print("No match")


def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run


main()
