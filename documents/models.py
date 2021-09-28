from django.db import models

class Document(models.Model):
    
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='files', max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True) #TODO correct format type for frontend
    nrDownloads = models.IntegerField(editable=False, default= 0)

    def __str__(self):
        return self.title


    def increment_nrDownloads(self):
        print("1")
        self.nrDownloads += 1
        self.save()
    
    