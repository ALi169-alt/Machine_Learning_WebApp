from django.shortcuts import render


def predict(request):
  return render(request, 'prediction/prediction.html', {})
