from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'Nitip Barang',
        'nama': 'Febrian Irvansyah',
        'kelas': 'PBP-A'
    }

    return render(request, "main.html", context)