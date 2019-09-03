from rest_framework import serializers
from polls.models import Question, Choice
from django.contrib.auth.models import User, Group



class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')

class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True, required=True)
    class Meta:
        model = Question
        fields = ('pub_date', 'question_text', 'status', 'choice_set')

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        choice_set_serializer = self.fields['choice_set']
        for each in choice_validated_data:
            each['question'] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question

    def validate(self, data):
        validated_data = super(QuestionSerializer, self).validate(data)
        choice_validated_data = validated_data['choice_set']
        print(len(choice_validated_data))
        if len(choice_validated_data) != 4:
            raise serializers.ValidationError('There should be 4 Choices')
        return validated_data

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']