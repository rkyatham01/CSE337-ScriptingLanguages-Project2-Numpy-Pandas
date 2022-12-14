# Run this script from the repository's root.
import os
import re
import pandas as pd
top200_movies_file = os.path.join('src', 'data', 'Top_200_Movies.csv')

#check
def get_movies_data():
    return pd.read_csv(top200_movies_file)

def get_movies_interval(y1, y2):

    if ((type(y1) != type(5)) or (type(y2) != type(5))):
        raise TypeError("They should be integers")

    if y1 > y2 or (y1 < 0) or (y2 < 0):
        raise ValueError("Impossible interval range")

    df = get_movies_data()
    newDF = df[(df["Year of Release"] >= y1) & (df["Year of Release"] <= y2)]
    dfFinal = newDF["Title"]
    return dfFinal

def get_rating_popularity_stats(index, type):
    errorMsg = 'Invalid index or type'
    df = get_movies_data()

    if index == 'Popularity Index':
        for i in df.index:
            convertThis = df.at[i, 'Popularity Index']
            newString = ''
            for c in convertThis:
                if c == ',':
                    continue
                else:
                    newString += c
            df.at[i, 'Popularity Index'] = float(newString)
        if type == 'count':
            check = df[index].count()
            finalNum = round(check,2)
            return finalNum
        elif type == 'mean':
            check = df[index].mean()
            finalNum = round(check,2)
            return finalNum
        elif type == 'median':
            check = df[index].median()
            finalNum = round(check,2)
            return finalNum
        elif type == 'min':
            check = df[index].min()
            finalNum = round(check,2)
            return finalNum
        elif type == 'max':
            check = df[index].max()
            finalNum = round(check,2)
            return finalNum
        else:
            return errorMsg
    elif index == 'Rating':
        if type == 'count':
            check = df[index].count()
            finalNum = round(check,2)
            return finalNum
        elif type == 'mean':
            check = df[index].mean()
            finalNum = round(check,2)
            return finalNum
        elif type == 'median':
            check = df[index].median()
            finalNum = round(check,2)
            return finalNum
        elif type == 'min':
            check = df[index].min()
            finalNum = round(check,2)
            return finalNum
        elif type == 'max':
            check = df[index].max()
            finalNum = round(check,2)
            return finalNum
        else:
            return errorMsg
    else:
        return errorMsg

def get_actor_movies_release_year_range(actor, upper, lower=0):
    if ((type(upper) != type(5)) or (type(lower) != type(5))):
        raise TypeError("They should be integers")

    if lower > upper or (lower < 0) or (upper < 0):
        raise ValueError("Interval is Impossible")

    df = get_movies_data().set_index('Title')
    df = df[(df["Year of Release"] >= lower) & (df["Year of Release"] <= upper) & (df["Movie Cast"].str.contains(actor))]
    df = df["Year of Release"]
    return df    
def get_actor_median_rating(actor):
    if actor == "":
        raise ValueError("actor is an empty string")
    if type(actor) != type('yo'):
        raise TypeError("actor is not a string")
    
    df = get_movies_data()
    df = df[(df["Movie Cast"].str.contains(actor))]
    if df.empty:
        return None
    medianOf = df['Rating'].median()
    return medianOf

def get_directors_median_reviews():
    df = get_movies_data()
    for i in df.index:
        convertThis = str(df.at[i, 'Number of Reviews'])
        newString = ''
        newNum = 0
        for c in convertThis:
            if c == "M":
                newNum = float(newString) * 1000000 #b/c its M
                break
            elif c == "K":
                newNum = float(newString) * 1000 #b/c its K
                break
            else:
                newString += c
        df.at[i, 'Number of Reviews'] = (newNum / 1000000)

    df = df.groupby(['Director'])['Number of Reviews'].median()
    return df
#df.loc[df.age_group == '(30,40]'].groupby(['Gender','Education']).DMDHHSIZ.median()
