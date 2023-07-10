class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6

TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5

TravelBlog.total_blogs += 1

# class TravelBlog:
#     total_blogs = 0
#
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#         TravelBlog.total_blogs += 1
#
# tb1 = TravelBlog('Франция', 6)
# tb2 = TravelBlog('Италия', 5)
