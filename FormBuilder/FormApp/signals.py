from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response, AnalyticsCache

@receiver(post_save, sender=Response)
def update_analytics(sender, instance, **kwargs):
    form = instance.form
    responses = form.responses.all()
    analytics_data = {}

    for question in form.questions.all():
        if question.question_type == 'text':
            word_counts = {}
            for response in responses:
                answer = response.data.get(question.text, "")
                for word in answer.split():
                    if len(word) >= 5:
                        word_counts[word] = word_counts.get(word, 0) + 1
            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            analytics_data[question.id] = {
                'top_words': dict(sorted_words[:5]),
                'Others': sum(count for _, count in sorted_words[5:])
            }

        elif question.question_type == 'checkbox':
            combination_counts = {}
            for response in responses:
                answer = tuple(sorted(response.data.get(question.text, [])))
                combination_counts[answer] = combination_counts.get(answer, 0) + 1
            sorted_combinations = sorted(combination_counts.items(), key=lambda x: x[1], reverse=True)
            analytics_data[question.id] = {
                'top_combinations': dict(sorted_combinations[:5]),
                'Others': sum(count for _, count in sorted_combinations[5:])
            }

        elif question.question_type == 'dropdown':
            option_counts = {}
            for response in responses:
                answer = response.data.get(question.text, "")
                option_counts[answer] = option_counts.get(answer, 0) + 1
            sorted_options = sorted(option_counts.items(), key=lambda x: x[1], reverse=True)
            analytics_data[question.id] = {
                'top_options': dict(sorted_options[:5]),
                'Others': sum(count for _, count in sorted_options[5:])
            }

    AnalyticsCache.objects.update_or_create(form=form, defaults={'data': analytics_data})
