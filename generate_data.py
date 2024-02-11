import numpy as np
import pandas as pd
from random import choice, randint


def load_lookups(colors='colors.csv', 
                 first_names='first_names.csv', 
                 last_names='last_names.csv', 
                 email_domains='email_domains.csv', 
                 brands='brands.csv'):
    '''Note: You need to know something about these data files.'''
    c = pd.read_csv(colors)
    f = pd.read_csv(first_names)
    l = pd.read_csv(last_names)
    e = pd.read_csv(email_domains)
    b = pd.read_csv(brands)
    
    return (c['favorite_color'].to_list(), 
            f['first_name'].to_list(), 
            l['last_name'].to_list(),
            e['email_domain'].to_list(),
            b['name'].to_list())


if __name__ == '__main__':

    colors, first_names, last_names, email_domains, brands = load_lookups()

    num_brands = len(brands)

    all_users = []

    # Full data set
    num_records = 33000000
    
    # Test data set
    # num_records = 330000

    for i in range(num_records):
        f=choice(first_names)
        l=choice(last_names)
        e=f'{f.lower()}.{l.lower()}@{choice(email_domains)}'
        all_users.append([f, l, e, choice(colors), randint(1945, 2002), True])

        if i%1000000 == 0:
            print(f'Wrote row {i} for user {e}')

    df = pd.DataFrame(all_users)
    df.columns = ['first_name', 'last_name', 'email', 'favorite_color', 'birth_year', 'is_adult']

    df.to_csv('table_users.csv', index_label='user_id')

    # =============================================================

    # These parameters will make about 168 relations for every 33 users and the
    # relations will be lognormally distributed
    mean, sd = 1.6, 0.45
    s = np.random.lognormal(mean, sd, len(df))
    relations = [int(i) for i in s]

    print(f'\nThere are {sum(relations)} relations')

    # For each relation, create a list of that size with an id on each one (will be user_id)
    # Then go back and randomly choose from brands to populate the list positions
    # This will be the table_user_brands table

    # ... then read both tables in, join, report out histogram


    user_brand = []
    for idx, i in enumerate(relations):
        user_id = idx

        # Get all the selections for this user
        # brand_choices = np.random.choice(brands, size=i)
        slice_start = randint(0, num_brands-1-i)
        brand_choices = brands[slice_start: slice_start+i]

        ub = list(zip([user_id]*i, brand_choices))

        # ub = [[user_id, 99] for _ in range(i)]

        user_brand.extend(ub)
        # print(f'Created {i} item list for user {user_id}: {ub}')
    
        if user_id%1000000 == 0:
            print(f'Wrote user brands for {idx} with {len(ub)} mappings')

    # print(user_brand)

    user_brand_df = pd.DataFrame(user_brand)
    user_brand_df.columns = ['user_id', 'brand_event_name']
    # print(user_brand_df)

    print('Writing table_user_brands.csv')
    user_brand_df.to_csv('table_user_brands.csv', index_label='user_brand_id')


    # Sample with this: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html