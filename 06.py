goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для ввода данных нажмите 'Enter', для вывода аналитики 'A'").upper()
    num += 1
    if control == 'A':
        print(f'Текущая аналитика')
        for key, value in analytics.items():
            print(f'{key}:{value}')
    for f in features.keys():
        feature_ = input(f'Введите наименование товара: "{f}"')
        features[f] = int(feature_)\
            if (f == 'цена' or f == 'количество')\
            else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
