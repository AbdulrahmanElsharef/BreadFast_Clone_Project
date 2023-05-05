food app:
department model:
        name=
        image
        SLUG

    product model:
        name -chr
        price - float
        image-img
        department-one to many
        subtitle-text
        Description-text
        Information-text
        Availability(stock,sale,soon)-choice
        Shipping-char
        Weight-float
        Share on-fa-tw-inst   -url
        slug


    productimage model:
        product-one to many
        image

    productreview model:
        user-one to many
        product-one to many
        rate-intger
        review-text

blog app
    post model:
        author-one to many
        department -one to many
        date
        image
        title
        head_topic
        post
        Share on-fa-tw-inst - gmail -url
        Tag-taggit

order app:
    Order(models.Model):
        user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
        code = models.CharField(max_length=10,default=generate_code)
        order_time = models.DateTimeField(default=timezone.now)

     OrderDetail(models.Model):
            order = models.ForeignKey(Order,related_name='order_Detail',on_delete=models.CASCADE)
            product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
            quantity = models.IntegerField()
            price = models.FloatField()

settings app
    company model:
        name-chr
        logo img
        slogan chr
        Email url
        Phone chr
        Address text
        Open time chr
        fa-tw-inst - gmail url

     DeliveryFee
        name
        time

**fake data 
** admin customize account app #user login - sighn - up and reset password

#translations

create api - post man
debug tool bar
caching

    


