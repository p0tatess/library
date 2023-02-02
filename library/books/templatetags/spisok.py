# from django import template
# from books.models import *
#
#
# register = template.Library()
#
# # @register.simple_tag()
# # def test(user):
# #     data = []
# #     from library.books.models import booksModel
# #     for i in booksModel.objects.filter(name=user):
# #             data.append(i.book)
# #     return data
#
# @register.simple_tag()
# def get_categories():
#     return booksModel.objects.all()


from django import template


register = template.Library()

@register.simple_tag()
def cal_str(word):
    res = "".join([str(s) for s in list(word)])
    return res

