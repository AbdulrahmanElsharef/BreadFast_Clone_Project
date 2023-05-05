import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from faker import Faker
from faker_food import FoodProvider
import random
from food.models import *
from blog.models import *
from django.contrib.auth.models import User

# def  seed_Department(n):
#     fake=Faker()
#     NAME=['Meat',
# 'Vegetables',
# 'Fruit','Nut','Gifts',
# 'Berries',
# 'Ocean_Foods'
# 'Butter','Eggs',
# 'Fastfood',
# 'Onion',
# 'Papayan','Crisps',
# 'Oatmeal',
# 'Bananas']
#     IMAGE=['cat-1.jpg','cat-2.jpg','cat-3.jpg','cat-4.jpg','cat-5.jpg']
#     for _ in range(n):
#         Department.objects.create(
#             name=f" Fresh {NAME[random.randint(0,13)]} ",
#             image=IMAGE[random.randint(0,4)]
#         )
#     print(f' {n} seed_Department done')

# seed_Department(25)



    
    


#     ('InStock','InStock'),('Sold','Sold'),('Soon','Soon')

# def seed_Product(n):
#     fake=Faker()
#     fake.add_provider(FoodProvider)
#     IMAGE=[pd-1.jpg'product-1.jpg','product-2.jpg','product-3.jpg','product-4.jpg','product-5.jpg','product-6.jpg','product-7.jpg','product-8.jpg','product-9.jpg','product-10.jpg','product-11.jpg','product-12.jpg']
#     AVAILABLE=['InStock','Sold','Soon']
#     for _ in range(n):
#         Product.objects.create(
#     name=fake.vegetable(),
#     price=random.uniform(19.99,99.99),
#     image=IMAGE[random.randint(0,11)],
#     department=Department.objects.get(id=random.randint(2,27)),
#     subtitle=fake.text(max_nb_chars=300) ,
#     description=fake.text(max_nb_chars=1000) ,
#     information=fake.text(max_nb_chars=1000) ,
#     available=AVAILABLE[random.randint(0,2)],
#     shipping_days=random.randint(0,4),
#     Weight=random.uniform(0.10,9.99),
#         )
#     print(f' {n} seed_Product done')

# seed_Product(1000)
        
        
        
# def seed_ProductImage (n):
#     fake=Faker()
#     IMAGE=['pd-1.jpg','pd-2.jpg','pd-3.jpg','pd-4.jpg','pd-5.jpg','pd-6.jpg','product-1.jpg','product-2.jpg','product-3.jpg','product-4.jpg','product-5.jpg','product-6.jpg','product-7.jpg','product-8.jpg','product-9.jpg','product-10.jpg','product-11.jpg','product-12.jpg']
#     for _ in range(n):
#         ProductImage.objects.create(
#             product=Product.objects.get(id=random.randint(1,1000)),
#             image=IMAGE[random.randint(0,17)],
#         )
#     print(f' {n} ProductImage done')

# seed_ProductImage(4000)


# def seed_ProductReview (n):
#     fake=Faker()
#     for _ in range(n):
#         ProductReview.objects.create(
#             user=User.objects.get(id=1),
#             product=Product.objects.get(id=random.randint(1,1000)),
#             rate=random.randint(1,5),
#             review=fake.text(max_nb_chars=300) ,
#             )
#     print(f' {n} seed_ProductReview done')

# seed_ProductReview(2000)

# def seed_Post (n):
#     fake=Faker()
#     fake.add_provider(FoodProvider)
#     IMAGE=['blog-1.jpg','blog-2.jpg','blog-3.jpg','blog-4.jpg','blog-5.jpg','blog-6.jpg']
#     for _ in range(n):
#         Post.objects.create(
#             author=User.objects.get(id=1),
#             department=Department.objects.get(id=random.randint(2,27)),
#             image=IMAGE[random.randint(0,5)],
#             title=fake.name() ,
#             head_topic=fake.text(max_nb_chars=100) ,
#             post=fake.text(max_nb_chars=1000) ,
#             Tag=f"{fake.ethnic_category()},fresh food"
#         )
#     print(f' {n} seed_Post done')

# seed_Post(100)

# def seed_post_tag(n):
#     fake=Faker()
#     NAME=['Meat',
# 'Vegetables',
# 'Fruit','Nut','Gifts',
# 'Berries',
# 'Ocean_Foods'
# 'Butter','Eggs',
# 'Fastfood',
# 'Onion',
# 'Papayan','Crisps',
# 'Oatmeal',
# 'Bananas']
#     for _ in range(n):
#         tag=f"fresh {NAME[random.randint(0,13)]}"
#         post=Post.objects.get(id=random.randint(1,99))
#         post.Tag.add(tag)
#         post.save()
#     print(f' {n} seed_post_tag done')
        
# seed_post_tag(100)        
        
