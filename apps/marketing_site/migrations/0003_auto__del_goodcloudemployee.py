# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'GoodCloudEmployee'
        db.delete_table('marketing_site_goodcloudemployee')


    def backwards(self, orm):
        
        # Adding model 'GoodCloudEmployee'
        db.create_table('marketing_site_goodcloudemployee', (
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('marketing_site', ['GoodCloudEmployee'])


    models = {
        
    }

    complete_apps = ['marketing_site']
