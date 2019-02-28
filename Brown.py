from nltk.corpus import brown
brown.categories()

cfd = nltk.ConditionalFreqDist(
           (genre,word)
            for genre in brown.categories()
            for word in brown.words(categories = genre))
genre = ['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tablulate(conditions = genre, samples = modals)