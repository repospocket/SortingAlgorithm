from django.shortcuts import render
from .ListofListsSort import ListofListsSort
from .TrieNodeSort import TrieNodeSort, NodeEncoder
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse
import json
from django.shortcuts import render
from Sorting_app.forms import SortingForm



def submit_form_view(request):
    if request.method == 'POST':
        form = SortingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            # Process the submitted form data
            # Call your sorting function with the data
            input_list = [int(x) for x in data.split(',')]
            # Call the sorting function
            list_sorter = TrieNodeSort()

            # Call the sort_list method on the instance
            [fisrtnode,sortedlist] = list_sorter.sort_list(input_list)
            # Pass the sorted list or any other data to the template
            json_data = json.dumps(fisrtnode, cls=NodeEncoder)
            return JsonResponse([json_data,sortedlist], safe=False)
        else:
            # Form is not valid, return a 404 error response
            return HttpResponseNotFound()
    else:
        form = SortingForm()
    return render(request, 'submit_form.html', {'form': form})