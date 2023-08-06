from djongo import models
from django.urls import reverse

class Category(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    _id = models.ObjectIdField()
    
    name = models.CharField(max_length=100)

    # Metadata

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class Product(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    _id = models.ObjectIdField()

    title = models.CharField(max_length=50, help_text='Enter field title')

    description = models.TextField(max_length=500, help_text="Enter description")

    price = models.FloatField(max_length=100, help_text="Enter price")

    image = models.CharField(max_length=500)

    # category = models.ArrayReferenceField(
    #     to=Category,
    #     on_delete=models.CASCADE
    # )
    # …

    # Metadata

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

class User(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    _id = models.ObjectIdField()

    user_name = models.CharField(max_length=100, blank=False)

    email = models.CharField(max_length=100, blank=False)

    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user_name

class Cart(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    _id = models.ObjectIdField()
    
    user_name = models.CharField(max_length=100, blank=False)

    product = models.ArrayField(
        model_container=Product
    )

    # Metadat

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user_name

# Cart Model:
# ■ id (integer, primary key)
# ■ user (integer)
# ■ products (array of integers)

# id (integer, primary key)
# ■ title (string)
# ■ description (text)
# ■ price (float)
# ■ image (string)
# ■ category (integer)

# User Model:
# ■ id (integer, primary key)
# ■ username (string)
# ■ email (string)
# ■ password (string)
