from django.db import models

# Create your models here.


# When Django sees that we've created a new item class it will automatically create an items table when we make and run migrations
# The class itself won't do anything. We need to use class inheritance to give it some functionality
# Null and blank prevents items from being created without a name. Null prevents it from being created without a name and blank will make the fields a required one on forms
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Override the string method so we can see our item names instead of item object
    def __str__(self):
        return self.name