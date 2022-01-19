import wikipedia

page_title = input("Enter the page title: ")
while page_title != '':
    print(wikipedia.summary(f"{page_title}"))
    page_title = input("Enter the page title: ")
