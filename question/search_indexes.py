
from haystack import indexes
from question.models import Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    creation_time = indexes.DateTimeField(model_attr='creation_time')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Question

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
