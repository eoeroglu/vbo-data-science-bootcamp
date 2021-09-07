
#########################
# ODEVLER
#########################

###############################################
# ÖDEV 1: Fonksiyonlara Özellik Eklemek.
###############################################

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    sns.countplot(x=dataframe[col_name], data=dataframe)
    plt.show()

# Görev: cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argumanla biçimlendirilebilir olsun.
# Not: Var olan özelliği de argumandan kontrol edilebilir hale getirebilirsiniz.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def cat_summary(dataframe, col_name="", plot=False):
    if col_name not in dataframe.columns:
        return print('Column \'%s\' could not be found in the dataframe!' % col_name)
    if col_name == "":
        cat_cols = [col for col in dataframe.columns if col in df.select_dtypes(include=['category','object']).columns]
    else:
        cat_cols = [col_name]
    for col in cat_cols:
        print(pd.DataFrame({col: dataframe[col].value_counts(),
                            "Ratio": 100 * dataframe[col].value_counts() / len(dataframe)}))
        print("##########################################")
    if plot:
        for col in cat_cols:
            sns.countplot(x=dataframe[col], data=dataframe)
            plt.show()

df = sns.load_dataset("tips")
cat_summary(df, col_name='aa')

# Fonksiyona arguman ile biçimlendirilebilen bir özellik eklemek ne demek?
# Örnek olarak aşağıdaki check_df fonksiyonuna argumanla biçimlendirilebilen 2 özellik eklenmiştir.
# Bu özelliler ile tail fonksiyonunun kaç gözlemi göstereceği ve quantile değerlerinin gösterilip gösterilmeyeceği
# fonksiyona özellik olarak girilmiştir ve bu özellikleri kullanıcı argumanlarla biçimlendirebilmektedir.


###############################################
# ÖDEV 2: Docstring.
###############################################
# Aşağıdaki fonksiyona 4 bilgi (uygunsa) barındıran numpy tarzı docstring yazınız.
# (task, params, return, example)
# cat_summary()

def cat_summary(dataframe, col_name="", plot=False):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                The dataframe to be calculated on.
        col_name: str, optional
                The name of the column to be calculated. If left blank, all columns of categorical type are calculated.
        plot: bool, optinal
                Variable that controls whether visualization is performed for each variable.

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("tips")
        cat_summary(df)
        cat_summary(df, col_name='sex')

    Notes
    ------
        By giving any column name, a column-specific operation can be performed, 
        or by leaving the col_name variable blank, the function can select categorical variables and perform operations on them.
        The function will raise a warning message if it cannot find the given col_name variable in the dataset.

    """
    if col_name not in dataframe.columns:
        return print('Column \'%s\' could not be found in the dataframe!' % col_name)
    if col_name == "":
        cat_cols = [col for col in dataframe.columns if col in df.select_dtypes(include=['category','object']).columns]
    else:
        cat_cols = [col_name]
    for col in cat_cols:
        print(pd.DataFrame({col: dataframe[col].value_counts(),
                            "Ratio": 100 * dataframe[col].value_counts() / len(dataframe)}))
        print("##########################################")
    if plot:
        for col in cat_cols:
            sns.countplot(x=dataframe[col], data=dataframe)
            plt.show()