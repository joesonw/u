from django.db import models
from django.db.models.fields import Field
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions
from django.dispatch import dispatcher,Signal
from django.db.models import signals

# -----------Threads and Entry---------------



class Renren_Thread(models.Model):

	def delete(self):		
		pass

class WB_Thread(models.Model):
	pass
	
class QQT_Thread(models.Model):
	pass
	
class Site_Thread(models.Model):
	pass
	
class Entry(models.Model):
	pass

#-------------Bind Listeners--------------
def bind_entry():
	pass
def on_delete():
	pass


class ArrayField(models.Field):
    description = _("Array")
    __metaclass__ = models.SubfieldBase
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 200
        super(ArrayField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "ArrayField"
    def to_python(self, value):
        if value is None:
            return None
        elif value == "":
            return []
        elif isinstance(value,basestring):
            try:
                return [int(i) for i in value.split("|")]
            except (ValueError,TypeError):
                raise exceptions.ValidationError(self.error_messages['invalid value'])
            
    
        if isinstance(value,list):
            return value
        else:
            return []
        
    def get_prep_value(self,value):
        if not value:
            return ""
        elif isinstance(value,basestring):
            return value
        else:
            return "|".join([str(i) for i in value])
            
    def fromfield(self,**kwargs):
    	pass

    def value_to_string(self,obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(obj)

