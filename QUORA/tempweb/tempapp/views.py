# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})
def questions(request):
    questions = Question.objects.all()  # Assuming you have a Question model
    context = {
        'questions': questions,
        'username': request.user.username,
    }
    return render(request, 'questions.html', context)



def question_detail(request, question_id):
    print("here")
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.question = question
            new_answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        answer_form = AnswerForm()
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'answer_form': answer_form})
# def question_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'question_detail.html', {'question': question})

def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'new_question.html', {'form': form})

# def answer_question(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.question = question
#             answer.save()
#             return redirect('question_detail', question_id=question.id)
#     else:
#         form = AnswerForm()
    
#     context = {
#         'question': question,
#         'form': form,
#     }
#     return render(request, 'answer_question.html', context)
# views.py


# def edit_answer(request, answer_id):
#     answer = get_object_or_404(Answer, pk=answer_id)
    
#     if request.method == 'POST':
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             form.save()
#             # Assuming you redirect back to the question detail after editing an answer
#             return redirect('question_detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
    
#     return render(request, 'edit_answer.html', {'form': form, 'answer': answer})



def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        question.delete()
        return redirect('index')  # Redirect to the list of questions or any other appropriate URL
    
    return render(request, 'delete_question.html', {'question': question})


def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('/', pk=question_id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'edit_question.html', {'form': form})
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        answer.delete()
        return redirect('index')  # Replace 'some_view_name' with the name of the view you want to redirect to after deletion
    return render(request, 'delete_answer.html', {'answer': answer})


#from django.shortcuts import render, get_object_or_404, redirect
#from .models import Answer
#from .forms import AnswerForm

def edit_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('answer_detail', answer_id=answer.pk)  # Redirect to answer detail or another view
    else:
        form = AnswerForm(instance=answer)
    
    return render(request, 'edit_answer.html', {'form': form, 'answer': answer})

def submit_answer(request, question_id):
    # Handle form submission logic here
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # Process form data and save to database
            answer = form.save(commit=False)
            answer.question_id = question_id
            answer.save()
            return redirect('question_detail', question_id=question_id)  # Redirect to the question detail page
    else:
        form = AnswerForm()
    
    return render(request, 'submit_answer.html', {'form': form})
