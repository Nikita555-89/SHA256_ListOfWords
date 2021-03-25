#Python script to calculate the sha256 values of a list of words.



from hashlib import sha256
import time


def main():
    """main function to take input from users"""
    #Words List to hold words
    wordsList = []
    # Dictionary to hold the words and their hashes
    sha256Dict = {}

    # Prompting the user to enter words. Informing the user that 'Finish' will end the prompt """
    print("Enter words one after another. Enter 'Finish' when done")

    # Collecting words from prompts until user enters 'Finish'
    while True:
        word = input("Enter Word: ")
        if word.strip() == 'Finish':
            break
        else:
            wordsList.append(word)

    # Exit the program if the user did not enter any words
    if not wordsList:
        print("Please enter some words.")
        exit(1)

    print("\nWords Entered are " + ",".join(wordsList))

    # Calculating hash for the entered words and storing results in 'sha256Dict dictionary' """
    start_time = time.time()
    for word in wordsList:
        sha256Dict[word] = sha256HashFunc(word)

    # Printing the words and hashes from the dictionary """
    print("\n\nHash of the words are: ")
    for k, v in sha256Dict.items():
        print("{} : {}".format(k, v))

    # Printing the script execution time
    print("\nScript execution time is {} seconds".format(time.time() - start_time))


def sha256HashFunc(value):
    """take in content to be hashed and return corresponding sha256 Hash values"""
    return sha256(bytes(value, 'utf-8')).hexdigest()


main()
