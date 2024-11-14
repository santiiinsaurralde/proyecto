from rest_framework import serializers
from .models import Project


class myappApi(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ("id" , "project") 
        read_only_fields=("done", )

      #"title", "project" ,"done"  
