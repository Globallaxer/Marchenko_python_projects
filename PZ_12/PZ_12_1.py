def analyze_car_exports():

    country_data = {}
    all_countries = set()

    num_countries = int(input("Введите количество стран: "))

    for _ in range(num_countries):
        country_name = input("Введите название страны: ")
        all_countries.add(country_name)

        num_brands = int(input(f"Введите количество марок автомобилей, экспортируемых в {country_name}: "))
        brands = set()
        for _ in range(num_brands):
            brand_name = input("Введите название марки: ")
            brands.add(brand_name)

        country_data[country_name] = brands

    # 1. Собираем все марки автомобилей, которые где-либо экспортируются
    all_brands = set()
    for country in country_data:
        all_brands.update(country_data[country])

    # 2. Определяем марки, экспортируемые во ВСЕ страны
    to_all = all_brands.copy()  # Начинаем с предположения, что все экспортируются во все
    for country in country_data:
        to_all.intersection_update(country_data[country]) # Пересечение с экспортом в каждую страну

    to_some = set()
    for country in country_data:
        to_some.update(country_data[country])
    to_some -= to_all  

    to_none = all_brands - to_some - to_all

    print("\nРезультаты:")
    print("Экспортируются во все страны:", to_all)
    print("Экспортируются в некоторые страны:", to_some)
    print("Не экспортируются ни в одну страну:", to_none)


analyze_car_exports()
