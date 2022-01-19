import wikipedia

page_title = input("Enter the page title: ")
while page_title != '':
    page = wikipedia.page(f'{page_title}')
    print(page.title)
    print(page.summary)
    print(page.url)
    page_title = input("Enter the page title: ")

print(wikipedia.search('Monty'))