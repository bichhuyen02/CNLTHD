from .models import Xe, LoaiXe, Ghe, GiaVe, BenXe, ChuyenXe, User, NhanVien, KhachHang, Complain
from rest_framework import serializers




#xe
class LoaiXeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoaiXe
        fields = ['id', 'name', 'active']

class XeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    # loaiXe = LoaiXeSerializer()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/static/%s" % obj.image.name


    class Meta:
        model = Xe
        fields = ['id', 'name', 'bienSo', 'loaiXe', 'image', 'active']

class GheSerializer(serializers.ModelSerializer):
    # xe = XeSerializer()
    class Meta:
        model = Ghe
        fields = ['id', 'name', 'xe', 'active']



#ve
class GiaVeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GiaVe
        fields = ['id', 'gia', 'loai', 'active']

class VeSerializer(serializers.ModelSerializer):
    pass
    # class Meta:
    #     model = GiaVe
    #     fields = ['id', 'gia', 'loai', 'active']



#chuyen xe
class BenXeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BenXe
        fields = ['id', 'name', 'description', 'active']

class ChuyenXeSerializer(serializers.ModelSerializer):
    # diemDen = TagSerializer(many=True)
    class Meta:
        model = ChuyenXe
        fields = '__all__'



#account
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'avatar']

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user

class NhanVienSerializer(serializers.ModelSerializer):

    class Meta:
        model = NhanVien
        fields = ['birth', 'phone', 'user']

class TaiXeSerializer(serializers.ModelSerializer):
    bangLai = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.bangLai:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.bangLai.name)
            return "/static/%s" % obj.bangLai.name


    class Meta:
        model = NhanVien
        fields = ['birth', 'phone', 'user', 'bangLai']

class KhachHangSerializer(serializers.ModelSerializer):

    class Meta:
        model = KhachHang
        fields = ['birth', 'phone', 'user']



#complain
class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ['id', 'content']