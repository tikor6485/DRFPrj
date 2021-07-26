from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from .serializers import PersonSerializer
# from .models import Person
# from rest_framework import ISAdminUser

@api_view(['GET', 'POST'])
def one(request):
    if request.method== 'POST':
        userName = request.data['name']
        return Response({'name':f'My name is {userName}'})
    else:
        return Response({'name':'My name is Tirdad'})


# @api_view()
# def persons(request):
#     persons = Person.objects.all()
#     ser_data = PersonSerializer(persons, many=True)
#     return Response(ser_data.data)
    

# @api_view()
# @permission_classes([ISAdminUser,])
# def person(request, id):
#     try:
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist():
#         return Response({'error':'This user is not exist'})
#     ser_data = PersonSerializer(person)
#     return Response(ser_data.data)


# @api_view(['POST'])
# def person_create(request):
#     info = PersonSerializer(data=request.data)
#     if info.is_valid():
#         # Person(newName = info.validated_data['newName'], newAge = info.validated_data['newAge'], newEmail = info.validated_data['newEmail']).save()
#         info.save()
#         return Response({'message':'OK'})
#     else:
#         return Response(info.errors)
