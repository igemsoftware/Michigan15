from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm

PROTOCOL_TYPES = (
    ('BC', 'Biochemistry'),
    ('BI', 'Bioinformatics'),
    ('BT', 'Botany'),
    ('CB', 'Cell Biology'),
    ('CH', 'Chemistry'),
    ('DB', 'Developmental Biology'),
    ('GN', 'Genetics'),
    ('IM', 'Immunology'),
    ('MB', 'Molecular Biology'),
    ('TC', 'Tissue Culture')
)
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

class Protocol(models.Model):
    title = models.TextField()
    author = models.ManyToManyField(Author)
    date_of_upload = models.DateField
    protocol_type = models.CharField(max_length=2, choices=PROTOCOL_TYPES, null=True)
    rating = models.DecimalField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        max_digits=3, decimal_places=2, default = 0.00)
    protocol = models.TextField(default = '')

class ProtocolForm(ModelForm):
    class Meta:
        model = Protocol
        fields = ['title', 'protocol_type', 'protocol']