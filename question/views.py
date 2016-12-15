from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from question.models import Question, Answer, Comment
from .forms import QuestionForm
from .forms import AnswerForm
from .forms import CommentForm
from django.utils import timezone
from django.template.context_processors import csrf
from django.contrib import messages
from django.conf import settings
from notification.models import Notification
from userprofile.models import UserProfile
from question.models import Tag


def questions(request):
    args = {}
    args.update(csrf(request))
    args['questions'] = Question.objects.all().order_by('-creation_time')
    args['notification'] = Notification.objects.filter(
        user=request.user, viewed=False)
    args['userprofile'] = UserProfile.objects.get(id=request.user.id)
    return render_to_response('questions.html', args)


def question(request, question_id=1):
    return render(request, 'final.html', {'question': Question.objects.get(id=question_id), 'user': request.user.id})


def tag(request, tag_id=1):
    return render(request, '', {'tag': Tag.objects.get(id=tag_id)})


def tags(request):
    args = {}
    args.update(csrf(request))
    args['tags'] = Tag.objects.all()
    return render_to_response('tags.html', args)


def add_question(request):
    if request.POST:
        form = QuestionForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.creation_time = timezone.now()
            a.updation_time = timezone.now()
            a.by = request.user
            a.save()
            form.save_m2m()
            return HttpResponseRedirect('/question/all')
    else:
        form = QuestionForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('add_question.html', args)


def like_question(request, question_id=1):
    x = Question.objects.get(id=question_id)
    p = request.user
    x.likes.add(p)
    x.save()
    return HttpResponseRedirect('/question/all')


def upvote_answer(request, answer_id=1):
    x = Answer.objects.get(id=answer_id)
    p = x.question.id
    a = request.user
    x.upvoted_by.add(a)
    x.save()
    return HttpResponseRedirect("/question/add_answer/%s" % p)


def downvote_answer(request, answer_id=1):
    x = Answer.objects.get(id=answer_id)
    p = x.question.id
    a = request.user
    x.downvoted_by.add(a)
    x.save()
    return HttpResponseRedirect("/question/add_answer/%s" % p)


def delete_answer(request, answer_id):
    c = Answer.objects.get(id=answer_id)
    p = c.question.id
    c.delete()
    messages.add_message(request, settings.DELETE_MESSAGE, "Answer Deleted")
    return HttpResponseRedirect("/question/get/%s" % p)


def add_answer(request, question_id=1):
    a = Question.objects.get(id=question_id)
    if request.method == "POST":
        f = AnswerForm(request.POST or None, request.FILES or None)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.by = request.user
            c.question = a
            c.save()
            return HttpResponseRedirect('/question/add_answer/%s' % question_id)
    else:
        f = AnswerForm()
    args = {}
    args.update(csrf(request))
    args['question'] = a
    args['form'] = f
    return render_to_response('final.html', args)


def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    c.delete()
    return HttpResponseRedirect("/question/get/%s" % c.answer.id)


def add_comment(request, answer_id=1):
    a = Answer.objects.get(id=answer_id)
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.comment_date = timezone.now()
            c.answer = a
            c.save()
            return HttpResponseRedirect('/question/get/%s' % a.id)
    else:
        f = CommentForm()
    args = {}
    args.update(csrf(request))
    args['answer'] = a
    args['form'] = f
    return render_to_response('add_comment.html', args)


def search_title(request):
    if request.method == "POST":
        search_text = request.POST("search_text")
    else:
        search_text = ''
    res = Question.objects.filter(title__contains=search_text)
    return render_to_response("question_search.html", {'questions': res})
