from rest_framework import serializers
from factors.models import Activity
# from users.models import User

class ActivityCreateSerializer(serializers.ModelSerializer):
    value = serializers.FloatField(write_only=True)  
    co2_emission = serializers.FloatField(read_only=True) 

    class Meta:
        model = Activity
        fields = ['category', 'value', 'co2_emission']

    def create(self, validated_data):
        user = self.context['request'].user
        category = validated_data['category']
        value = validated_data.pop('value')

        if value > 0:
            if category == 'transport':
                co2_emission = value * 0.21
            elif category == 'energy':
                co2_emission = value * 0.5
            else:
                co2_emission = 0
        else:
            co2_emission = 0

        # DB ga saqlaymiz
        activity = Activity.objects.create(
            user=user,
            category=category,
            co2_emission=co2_emission,
        )
        return activity
    

