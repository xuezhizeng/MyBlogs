# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.URLField(choices=[('http://or6fe9yua.bkt.clouddn.com/image/A-480x270.jpg', 'A'), ('B', 'http://or6fe9yua.bkt.clouddn.com/image/B-480x270.jpg'), ('C', 'http://or6fe9yua.bkt.clouddn.com/image/C-480x270.jpg'), ('D', 'http://or6fe9yua.bkt.clouddn.com/image/D-480x270.jpg'), ('E', 'http://or6fe9yua.bkt.clouddn.com/image/E-480x270.jpg'), ('F', 'http://or6fe9yua.bkt.clouddn.com/image/F-480x270.jpg'), ('G', 'http://or6fe9yua.bkt.clouddn.com/image/G-480x270.jpg'), ('H', 'http://or6fe9yua.bkt.clouddn.com/image/H-480x270.jpg'), ('I', 'http://or6fe9yua.bkt.clouddn.com/image/I-480x270.jpg'), ('J', 'http://or6fe9yua.bkt.clouddn.com/image/J-480x270.jpg'), ('K', 'http://or6fe9yua.bkt.clouddn.com/image/K-480x270.jpg'), ('L', 'http://or6fe9yua.bkt.clouddn.com/image/L-480x270.jpg'), ('M', 'http://or6fe9yua.bkt.clouddn.com/image/M-480x270.jpg'), ('N', 'http://or6fe9yua.bkt.clouddn.com/image/N-480x270.jpg'), ('O', 'http://or6fe9yua.bkt.clouddn.com/image/O-480x270.jpg'), ('P', 'http://or6fe9yua.bkt.clouddn.com/image/P-480x270.jpg'), ('Q', 'http://or6fe9yua.bkt.clouddn.com/image/Q-480x270.jpg'), ('R', 'http://or6fe9yua.bkt.clouddn.com/image/R-480x270.jpg'), ('S', 'http://or6fe9yua.bkt.clouddn.com/image/S-480x270.jpg'), ('T', 'http://or6fe9yua.bkt.clouddn.com/image/T-480x270.jpg'), ('U', 'http://or6fe9yua.bkt.clouddn.com/image/U-480x270.jpg'), ('V', 'http://or6fe9yua.bkt.clouddn.com/image/V-480x270.jpg'), ('W', 'http://or6fe9yua.bkt.clouddn.com/image/W-480x270.jpg'), ('X', 'http://or6fe9yua.bkt.clouddn.com/image/X-480x270.jpg'), ('Y', 'http://or6fe9yua.bkt.clouddn.com/image/Y-480x270.jpg'), ('Z', 'http://or6fe9yua.bkt.clouddn.com/image/Z-480x270.jpg')], verbose_name='题图'),
        ),
    ]
