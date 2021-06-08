from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns


def plot_variable_pairs(df, cols):
    ''' 
    This function takes in a dataframe of columns and performs
    a pairplot.
    '''
    sns.pairplot(df[cols], corner=True, kind='reg', plot_kws={'line_kws':{'color':'red'}})
    plt.show()

def months_to_years(df):
    '''
    This function takes in the tenure in months and converts it to completed years
    with a new feature called 'tenure_years'.
    '''
    df['tenure_years'] = (df['tenure'] / 12).astype(int)
    return df

def plot_categorical_and_continuous_vars(df, cat_var, cont_var):
    '''
    This function takes in a datafram, a categorical variable and a continuous variable,
    then generates 3 plots - box, bar and swarm.
    '''
    sns.catplot(x=cat_var, y=cont_var, data=df, kind='box')
    
    sns.catplot(x=cat_var, y=cont_var, data=df, kind='bar')
    
    sns.catplot(x=cat_var, y=cont_var, data=df, kind='swarm')


def data_split(df):
    '''
    This function takes in the  data and 
    performs a split.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test