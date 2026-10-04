import tomllib

"""tomllib会按照字面量类型转成Python对应的类型"""
with open('config.toml', 'rb') as f:
    data = tomllib.load(f)
    print(data)
    print(type(data))
    if 'profiles' in data:
        for profile in data['profiles']:
            print(profile)
            print(type(profile['age']))
            print(f'type of age: {type(profile["height"])}')