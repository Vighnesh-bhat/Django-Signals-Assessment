from django.db import models

#Question 1
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    

#Question 2
class Order(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()



#Question 3
class OrderLog(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)

