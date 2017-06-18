#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.forms import forms
from django.contrib.staticfiles.templatetags.staticfiles import static

__author__ = '@elinaldosoft'


class Bootstrap4Select(object):
    def build_attrs(self, extra_attrs=None, **kwargs):
        attrs = super(Bootstrap4Select, self).build_attrs(extra_attrs, **kwargs)
        attrs.setdefault('data-theme', 'bootstrap')
        return attrs

    def _get_media(self):
        return forms.Media(
            js=(
                '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                settings.SELECT2_JS,
                static('django_select2/django_select2.js'),
            ),
            css={'screen': (
                settings.SELECT2_CSS,
                '//cdnjs.cloudflare.com/ajax/libs/select2-bootstrap-css/1.4.6/select2-bootstrap.css',)}
        )

    media = property(_get_media)
