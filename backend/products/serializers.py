from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicUserSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductInlineSerializer(serializers.Serializer):
     url = serializers.HyperlinkedIdentityField(
          view_name='product-detail',
          lookup_field='pk',
          read_only=True
     )
     title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicUserSerializer(source='user', 
    read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',   
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)
    
    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()

