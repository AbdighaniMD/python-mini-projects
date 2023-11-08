#install: "pip install wikipedia"
import wikipedia

def topicSummary():
    userQuery = str(input("Enter a topic name <> "))

    resultSummary = wikipedia.summary(userQuery)
    print(resultSummary)

def topicSearch():
    userQuery = str(input("Topic Search <> "))

    resultSearch = wikipedia.search(userQuery)
    print(resultSearch)

def wikipediaPage():
    userQuery = str(input("Search Wikipedia Page Name <> "))

    resultWikipediaPage = wikipedia.page(userQuery)
    print(resultWikipediaPage.title)
    print(resultWikipediaPage.url)



while(True):
    print("1.Topic Summary")
    print("2.Search by key words")
    print("3.Search by key words")
    print("4.EXIST")
    userQuery = str(input("Enter 1, 2, 3, or 4 <> "))

    match userQuery:
        case "1":
            topicSummary()
        case "2":
            topicSearch()
        case "3":
            wikipediaPage()           
        case "4": 
            print("Thank you for using Wiki")
            break


#topicSummary()
#topicSearch()

#wikipediaPage()


