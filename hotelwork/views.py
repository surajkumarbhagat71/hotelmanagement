from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import TemplateView , View , ListView,DetailView
from django.utils.timezone import timezone
from django.views.generic.edit import UpdateView

# Create your views here.

class HomeView(TemplateView):

    template_name = 'maneeger/login.html'


class LoginView(View):
    def post(self,request,*args,**kwargs):

        if request.method == 'POST':
            username = self.request.POST.get('email')
            password = self.request.POST.get('password')

        cond = Q(email_id = username) & Q(password = password)

        check = Maneeger.objects.filter(cond).count()

        if (check == 1):
            request.session['login'] = username
            return redirect('dashaboard')
        else:
            return redirect('home')


class DashaboardView(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        context = {
            "rooms":Rooms.objects.all().count(),
            "avalblerooms":Rooms.objects.filter(room_status=False).count(),
            "rantedrooms":Rooms.objects.filter(room_status=True).count(),
            "roomcategory":Category.objects.all().count(),
            "allemplyee":Emplyee.objects.filter(status=True).count(),
            "allemplyeecategory":EmplyeeCategory.objects.all().count(),
        }

        return render(request,'maneeger/dashaboard.html',context)


class AddCategoryView(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        form = CategoryForm()
        context = {"form":form}
        return render(request,'maneeger/add_category.html',context)

    def post(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        form = CategoryForm(self.request.POST or None )

        if form.is_valid():
            form.save()
            return redirect('dashaboard')


class AddRoomView(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        form = RoomsForm()
        context = {"roomform":form}
        return render(request,'maneeger/add_room.html',context)

    def post(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        form = RoomsForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashaboard')


class AllRoomView(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        data = Rooms.objects.all()
        context = {"room":data}

        return render(self.request,'maneeger/all_room.html',context)


class AllCategoryView(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        data = Category.objects.all()
        context = {"category":data}

        return render(self.request,'maneeger/all_category.html',context)



class AvalableRooms(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        room = Rooms.objects.filter(room_status=False)

        context = {"avalableroom":room}

        return render(request,'maneeger/avalablerooms.html',context)


class RantedRooms(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        room = UserDetails.objects.filter(status=True)

        context = {"rantedroom":room}

        return render(request,'maneeger/checkin_user.html',context)


class Checkout_user_details(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        room = UserDetails.objects.filter(status=False)

        context = {"checkoutdetails":room}

        return render(request,'maneeger/checkouted_user_details.html',context)


class CheckinView(View):
    def get(self,request,pk,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        form = UserDetailsForms()
        context = {"form":form,"pk":pk}
        return render(request,'maneeger/checkin.html',context)

    def post(self,request,pk,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        form = UserDetailsForms(self.request.POST or None)

        if form.is_valid():
            x = form.save(commit=False)
            x.room_number = Rooms(pk)
            x.save()

            room = Rooms.objects.get(room_id=pk)
            room.room_status = True
            room.save()
            return redirect('dashaboard')


class CheckoutView(View):
    def get(self,request,pk,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        data = UserDetails.objects.get(cast_id=pk)
        data.status = False
        data.save()

        room_number = UserDetails.objects.get(cast_id=pk)
        room = Rooms.objects.get(room_id=room_number.room_number.room_id)
        room.room_status = False
        room.save()
        return redirect('dashaboard')


######################################################  Emplyee management ##################################

class AddEmplyeeView(View):
    def get(self,request,*args,**kwargs):
        form = EmapyForm()
        context = {"addemplyee":form}

        return render(request,'maneeger/add_emplyee.html',context)

    def post(self,request,*args,**kwargs):
        form = EmapyForm(request.POST or None ,request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('dashaboard')
        else:
            return redirect('add_emplyee')



class AddEmplyeeCategory(View):
    def get(self,request,*args,**kwargs):
        form = EmaplyeCategoryForm()
        context = {"addemplyecategory":form}

        return render(request, 'maneeger/add_emaplyee_category.html', context)

    def post(self,request,*args,**kwargs):
        form = EmaplyeCategoryForm(request.POST or None )

        if form.is_valid():
            form.save()
            return redirect('dashaboard')
        else:
            return redirect('add_emplyee_category')


class AllCurrentEmplyee(View):
    def get(self,request,*args,**kwargs):
        context = {"allemplyee":Emplyee.objects.filter(status=True)}

        return render(self.request,'maneeger/current_emplyee_list.html',context)


class AllEmplyeeRecords(View):
    def get(self,request,*args,**kwargs):
        context = {"allemplyeerecord":Emplyee.objects.filter(status=False)}

        return render(request,'maneeger/emplyee_records_list.html',context)


class AllEmplyeeCategory(View):
    def get(self,request,*args,**kwargs):
        data = {"allemplyeecategory":EmplyeeCategory.objects.all()}

        return render(request,'maneeger/all_emplyee_category.html',data)


class RemoveEmplyeeView(View):
    def get(self,request,pk,*args,**kwargs):

        data = Emplyee.objects.filter(emplyee_id = pk)
        data.status = False
        data.save()

        return render(request,'maneeger/dashaboard.html')

class EmplyeeDetailsView(View):
    def get(self,request,pk,*args,**kwargs):

        data = {"emplyee_detail":Emplyee.objects.get(emplyee_id=pk)}

        return render(request,'maneeger/emplyee_details.html',data)


class UpdateRoomCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'maneeger/add_category.html'




class LogoutView(View):
    def get(self,request):
        if request.session.has_key('login'):
            del request.session['login']
        return render(request,'maneeger/login.html')