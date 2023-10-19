import library


if __name__ == '__main__':
    AbdighaniLibrary = library.Library(["Blood Meridian", "The Line of Beauty", "White Noise", "American Psycho", "The God of Small Things", "Americanah","Don Quixote"], "AbdighaniMD")

    while(True):
        print(f"Welcome to the {AbdighaniLibrary.name} Library. Enter your choice to continue")
        print("1. Display All Books owned by us")
        print("2. lend a book out")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Quit")

        print(" ")

        userChoice = input("<> ")

        if userChoice  not in ['1','2','3','4','5']:
            continue
        else:
            match userChoice:
                case "1":
                    print(" ")
                    AbdighaniLibrary.displayBook()
                    print(" ")
                case "2":
                    print(" ")
                    book = input("Enter the name of the book you: ")
                    user_name = input("Enter your name: ")
                    AbdighaniLibrary.lenBook(book, user_name)
                    print(" ")
                case "3":
                    print(" ")
                    book = input("Enter the name of the book you want to add: ")
                    AbdighaniLibrary.addBook(book)
                    print(" ")
                case "4":
                    print(" ")
                    book = input("Enter the name of the book you want to return ")
                    AbdighaniLibrary.returnBook(book)
                    print(" ")
                case "5":
                    print(" ")
                    print("Quit ")
                    break


