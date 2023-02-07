from rest_framework import serializers

from pokemon.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"

    def validate_name(self, value):
        """Validate name does not exist and return lower case

        Args:
            value (_type_): Value from data object

        Raises:
            serializers.ValidationError: Pokemon already exists

        Returns:
            _type_: Lower case value
        """
        lower_value = value.lower()
        if Pokemon.objects.filter(name=lower_value).exists():
            raise serializers.ValidationError(f"{value} already exists")
        return lower_value

    def validate_type_1(self, value):
        """Check if type_1 exists

        Args:
            value (_type_): Value from data object

        Returns:
            _type_: Lower case value
        """
        if value:
            return value.lower()

    def validate_type_2(self, value):
        """Check if type_2 exists

        Args:
            value (_type_): Value from data object

        Returns:
            _type_: Lower case value
        """
        if value:
            return value.lower()
