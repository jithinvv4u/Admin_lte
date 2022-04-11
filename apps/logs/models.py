from django.db import models

class ErrorLogs(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    function_name = models.CharField(max_length=300,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    resolved_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ffz_error_logs'

    def __str__(self):
        return str(self.id)
