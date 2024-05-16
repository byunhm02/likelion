from rest_framework import serializers
from polls.models import Poll,Poll_agree,Poll_disagree

class PollSerializer(serializers.ModelSerializer):
    agreeRate=serializers.SerializerMethodField()
    disagreeRate=serializers.SerializerMethodField()
    class Meta:
        model=Poll
        fields=('id','title','description','agree','disagree','agreeRate','disagreeRate','createdAt')
        
    def get_agreeRate(self, obj):
            total_votes = obj.agree + obj.disagree
            if total_votes > 0:
                return (obj.agree / total_votes) 
            else:
                return 0


    def get_disagreeRate(self, obj):
            total_votes = obj.agree + obj.disagree
            if total_votes > 0:
                return (obj.disagree / total_votes) 
            else:
                return 0


#class PollSerializer(serializers.ModelSerializer):
#    agreerate=serializers.SerializerMethodField()
#    disagreerate=serializers.SerializerMethodField()
#    class Meta:
#        model=Poll
#        fields=('id','description','agree','disagree','agreerate','disagreerate','createdAt')
#        
#        def get_agreerate(self, obj):
#            return obj.agreerate()

#        def get_disagreerate(self, obj):
#            return obj.disagreerate()
        
#class PostSerializer(serializers.ModelSerializer):
    