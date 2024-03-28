from rest_framework import serializers
from .models import Course, User, Lesson, Tag, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = '/static/%s' % (obj.image)

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = '/static/%s' % (obj.image)

        return request.build_absolute_uri(path)

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date', 'course_id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
