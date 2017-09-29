# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  slug = models.SlugField(max_length=50)
  created_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.title