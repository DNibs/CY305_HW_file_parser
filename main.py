"""
Author: CPT Niblick, David
Date: 2020 09 04
Deletes files where filename doesn't contain a name of a cadet from the "cadets.csv" list
"""

import os
import pandas as pd


dir_list = 'C:\\Users\\david.niblick\\OneDrive - West Point\\CY305\\AY211'
dir_hw = 'C:\\Users\\david.niblick\\OneDrive - West Point\\CY305\\AY211\\HWs\\DB4\\all_files'
fn_list = 'Niblick_cadet_list.csv'


if __name__ == '__main__':
    # get to directory
    os.chdir(dir_list)
    df_cdt_lst = pd.read_csv(fn_list, header=None)
    os.chdir(dir_hw)
    file_list = os.listdir()

    for fn in file_list:
        keep_flag = 0
        for index in df_cdt_lst.iterrows():
            name = index[1].values[0]
            if name in fn:
                keep_flag = 1
        if keep_flag == 0:
            # print(fn)
            os.remove(fn)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
