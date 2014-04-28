from django.core.urlresolvers import reverse
from djangorestframework.views import View
from djangorestframework.resources import ModelResource
from models import *

class LineItemResource(ModelResource):
    model = LineItem
    fields = ('product', 'unit_price', 'quantity')
    def product(self, instance):
        return instance.product.title
