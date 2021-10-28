from rest_framework import serializers
from .models import BookModel


class BookModelSerializer(serializers.ModelSerializer):
    def validate(self, data):
        title = data['title']
        if title:
            first_letter = title[0]
            if first_letter.islower():
                raise serializers.ValidationError('Title must start with capital letter!')
        return data

    class Meta:
        model = BookModel
        fields = '__all__'
