""" Middleware for storing http requests """
from profile.models import DbLog
from django.db import connection


class StoreDbRequestMiddleware(object):
    """ Store all db requests in database """
    
    def process_response(self, request, response):
      queries = connection.queries[:]  
      for query in queries:
          DbLog.objects.create(sql=query['sql'])
      return response
