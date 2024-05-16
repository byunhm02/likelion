from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Poll,Poll_agree,Poll_disagree
from .serializers import PollSerializer

# Create your views here.
#@api_view(['GET']) #/poll
#def poll_list(requst):
#    poll=Poll.objects.order_by('-createdAt')
#    #poll=Poll.objects.all()
#    serializer=PollSerializer(poll,many=True)
#    return Response(serializer.data)

    
#@api_view(['POST']) #/poll
#def poll_register(requst):
#    pass

@api_view(['GET','POST'])
def poll(request):
    if request.method=='GET':
        sort_by = request.query_params.get('sort', 'latest')
        
        # 정렬 기준에 따라 쿼리셋을 정렬
        if sort_by == 'latest':
            poll = Poll.objects.order_by('-createdAt')
        elif sort_by == 'oldest':
            poll = Poll.objects.order_by('createdAt')
        elif sort_by == 'agree':
            poll = Poll.objects.order_by('-agree')
        elif sort_by == 'disagree':
            poll = Poll.objects.order_by('-disagree')
        else:
            # 유효하지 않은 정렬 기준이 주어진 경우 기본값 사용
            poll = Poll.objects.order_by('-createdAt')

        serializer = PollSerializer(poll, many=True)
        return Response(
            serializer.data
        , status=200)
        
        
        #poll=Poll.objects.order_by('-createdAt')
        #serializer=PollSerializer(poll,many=True)
        #return Response({
        #    'message':'조회 성공',
        #    'data': serializer.data
        #    },status=200)
        
        
    elif request.method=='POST':
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE']) #/poll/{pollid}
def poll_detail(request,id):
    if request.method=='GET':
        
        try:
            poll=Poll.objects.get(id=id)
        except Poll.DoesNotExist:
            return Response({
                'message': '투표가 존재하지 않습니다.'
            },status=404)
        serializer = PollSerializer(poll)
        return Response(serializer.data
                ,status=200)
    if request.method=='PUT':
        try:
            poll=Poll.objects.get(id=id)
        except Poll.DoesNotExist:
            return Response({
                'message': '투표가 존재하지 않습니다.'
            },status=404)
        serializer=PollSerializer(poll,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            ,status=200)
    if request.method=='DELETE':
        try:
            poll=Poll.objects.get(id=id)
        except Poll.DoesNotExist:
            return Response({
                'message': '투표가 존재하지 않습니다.'
            },status=404)
        poll.delete
        return Response({
            'message': '삭제 성공'
        }, status=204)
        
#@api_view(['PUT'])#/poll/{pollid}
#def poll_modify(request,id):
#    try:
#        poll=Poll.objects.get(id=id)
#    except Poll.DoesNotExist:
#        return Response({
#            'message': '투표가 존재하지 않습니다.'
#        },status=404)
#    if request.method=='PUT':
#        serializer=PollSerializer(poll,data=request.data)
 #       if serializer.is_valid():
 #           serializer.save()
 #           return Response({
 #               'message':'수정성공',
#                'data':serializer.data
#            },status=200)

#@api_view(['DELETE']) #/poll/{pollid}
#def poll_del(request,id):
#    pass
    
#@api_view(['GET','PUT','DELETE'])
#def viewpoll(request,id):
#    if request.method=='GET':
#        poll=Poll.objects.get(id=id)
#        serializer=PostSerializer(poll)
    
    
    
@api_view(['POST']) #/poll/{pollid}/agree
def vote_agree(requst,id):
    try:
        poll=Poll.objects.get(id=id)
    except Poll.DoesNotExist:
        return Response({'message':'투표항목이 존재하지 않습니다'})
    poll.agree+=1
    poll.save()
    serializer = PollSerializer(poll)
    return Response(serializer.data
    ,status=200)
    
    

@api_view(['POST']) #/poll/{pollid}/disagree
def vote_disagree(requst,id):
    try:
        poll=Poll.objects.get(id=id)
    except Poll.DoesNotExist:
        return Response({'message':'투표항목이 존재하지 않습니다'})
    poll.disagree+=1
    poll.save()
    serializer = PollSerializer(poll)
    return Response(serializer.data
    ,status=200)
