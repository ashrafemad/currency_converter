from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from currencies.models import Currency
from users.models import ActivityLog


class ConvertCurrencySerializer(serializers.Serializer):
    from_currency = serializers.CharField()
    to_currency = serializers.CharField()
    amount = serializers.DecimalField(max_digits=8, decimal_places=5)

    def validate(self, attrs):
        available_currencies = Currency.available_currencies()
        from_currency = attrs['from_currency'].upper()
        to_currency = attrs['to_currency'].upper()
        if from_currency not in available_currencies or to_currency not in available_currencies:
            raise ValidationError(f'Please select valid currency,'
                                  f' current avaliable currencies '
                                  f'are {", ".join(available_currencies)}')

        attrs['from_currency'] = from_currency
        attrs['to_currency'] = to_currency
        return attrs

    def create(self, validated_data):
        user = self.context['user']
        convert_result = Currency.convert(validated_data['from_currency'],
                               validated_data['to_currency'],
                               validated_data['amount'])
        ActivityLog.log(
            user, validated_data['from_currency'], validated_data['to_currency']
        )
        return convert_result

    def to_representation(self, converted_amount):
        return {'converted_amount': converted_amount}
