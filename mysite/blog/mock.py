from django.http import Http404

class Post():

	POSTS= [
		{'id': 1 , 'title' : ' First post' , 'body' : ' this my First post '},
		{'id': 2 , 'title' : ' second post' , 'body' : ' this my second post '},
		{'id': 3 , 'title' : ' third post' , 'body' : ' this my third post '},
	]

	@classmethod
	def  all(cls):
		return cls.POSTS

	@classmethod
	def find(cls,id):
		try:
			return cls.POSTS[int(id) - 1]
		except:
			raise Http404('sorry ,post  # {} not found'.format(id))
		