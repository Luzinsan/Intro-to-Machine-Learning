import pandas as pd
#pd.set_option("display.max_rows", 3)
pd.set_option("display.max_columns", 11)
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
    print(df.columns)
    grouping_min = df.groupby(['country', 'province']).apply(lambda frame: frame.loc[frame.points.idxmax()])
    grouping_min_withoutloc = df.groupby(['country', 'province']).apply(lambda frame: frame.points.max())
    #print(grouping_min)
    #print(grouping_min_withoutloc)
    #grouping_by_points = df.groupby('country').apply(lambda frame: frame.loc[frame.points.idxmax()])
    countries_reviewed = df.groupby(['country', 'province']).price.agg([len, min, max])
    countries_reviewed = countries_reviewed.reset_index()
    countries_reviewed.sort_values(by=['len','max','country'],ascending=False)
    print(countries_reviewed)
    #grouping_by_points = grouping_by_points.reset_index()
    #print(grouping_by_points.groupby(['country']).price.agg([len,min,max]))

#handle_test()

csv_test('data/winemag-data-130k-v2.csv')