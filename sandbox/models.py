from django.db import models
import uuid


class FILE_HASHES(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255, unique=True)
    file_hash = models.CharField(max_length=64)

    def __str__(self):
        return self.file_name



