import pandas as pd

def handle_test():
    fruit = pd.DataFrame([['I liked it', 'Pretty good'], ['It was awful', 'Bland']],
                         columns=['Bob', 'Sue'],
                         index=['Product A', 'Product B'])
    print(fruit, end="\n\n")
    fruit.to_csv("fruits.csv")
    print(fruit.loc[[True, False]], end='\n\n')

    ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
                            index=['Flour', 'Milk', 'Eggs', 'Spam'],
                            name='Dinner')
    print(ingredients)
    ingredients.to_csv("ingredients.csv")

    return "fruits.csv", "ingredients.csv"

def csv_test(file):
    df = pd.read_csv(file, index_col=0)
    #print('\nDATASET: \n', df)
    #print('\nDATASET: \n', df.loc[5:10, ['country', 'province', 'region_1', 'region_2']])
    #df.set_index('points')
    df.gropby('points')
    print(df)


handle_test()

csv_test('../pandas/data/winemag-data_first150k.csv')


import pandas as pd

