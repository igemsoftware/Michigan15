import datetime
from django.template import loader
from django.template import Context
from haystack import indexes
from protocat_app.models import Protocol

class ProtocolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Protocol

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
