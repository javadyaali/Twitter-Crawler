import pandas as pd


def writer(file_address, hashtags):
        l1 = hashtags['twitter']
        l2 = hashtags['insta']
        s1 = pd.Series(l1, name='Twitter')
        s2 = pd.Series(l2, name='Instagram')

        # Doing this because of ignoring different length of columns
        data_frame = pd.concat([s1,s2], axis=1)
        data_frame.to_csv(file_address, sep=',', encoding='utf8')
