import numpy as np

def average_diff(list_):
    '''平均差を計算して返す関数
        ※平均差：1次元データn個の散らばりの尺度 |xi - xj| / n^2

        Arguments:
            list (float): 数値の1次元リスト

        Returns:
            float: 平均差
    '''
    # データサイズの二乗
    squared_list_size = np.power(len(list_), 2)

    return np.sum(np.absolute([(x_i - x_j) / squared_list_size for x_i in list_ for x_j in list_]))


def gini_coefficient(list_):
    '''ジニ係数を計算して返す関数
        ※ジニ係数：平均差と平均値x_ave*2の比 |xi - xj| / 2 * n^2 * x_ave

        Arguments:
            list (float): 数値の1次元リスト

        Returns:
            float: 平均差
    '''
    # 1次元データの平均値
    x_ave = np.mean(list_)

    # データサイズの二乗 * 
    squared_list_size = np.power(len(list_), 2)

    return np.sum(np.absolute([(x_i - x_j) / (squared_list_size * x_ave * 2)  for x_i in list_ for x_j in list_])) 
    
 
# 実装時動確用            
def main():
    list_ = [0, 3, 3, 5, 5, 5, 5, 7, 7, 10]
    list_2 = [0, 1, 2, 3, 5, 5, 7, 8, 9, 10]
    list_3 = [3, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    print(average_diff(list_))
    print(gini_coefficient(list_))

if __name__ == '__main__':
    main()

