def dif_files():
    with open('inFile_1.csv', 'r') as inFile_1:  # Read input files
        with open('inFile_2.csv', 'r') as inFile_2:
            file_1, file_2 = set(inFile_1), set(inFile_2)
            dif_1 = sorted(file_1 - file_2)  # find difference inFile_1 & inFile_2
            dif_2 = sorted(file_2 - file_1)  # find difference inFile_2 & inFile_1

    with open('outFile_1.csv', 'w') as outFile_1:
        with open('outFile_2.csv', 'w') as outFile_2:
            for line_1, line_2 in zip(dif_1, dif_2):
                outFile_1.write(line_1)
                outFile_2.write(line_2)


if __name__ == '__main__':
    dif_files()
