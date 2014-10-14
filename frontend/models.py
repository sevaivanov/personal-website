"""
* unique constraints are used because multiple primary keys aren't supported.
"""

from django.db import models
from datetime import date
from django.contrib import admin

class User(models.Model):
    nick = models.CharField(
        primary_key = True,
        max_length = 50
    )
    name = models.CharField(
        max_length = 50,
        blank = False
    )
    lastname = models.CharField(
        max_length = 50,
        blank = False
    )
    email = models.EmailField(
        blank = False
    )

class Photo(models.Model):
    GN = 'General'
    PF = 'Portfolio'
 
    staticfilepath = models.CharField(
        primary_key = True,
        max_length = 50
    )
    fragment_identifier = models.CharField(
        max_length = 20,
        unique = True
    )
    title = models.CharField(
        max_length = 50,
        blank = False,
        unique = True
    )
    author = models.CharField(
        max_length = 50,
        blank = False
    )
    category = models.CharField(
        max_length = 2,
        blank = False,
        default = GN
    )
    hardware = models.CharField(
        max_length = 50
    )
    application = models.CharField(
        max_length = 50
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )    
    owner = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('owner', 'title', 'category')
        )

class Video(models.Model):
    IN = 'Introduction'
    CM = 'Complete'
    UN = 'Unofficial'

    staticfilepath = models.CharField(
        primary_key = True,
        max_length = 50 
    )
    title = models.CharField(
        max_length = 50,
        blank = False,
        unique = True 
    )
    director = models.CharField(
        max_length = 50, 
        blank = False
    )
    description = models.CharField(
        max_length = 50 
    )
    category = models.CharField(
        max_length = 2,
        blank = False,
        default = UN
    )
    hardware = models.CharField(
        max_length = 50
    )
    application = models.CharField(
        max_length = 50
    )
    date_created = models.DateField(
        default = date.today,
        blank = False
    )
    owner = models.ForeignKey(
        'User'
    )

    class Meta:
        unique_together = (
            ('owner', 'title', 'category')
        )

class Skill(models.Model):
    GN = "General"
    MD = 'Methods of development'
    OS = 'Operative system'
    FR = 'Framework'
    RC = 'Revision control'
    PR = 'Programming'
    ML = 'Markup language'
    DB = 'Database'
    SR = 'Server'
    SW = 'Sofrware'
    HW = 'Hardware'
    VA = 'Visual art'

    title = models.CharField(
        max_length = 10,
        blank = False
    )
    description = models.CharField(
        max_length = 255
    )
    category = models.CharField(
        max_length = 2,
        blank = False,
        default = GN
    )
    rating_on_five = models.DecimalField(
        max_digits = 1,
        decimal_places = 0
    )
    owner = models.ForeignKey(
        'User'
    )
    
    class Meta:
        unique_together = (
            ('owner', 'title', 'category')
        )

